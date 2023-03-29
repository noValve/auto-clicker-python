import pyautogui
from pynput.keyboard import *
import os

# ======= Settings =======
run_key = Key.f1
pause_key = Key.f2
exit_key = Key.f3
click_delay = 0.05 # delay between each click (in seconds)

# ======= Variables =======
running = False
amount_of_clicks = 0 

def menu_display():
    print("""
    ___         __        _________      __            
   /   | __  __/ /_____  / ____/ (_)____/ /_____  _____
  / /| |/ / / / __/ __ \/ /   / / / ___/ //_/ _ \/ ___/
 / ___ / /_/ / /_/ /_/ / /___/ / / /__/ ,< /  __/ /    
/_/  |_\__,_/\__/\____/\____/_/_/\___/_/|_|\___/_/       
""")
    print("made by @noValve")
    print("\nClick delay: " + str(click_delay))
    print("Controls:")
    print("\t- Run: " + str(run_key)[4:].upper())
    print("\t- Pause: " + str(pause_key)[4:].upper())
    print("\t- Exit: " + str(exit_key)[4:].upper())
    print("\nPress " + str(run_key)[4:].upper() + " to start...")

def on_key_press(key):
    """
    Performs an action depending on the pressed key.

    Args:
        key (Key): The pressed key.
    """
    global running, amount_of_clicks

    match key:
        case Key.f1:
            if not running and amount_of_clicks == 0:
                running = True
                print("[Started]")
            elif not running:
                running = True
                print("[Resumed]")

        case Key.f2:
            if running:
                running = False
                print("[Paused] (" + str(amount_of_clicks) + " clicks)")

        case Key.f3:
            running = False
            print("[Exited] (" + str(amount_of_clicks) + " clicks )")
            os._exit(0)

def main():
    global amount_of_clicks
    key_listener = Listener(on_press=on_key_press) 
    key_listener.start()

    menu_display()
    while True:
        if running:
            pyautogui.click(pyautogui.position())
            amount_of_clicks+=1
            pyautogui.PAUSE = click_delay

if __name__ == "__main__":
    main()

