import time
import threading
import pyautogui
import keyboard

# Global variable to control the auto clicker loop
auto_clicking = False

def auto_clicker(interval):
    global auto_clicking
    while auto_clicking:
        pyautogui.click()
        time.sleep(interval)

def initiate_auto_clicker(interval):
    global auto_clicking
    if not auto_clicking:
        auto_clicking = True
        print("Starting auto clicker...")
        time.sleep(2)
        click_thread = threading.Thread(target=auto_clicker, args=(interval,))
        click_thread.start()

def stop_auto_clicker():
    global auto_clicking
    if auto_clicking:
        auto_clicking = False
        print("Stopping auto clicker...")

def main():
    interval = float(input("Enter the interval between clicks (in seconds): "))
    
    # Register key listeners
    keyboard.add_hotkey('i', initiate_auto_clicker, args=(interval,))
    keyboard.add_hotkey('p', stop_auto_clicker)

    print("Press 'I' to initiate auto clicker and 'P' to stop auto clicker.")
    keyboard.wait('esc')  # Wait for the 'esc' key to exit

if __name__ == "__main__":
    main()
