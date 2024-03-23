import pywin 
import win32gui 
import win32api




def getlist():
    thelist = []
    def findit(hwnd,ctx):
        if win32gui.GetWindowText(hwnd) == "Runelite": # check the title
            thelist.append(hwnd)

    win32gui.EnumWindows(findit,None)
    return thelist

b = getlist()
print(b) # b is the list of hwnd,contains those windows title is "Windows PowerShell"