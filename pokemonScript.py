from keyModule import PressKey, ReleaseKey
import time 
import keyboard
import random
from runPokeScript import pressSpeed, pressDuration

pressSpeed = 0.008 #0.01
pressDuration = 0.018
speedKey = 0x5A #Z key

moveset = ['w','d','s','a']
aButton = 'q'
bButton = 'e'
startButton = 'r'
all_actions = moveset + [aButton,bButton,startButton]
action_dict = {'w':0x57,'s':0x53,'a':0x41,'d':0x44,'q':0x51,'e':0x45,'r':0x52}
expl_dict = {'w':'UP','s':'DOWN','a':'LEFT','d':'RIGHT','q':'BUTTONA',
                'e':'BUTTON B','r':'START'}

#action weights
weightMove = 0.60
weightA = weightMove + 0.35
weightB = weightA + 0.09
weightStart = 1

def uniform_action_run():
    print("Actions currently randomly chosen")
    pressCounter = 0
    while True:
        pressCounter += 1
        if pressCounter%100==0:
            print("Count: {}".format(pressCounter),end='\r')
        try:
            if keyboard.is_pressed('esc'):
                print("Stopping script")
                break
        except:
            pass
        time.sleep(pressSpeed)
        move = random.choice(all_actions)
        key = action_dict[move]
        PressKey(key)
        time.sleep(pressDuration)
        ReleaseKey(key)

def weighted_action_run():
    print("Actions currently with weight distribution")
    pressCounter = 0
    while True:
        pressCounter += 1
        if pressCounter%100==0:
            print("Count: {}".format(pressCounter),end='\r')
        try:
            if keyboard.is_pressed('esc'):
                print("Count: {}".format(pressCounter))
                print("Stopping script")
                break
        except:
            pass
        time.sleep(pressSpeed)
        p = random.random()
        if p < weightMove: move = random.choice(moveset)
        elif p<weightA: move = aButton
        elif p<weightB: move = bButton
        else: move = startButton
        key = action_dict[move]
        PressKey(key)
        time.sleep(pressDuration)
        ReleaseKey(key)

def circles(n=10,s=pressSpeed,d=pressDuration):
    for i in range(n):
        for a in moveset:
            time.sleep(s)
            key = action_dict[a]
            PressKey(key)
            time.sleep(d)
            ReleaseKey(key)

