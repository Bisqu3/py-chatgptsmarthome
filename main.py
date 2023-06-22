import os
import sqlite3 as sql
import openai
from gtts import gTTS
from playsound import playsound
#main loop for progressive conversation

def lightsoff(location):
    print("Lights off in "+location)
    #TODO
def lightson(location):
    print("Lights on in "+location)
    #TODO


def main():
    with open('key.txt') as f:
        key = f.readlines()
        print(key[0])
    #DONT REVEAL THIS KEY! ENCRYPT AND HIDE IT LATER
    openai.api_key = key[0]
    #DONT REVEAL THIS KEY ^^^^^^^^^^^^^^^^^^^^^^^^^^

    #prompt for chatgpt to follow in its responses
    SystemPrompt = "you will SOMETIMES be provided with user responses for smart home control. when this happens please respond ONLY with a tag and its state. working examples are lightsoff(location) and lightson(location). other examples are fanoff('bathroom') or pumpon('livingroom'). get the location if the user did not provide context for one. the location should be in quotations and have no spaces. sometimes the user will not want smart home control, please consider."
    #holds line of conversation between you and chatgpt
    #short term memory
    chathistory = [{"role": "system", "content": SystemPrompt}]
    #log to db when?

    while True:
        userinput = input("Prompt: ")
        if userinput == "-histlog":
            print(chathistory)
            main()
        elif userinput == "-dumpmem":
            chathistory = [{"role": "system", "content": SystemPrompt}]
            print("Conversation Cleared.")
            main()
        curmessage = {"role": "user", "content": userinput}
        chathistory.append(curmessage)
        #query sent to openai
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=chathistory)
        resmessage = {"role": "assistant", "content": str(chat_completion.choices[0].message.content)}
        chathistory.append(resmessage)
        print("Response: "+chat_completion.choices[0].message.content)

        testspeak = gTTS(text = chat_completion.choices[0].message.content, lang = "en", slow = False)
        testspeak.save("speech.mp3")

        try:
            exec(chat_completion.choices[0].message.content)
        except:
            print("probably not a command")
        #TODO log to db
        #TODO speech recognition to user input. speech to text for assistant response.

print("-dumpmem || clears conversation topic.\n -histlog || show the logged conversation")
main()