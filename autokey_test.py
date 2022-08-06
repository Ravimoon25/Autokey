#import package
import pyautogui as pg

#Add variables for pause gap and failsafe
pg.PAUSE = 2
pg.FAILSAFE = True

#Loop for 1000 times
for i in range(0, 1000):
    pg.moveTo(1300, 100)
    pg.moveTo(1300, 200)
    pg.click()

print("Done")

