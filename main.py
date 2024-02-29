from pynput import keyboard
from time import sleep
from threading import Thread
from os import system
from pystyle import Colors

is_auto_running = False
keyController = keyboard.Controller()


def auto_press_r():
    global is_auto_running
    print(Colors.yellow, "Spaming R...\n")
    print(Colors.green, "Press -> (Right Arrow) Button to stop Spaming R\n")
    while is_auto_running:
        keyController.press("r")
        keyController.release("r")
        sleep(0.025)
    print(Colors.red, "Stopped Spaming!\n")
    print(Colors.green, "Press <- (Left Arrow) Button to start Spaming R\n")


def on_press(key):
    global is_auto_running
    if key == keyboard.Key.left and not is_auto_running:
        is_auto_running = True
        thread = Thread(target=auto_press_r)
        thread.start()
    elif key == keyboard.Key.right and is_auto_running:
        is_auto_running = False


def main():
    system("title " + "Fakekey2k")

    with keyboard.Listener(on_press=on_press) as listener:
        print(Colors.green, "Press <- (Left Arrow) Button to start Spaming R\n")
        listener.join()


if __name__ == "__main__":
    main()
