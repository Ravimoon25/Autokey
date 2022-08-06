import pyautogui as pg

pg.PAUSE = 2
pg.FAILSAFE = True

for i in range(0, 1000):
    pg.moveTo(1300, 100)
    pg.moveTo(1300, 200)
    pg.click()


