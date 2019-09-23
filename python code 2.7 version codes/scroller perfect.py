from Tkinter import *
w = Tk()
s = Scrollbar(w) #defining scroll bar for "w"
T = Text(w, height = 4,width=20)
T.pack(side=RIGHT, fill=Y) # text layer will move to right side, if we want to change it to left then make it LEFT
s.pack(side=LEFT, fill=Y) # creats a scroll layer on LEFT side
s.config(command=T.yview)
T.config(yscrollcommand=s.set) # it will set to position where we relese scroller ,it wont go back
matter = """ A novel attendance system for members
of the industry using NFC (Near Field Communication) is proposed.
This work uses NFC readers to read the NFC cards. The system was built
using Arduinouno. ATMEGA328 microcontroller is heart of entire system for
which PN532 (NFC module) is interfaced and then a buzzer sound is given
uniquely to differentiate the cards and 16x2 LCD is
also interfaced for the purpose of display. """
T.insert(END,matter) 
mainloop()
