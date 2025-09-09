import subprocess
import time
import os
import signal

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

timed = int(input("View Time (sec): "))
url = input("Enter URL: ")
cycles = int(input("Views: "))

for i in range(cycles):
    proc = subprocess.Popen([chrome_path, "--incognito", url])
    time.sleep(timed)
    try:
        os.system("taskkill /im chrome.exe /f")
    except Exception:
        pass
    time.sleep(1)
