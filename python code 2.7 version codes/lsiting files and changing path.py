import os #importing os libraries
flist = os.listdir(r"C:\Users\roopak\Desktop\python\images_list") # listing files in the folder
print(flist) # printing files in the folder
cpath = os.getcwd() # geting the default directry path of python
print(cpath) # printing the path of python
path=os.chdir(r"C:\Users\roopak\Desktop\python\images_list") # changing the python path to our folder, to work on it
wpath=os.getcwd() # now getting the changed path i.e our path 
print(wpath) # printing the changed path
