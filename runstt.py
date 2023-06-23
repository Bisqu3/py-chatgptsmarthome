#HANDLES ALL AUDIO IN AND OUT.
#once confident and user has stopped talking, send text to main to go to chatgpt.
import os
#STT dependencies
import queue
import pyaudio
from google.cloud import speech_v1p1beta1 as speech
#main communication between user and chatgpt
from gpthandler import *
from configure.py import *
#TTS dependencies
import pyttsx3


"""

        PUT YOUR GOOGLE CLOUD API JSON FILE IN THE KEYS FOLDER. RENAME IT TO auth.json

"""
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys/auth.json"

RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

#MicrophoneStream class from pyaudio docs with added microphone selection
class MicrophoneStream(object):
    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self): 
        self._audio_interface = pyaudio.PyAudio()

        # List all audio input devices
        device_index = None
        for i in range(self._audio_interface.get_device_count()):
            dev_info = self._audio_interface.get_device_info_by_index(i)
            print(dev_info)
            if dev_info["name"].lower() == snag(1).lower(): # Use the exact name of your microphone
                device_index = i
                break
        if device_index is None:
            raise Exception("Could not find the microphone device. enter exact name in stt.py")

        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=1, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
            input_device_index=device_index,
            stream_callback=self._fill_buffer,
        )
        self.closed = False

        return self


    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b"".join(data)


def listenloop(responses):
    for response in responses:
        if not response.results:
            continue

        result = response.results[0]

        if not result.alternatives:
            continue

        transcript = result.alternatives[0].transcript

        #ship user prompt to main.py
        if result.is_final:
            print(f"Transcript: {transcript}\n")
            response = speechreceived(transcript)
            pyttsx3.speak(response)
            
                


def main():
    #google cloud shit
    language_code = "en-US"

    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code,
    )
    streaming_config = speech.StreamingRecognitionConfig(
        config=config,
        interim_results=True,
    )
    #With microphone input as stream, get stt response and feed to listen loop
    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )

        responses = client.streaming_recognize(streaming_config, requests)

        #listen loop. loop through response strings until final response is received.
        listenloop(responses)


if __name__ == "__main__":
    main()
