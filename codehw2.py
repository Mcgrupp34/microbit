#Using the ambient light sensor to select a bank of notes for the Room Music Bot
#This uses the ambient light level of the room the room music bot is in to select a distinct
#bank of notes to build music music from the dimensional measurements of the room
from microbit import *

while True:
    #reading light level into a variable from pin0
    light = pin0.read_analog()
    #reporting for debugging
    print(light)

    #logic for note selection, when light level is read, one of three vectors of notes is selected for
    #room bot to choose notes from. Note, maximum value of reading from the ambient light sensor is 1023,
    #which has been divided into 3, for three banks of possible notes.
    if (light <= 341):
        pos_notes = ['X']
    elif (341 <= light <=682):
        pos_notes = ['Y']
    else:
        pos_notes = ['Z']

    #reporting to make sure it works
    print(pos_notes)
    sleep(1000)

#next steps are to add this into the already working code for the basic functionality of the room music bot.

