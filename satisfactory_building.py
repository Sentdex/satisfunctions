import pyautogui
import time
import getkeys

KEY_FOR_BUILD = "E"

print("Starting in...")
for i in reversed(range(4)):
    print(i)
    time.sleep(1)

while True:
    keys = getkeys.key_check()
    if KEY_FOR_BUILD in keys:
        pyautogui.click()
