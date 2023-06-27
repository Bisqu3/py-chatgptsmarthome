#Main com with chatgpt. manages the assistant and its memory.

import os
import sqlite3 as sql
import openai
import time
from lightcontrol import *
from configure import *

#new stuff
import webbrowser
from memhandler import *
from spotifycontrol import *

#FUNCTIONS FOR ASSISTANT USE
#light control with phue
def lights(location, state):
    t = "Lights at {0} are set to {1}".format(location,state)
    print(t)
    lightstate(location, state)

#browser access
def show(url):
    webbrowser.open(url, new = 0, autoraise = True)

#records what you say after asking it to record
def notepad(msg):
    print(msg) 

def showlog():
    print(short_mem)

#main loop for progressive conversation
def speechreceived(prompt):
    openai.api_key = snag(0)
    UserInfo = "My name is User."
    #Decides how chatgpt reacts.
    # SHC_ tag for smart home control
    SystemPrompt = """you will SOMETIMES be provided with user responses for smart home control.
    when this happens respond ONLY with a tag according to the rules numbered below:
    1. the tags state is decided by an 8-bit value. 0 is off. 255 is on. the light may be dimmed between 0-255. consider user input on what level it should be set to. working examples are SHC_lights('office', 0)$$ and SHC_lights('livingroom', 255)$$. other examples are SHC_lights('bedroom', 177)$$ or SHC_pump('balcony', 0)$$. get the location IF the user did not provide context for one. lamp is an acceptible location. the location should be in quotations and have NO SPACES.
    2. the user may ask you to start recording a message for them. when this happens, respond with SHC_notepad('users-message')$$
    3.sometimes the user WILL NOT want smart home control, CONSIDER you will have to alternate between assistance AND smart home control.
    4. the user may say 'show me' and then provide info on their request. when this happens, respond with SHC_show('website-url')$$ where website-url is a link to the related subject
    5. the user may say 'play' or 'on spotify' followed by a song name or artist. when this happens respond with SHC_playspotify('enter-song')$$ where enter-song is the song or artist the user is requesting.
    6. other spotify features include SHC_likesong()$$ and SHC_addsong(enter-song)$$. 
    7. the user may say 'picture of' or 'pull up an image' followed by a request. when this happens respond with SHC_show('image-url')$$ where image-url is a google image link searching for the users topic.
    8. the user may say 'show me conversation logs' or 'conversation history'. when this happens respond with SHC_showlog()$$
    The user has provided info about themselves: """+UserInfo+"""
    """
    #TODO get from database. so assistant can recollect things
    short_term_mem = [{"role": "system", "content": SystemPrompt}]

    curmessage = {"role": "user", "content": prompt}
    short_mem.append(curmessage)
    #combine local short-term-mem with global short-mem
    short_term_mem += short_mem
    #print(short_term_mem)
    #query sent to openai
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = short_term_mem)
    res = chat_completion.choices[0].message.content
    resmessage = {"role": "assistant", "content": str(res)}
    short_mem.append(resmessage)
    print("==ChatGPT response==")
    print(res)
    p = res.find("SHC_")
    e = res.find("$$")
    if p > -1:
        res = res[p+4:e]
        print("modified response: "+res)
    try:
        #Try function
        exec(res)
        return res
    except:
        print("_function not found")
        #TTS
        return res
    #TODO log to db