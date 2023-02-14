import pyautogui as pg
import time


time.sleep(3)
for i in range(5):
    pg.write("hello world ")
    pg.press("enter")
    time.sleep(60)
