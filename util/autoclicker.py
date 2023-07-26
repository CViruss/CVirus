import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

def on_press(key):
    global toggle_key
    try:
        if key == toggle_key:
            toggle_clicker()
    except AttributeError:
        pass

def toggle_clicker():
    global clicking
    clicking = not clicking

def autoclicker():
    mouse = Controller()
    while True:
        while clicking:
            mouse.click(selected_button)
            time.sleep(0.1)

if __name__ == "__main__":
    clicking = False
    toggle_key = KeyCode(char=input("Choose a key to toggle autoclicking: "))
    mouse_buttons = {
        1: Button.left,
        2: Button.right
    }
    print("Choose a mouse button:")
    for key, value in mouse_buttons.items():
        print(f"{key}. {value}")
    choice = int(input())
    selected_button = mouse_buttons.get(choice)
    with Listener(on_press=on_press) as listener:
        autoclicker()
