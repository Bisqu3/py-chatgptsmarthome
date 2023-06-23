#Main com with chatgpt. manages the assistant and its memory.

import os
import sqlite3 as sql
import openai
import time
from lightcontrol import *
from configure import *

#main loop for progressive conversation


"""

        PUT YOUR OPENAI API KEY IN keys/OPENAI-KEYHERE.txt 

"""


#TODO Get light control in one function. have to tweak chatgpts system prompt
def lights(location, state):
    t = "Lights at {0} are set to {1}".format(location,state)
    print(t)
    lightstate(location, state)

def speechreceived(prompt):
    openai.api_key = snag(0)
    #Decides how chatgpt reacts.
    #TODO define more control methods.
    # SHC_ tag for smart home control
    SystemPrompt = """you will SOMETIMES be provided with user responses for smart home control.
    when this happens respond ONLY with a tag and the tags location and state.
    the tags state is decided with binary. 0 is off. 1 is on.
     working examples are SHC_lights('office', 0)$$ and SHC_lights('livingroom', 1)$$.
     other examples are SHC_fans('bedroom', 1)$$ or SHC_pump('balcony', 0)$$.
     get the location IF the user did not provide context for one.
     the location should be in quotations and have NO SPACES.
     sometimes the user will NOT want smart home control, CONSIDER you will have to alternate between assistance AND smart home control."""
    #TODO get from database. so assistant cant recollect things
    short_term_mem = [{"role": "system", "content": SystemPrompt}]

    curmessage = {"role": "user", "content": prompt}
    short_term_mem.append(curmessage)
    #query sent to openai
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = short_term_mem)
    res = chat_completion.choices[0].message.content
    resmessage = {"role": "assistant", "content": str(res)}
    print("Response: "+res)
    p = res.find("SHC_")
    e = res.find("$$")
    if p > -1:
        res = res[p+4:e]
        print("modified response: "+res)
    try:
        #Try function
        exec(res)
    except:
        print("_function not found")
        #TTS
        return res
    #TODO log to db