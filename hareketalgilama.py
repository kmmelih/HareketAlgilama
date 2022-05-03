import cv2
import numpy as np
import win32gui
from PIL import ImageGrab, Image

screen_grab = 0
winName = input("Pencere adını girin:")
#1024x768 uygulama çözünürlüğü


def capture_dynamic():
    toplist, winlist = [], []
    
    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
        
    win32gui.EnumWindows(enum_cb, toplist)

    wnd = [(hwnd, title) for hwnd, title in winlist if winName in title.lower()]

    if wnd:
        wnd = wnd[0]
        hwnd = wnd[0]

        bbox = win32gui.GetWindowRect(hwnd)
        img = ImageGrab.grab(bbox)
        global tempScreen
        tempScreen = screen_grab
        return img
    else:
        return None


while(True):   
    screen_grab =  capture_dynamic()
    
    if(screen_grab == None):
        print("No Window Found! Please Try Again")
        break
    
    screen_grab = np.array(screen_grab)
    diff = cv2.absdiff(tempScreen,screen_grab)
    cv2.imshow('window',cv2.cvtColor(diff, cv2.COLOR_BGR2RGB))
    cv2.resizeWindow("window", 600, 500) 
    cv2.moveWindow("window", 1024, 0)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break