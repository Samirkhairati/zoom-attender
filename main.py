import subprocess
import pyautogui
import time
from datetime import datetime

schedule = [
    ['1,s,0800,0845\n', '1,,,\n', '1,,,\n', '1,,,\n', '1,,,\n', '1,,,\n'],
    ['2,,,\n', '2,,,\n', '2,,,\n', '2,,,\n', '2,,,\n', '2,,,\n'],
    ['3,,,\n', '3,,,\n', '3,,,\n', '3,,,\n', '3,,,\n', '3,,,\n'],
    ['4,c,0742,0810\n', '4,m,0812,0905\n', '4,s,0910,1010\n', '4,c,1012,1110\n', '4,m,1120,1205\n', '4,p,1220,1310\n'],
    ['5,c,0742,0810\n', '5,e,0812,0905\n', '5,s,0910,1010\n', '5,p,1012,1110\n', '5,m,1120,1205\n', '5,c,1220,1310']
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
        

