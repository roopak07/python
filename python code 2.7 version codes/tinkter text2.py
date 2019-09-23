from Tkinter import *
w = Tk()
T = Text(w, height = 4,width=20)
T.pack() #  pack means creating a layer on tkinter window ,if we remove pack we wont get any layer on tinkter window, if u change width and height with and without pack you will know about importance of pack
matter = """ A novel attendance system for members of the industry using NFC (Near Field Communication) is proposed. This work uses NFC readers to read the NFC cards. The system was built using Arduinouno. ATMEGA328 microcontroller is heart of entire system for which PN532 (NFC module) is interfaced and then a buzzer sound is given uniquely to differentiate the cards and 16x2 LCD is
also interfaced for the purpose of display. """ # here we are creating a box called matter in which are we are inserting some large text which cant be displayed, we are using """ to avoid content break ,if we use singe " if press enter in the middle of the content then will get an erro 
T.insert(END,matter) #insert means it creates a layer for text, if u remove END we will get error, here the box in the matter is placed on insert layer
mainloop()
 
