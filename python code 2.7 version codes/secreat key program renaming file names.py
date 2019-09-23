import os #importing os libraries

file_folder=os.listdir(r"C:\Users\roopak\Desktop\python\images_list") # listing files in folder
print(file_folder) #printing file names
default_path=os.getcwd() # assigning default os file path to a variable default_path 
print("default path "+default_path) #printing the path of python
os.chdir(r"C:\Users\roopak\Desktop\python\images_list") #changing path to our folder
Cpath=os.getcwd() # assigning path to a varable Cpath
print("current path" +Cpath) #printing path

for file_name in file_folder: #file_name is a variable 
    Cfile_name=file_name.translate(None,"0123456789") #changing file name and assigning that to a variable Cfile ,
    #here we dont have table so we use None in translate(table,"letters or numbers or any varable to delet")
    print(Cfile_name) #printing modified file
    os.rename(file_name,Cfile_name) #os.rename(old file, new file)
# here we are assigning modified file name to old file name in folder or directry
