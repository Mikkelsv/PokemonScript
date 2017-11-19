from pokemonScript import *
import keyboard
import time

pressSpeed = 0.01  # Time between actions
pressDuration = 0.03  # Duration of key pressed down

if __name__ == "__main__":
    print("Waiting for esc",end='\r')
    keyboard.wait('esc')
    print("Acid Ash Adventure")
    time.sleep(1)
    weighted_action_run()
