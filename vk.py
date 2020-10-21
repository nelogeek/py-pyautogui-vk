import pyautogui
import time
#for i in range(10):
#   xm, ym = pyautogui.position()
#   print(xm, ym)
#   time.sleep(1)

pyautogui.moveTo(178, 767)
pyautogui.hotkey('win','r')
time.sleep(2)
pyautogui.typewrite(r"C:\Users\iell\AppData\Local\Yandex\YandexBrowser\Application\browser.exe")
pyautogui.hotkey('enter')
time.sleep(2)
pyautogui.hotkey('win', 'up')
pyautogui.hotkey('ctrl', 't')
pyautogui.click(x=568, y=56, button='left')
pyautogui.typewrite(r"https://vk.com/im")
pyautogui.hotkey('enter')