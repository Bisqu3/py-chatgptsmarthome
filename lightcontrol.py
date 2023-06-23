from phue import Bridge
from time import sleep
from configure import *


"""
        light control is room name with an array of light names within that room
"""
office = ['Den1', 'Den2']
livingroom = ['Livingroom1', 'Livingroom2', 'Lamp1']
bedroom = ['Bedroom1', 'Bedroom2']
lamp = ['Lamp1']

#   local ip of your hue bridge

def getvarname(name):
    if name in globals():
        return globals()[name]
    if name in locals():
        return locals()[name]
    raise Exception("no room assignment found")

def lightstate(room, state):
    b = Bridge(snag(2))
    v = 255
    if state == 0:
        v = 0
    print(v)
    r = getvarname(room)
    b.connect()
    sleep(0.5)
    b.set_light(r, 'bri', v)