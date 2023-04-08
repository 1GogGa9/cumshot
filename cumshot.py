import pyautogui
import tkinter 
from tkinter import filedialog
import datetime
from datetime import datetime
x = datetime.now()

randomname = x.strftime("%f")
def path():

    directory = filedialog.askdirectory()
    return directory

def cumshot():
   myScreenshot = pyautogui.screenshot(f"{randomname}.jpg")
   myScreenshot.save(f"{path()}/{randomname}.jpg")

root = tkinter.Tk()
root.withdraw() 


cumshot()
print ()

