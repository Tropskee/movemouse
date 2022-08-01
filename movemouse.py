import pyautogui
import time


def movemouse():
    pyautogui.moveRel(10, 0, duration=0.1)
    pyautogui.moveRel(0, -10, duration=0.1)
    pyautogui.moveRel(-10, 0, duration=0.1)
    pyautogui.moveRel(0, 10, duration=0.1)


if __name__ == '__main__':
    count = 0
    minutes = 5
    while True:
        print('\r', minutes*60 - count, 'seconds left before moving mouse',
              end='', flush=True)
        if count >= minutes*60:
            movemouse()
            pyautogui.press('shift')
            count = 0
        else:
            time.sleep(1)
            count += 1
