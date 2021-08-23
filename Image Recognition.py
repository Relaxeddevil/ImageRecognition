import time
import keyboard
import win32api
import win32con
import sys
import pyautogui

from PIL import ImageGrab
from functools import partial

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


def click(x, y):  # click function
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.01)


def target():
    # region=(480, 180, 950, 450)
    Target = pyautogui.locateOnScreen("Target.png", region=(480, 180, 950, 450), grayscale=True, confidence=0.7)
    Target_center = pyautogui.center(Target)

    return Target_center


keyboard.wait("F4")

while keyboard.is_pressed("Esc") == False:

    if pyautogui.locateOnScreen("Target.png", region=(480, 180, 950, 450), grayscale=True, confidence=0.7) is not None:

        """#pyautogui.moveTo(target().x - 1920, target().y)

        mouse_pos = pyautogui.position()
        mouse_posx = mouse_pos[0]
        mouse_posy = mouse_pos[1]
        #click(mouse_posx, mouse_posy)"""

        click(target().x - 1920, target().y)
        # pyautogui.click(target().x - 1920, target().y)

    """ area1 = pyautogui.screenshot(region=(480, 223, 850, 350))
    # r == 149
    area2 = pyautogui.screenshot(region=(658, 336, 602, 423))
    # r == 255
    width, height = area2.size

    for x in range(0, width, 2):
        for y in range(0, height, 2):

            r, g, b = area2.getpixel((x, y))

            if r == 255:
                click(x + 658 - 1920, y + 336)

                time.sleep(1)

                break

            if keyboard.is_pressed("Esc"):
                sys.exit()"""

sys.exit()
