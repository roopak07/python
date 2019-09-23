from Tkinter import *
w = Tk()
T = Text(w, height = 4,width=20)
T.pack() #  pack means creating a layer on tkinter window ,if we remove pack we wont get any layer on tinkter window, if u change width and height with and without pack you will know about importance of pack
T.insert(END,"hi \n hellow") #insert means it creates a layer for text, if u remove END we will get error
mainloop()
 
