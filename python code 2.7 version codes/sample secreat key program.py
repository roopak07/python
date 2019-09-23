
import os

file_list=os.listdir(r"C:\Users\roopak\Desktop\python\images_list")
print(file_list)
cwd=os.getcwd()
print(cwd)

for file_name in file_list:
    Rfile=file_name.translate(None,"0123456789") #here we are storing modified name in other variable ,but we need assign changes to the particular files
    print(Rfile)
    #in this program we are working with file ,not in directry
    #so we can modify file names temperarly but cant see changes in folder,
    #so we need to work with directry 
