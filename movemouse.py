import pyautogui
import time


def movemouse():
    pyautogui.moveRel(10, -10, duration=0.25)
    pyautogui.moveRel(-10, 10, duration=0.25)


if __name__ == '__main__':
    i = True
    count = 0
    minutes = 5
    while i:
        print('\r', minutes*60 - count, 'seconds left before moving mouse',
              end='', flush=True)
        if count >= minutes*60:
            movemouse()
            count = 0
        else:
            time.sleep(1)
            count += 1
