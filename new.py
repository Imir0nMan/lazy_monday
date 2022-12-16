import os
import keyboard
import time

os.system("start cmd")

class Key():
    namespace = ''
    delay=0
    def __init__(self, name, delay):   
        self.namespace = name
        self.delay=delay

class AltKey():
    namespace = ''
    delay=0
    #0=press and release 1=just press 2=release
    pressType=0
    def __init__(self, name,presstype,delay):   
        self.namespace = name
        self.pressType = presstype
        self.delay=delay

keys = [Key("start chrome /incognito facebook.com",1),AltKey("enter",0,0.1),Key("ashot_gasparyan_2002@mail.ru",2),AltKey("tab",0,0.1),Key("mam1975pap1977",0.1),AltKey("enter",0,0.1),AltKey("enter",0,2),AltKey("tab",10,5),AltKey("enter",0,0.2),AltKey("tab",4,0),AltKey("enter",0,0.5),Key("Ashot Gasparyan",1)]

def main():
    for key in keys:
        time.sleep(key.delay)
        if type(key) is Key:
            keyboard.write(key.namespace)
        elif key.pressType==0 :
            keyboard.press_and_release(key.namespace)
        elif key.pressType==1 :
            keyboard.press(key.namespace)
        elif key.pressType==2:
            keyboard.release(key.namespace)
        elif key.pressType>2:
            for element in range(key.pressType):
                keyboard.press_and_release(key.namespace)
# keyboard.press("win")
# keyboard.press_and_release("r")
# keyboard.release("win")
#keyboard.press("enter")


main()