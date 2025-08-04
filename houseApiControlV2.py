from tkinter import *
from gpiozero import LED, Button as btnz
import requests
from signal import pause



class HomeApiControll:
    
    def updateDoor(self, state):
        if state == 1:
            msg = {"state":1}
            rep = requests.get('https://ftonye.pythonanywhere.com/updateFrontDoor',params=msg) 
            print(rep.text) 
            self.__doorLedOn.on()
            self.__doorLedOff.off()
            self.__lblStatus.config(text=rep.text)
            self.__doorOpen.config(bg='red') 
            self.__doorClose.config(bg='green') 
        else:
            msg = {"state":0}
            rep = requests.get('https://ftonye.pythonanywhere.com/updateFrontDoor',params=msg)  
            print(rep.text) 
            self.__doorLedOn.off()
            self.__doorLedOff.on()
            self.__lblStatus.config(text=rep.text)
            self.__doorOpen.config(bg='green')
            self.__doorClose.config(bg='red')
    
    def doorOn(self):
        msg = {"state":1}
        rep = requests.get('https://ftonye.pythonanywhere.com/updateFrontDoor',params=msg) 
        print(rep.text) 
        self.__doorLedOn.on()
        self.__doorLedOff.off()
        self.__lblStatus.config(text=rep.text)
        self.__doorOpen.config(bg='red') 
        self.__doorClose.config(bg='green') 

    def doorOff(self):
        msg = {"state":0}
        rep = requests.get('https://ftonye.pythonanywhere.com/updateFrontDoor',params=msg)  
        print(rep.text) 
        self.__doorLedOn.off()
        self.__doorLedOff.on()
        self.__lblStatus.config(text=rep.text)
        self.__doorOpen.config(bg='green')
        self.__doorClose.config(bg='red')


        
    
    def __init__(self,root:Tk):
        self.__root = root
        
        self.__doorOpen = Button(self.__root,text='Open Door',bg='green', command=lambda:self.updateDoor(1))
        self.__doorOpen.grid(row=0,column=0)
        
        self.__doorClose = Button(self.__root,text='Close Door',bg='green', command=lambda:self.updateDoor(0))
        self.__doorClose.grid(row=0,column=1)
        
        self.__lblStatus = Label(self.__root,text='La porte est ferme')
        self.__lblStatus.grid(row =1,column=0, columnspan= 2)
        
        self.__doorLedOn = LED(2)
        self.__doorLedOff = LED(3)

        self.__btnOn = btnz(4)
        self.__btnOn.when_pressed = self.doorOn
        
        self.__btnOff = btnz(17)
        self.__btnOff.when_pressed = self.doorOff
        
        self.__root.mainloop()
        
mainWindow = Tk()
GUI = HomeApiControll(mainWindow)
pause()
        