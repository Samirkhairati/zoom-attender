import subprocess
import pyautogui
import time
from datetime import datetime

schedule = [
    ['1,s,0800,0845\n', '1,,,\n', '1,,,\n', '1,,,\n', '1,,,\n', '1,,,\n'],
    ['2,,,\n', '2,,,\n', '2,,,\n', '2,,,\n', '2,,,\n', '2,,,\n'],
    ['3,s,1115,1117\n', '3,p,1119,1121\n', '3,c,1123,1125\n', '3,m,1127,1129\n', '3,e,1131,1133\n', '3,s,1135,1137\n'],
    ['4,,,\n', '4,,,\n', '4,,,\n', '4,,,\n', '4,,,\n', '4,,,\n'],
    ['5,,,\n', '5,,,\n', '5,,,\n', '5,,,\n', '5,,,\n', '5,,,']
]

day = int(datetime.now().strftime('%w'))
daily = [ i.strip('\n').split(',') for i in schedule[day-1] ]
classesDone = 0

def subject(sub):
    btn = pyautogui.locateCenterOnScreen('img/'+sub+'.png')
    pyautogui.moveTo(btn)
    pyautogui.click()

while True:
    now = datetime.now().strftime("%H") + datetime.now().strftime("%M")
    time.sleep(1)
    print(now)
    currentClass = daily[classesDone]
    print(currentClass,',',classesDone)
    if now == currentClass[2]:   # login time
        subprocess.call(["C:\Program Files\Google\Chrome\Application\chrome.exe"])
        time.sleep(20)
        subject(currentClass[1])
        time.sleep(20)
        subprocess.call(["taskkill","/IM","chrome.exe"])
        time.sleep(30)
    if now == currentClass[3]:  # logout time
        subprocess.call(["taskkill","/IM","zoom.exe"])
        time.sleep(60)
        classesDone+=1
    if classesDone==6: break   # day over
        

