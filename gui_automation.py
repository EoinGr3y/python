import pyautogui

print(pyautogui.size())
print(pyautogui.position())
width, height = pyautogui.size()
pyautogui.moveTo(10, 10, duration=1)
pyautogui.moveRel(200, 200, duration=10)
pyautogui.click(435, 37)