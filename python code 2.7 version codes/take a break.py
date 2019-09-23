import webbrowser #module for 
import time # module for time.sleep
import datetime # module for datetime.datetime.now()

breaks_count=0
no_of_breaks=4
print("Program is started on:")
print(datetime.datetime.now())  # we can also have single code for this two lines as : print("this program is started on:"+str(datetime.datetime.now()))
while(breaks_count<no_of_breaks):
    time.sleep(2) # 60*60*2 = 2 hours
    breaks_count=breaks_count+1
    print("break: "+str(breaks_count))
    print("break time:"+str(datetime.datetime.now())) 
    #print("break count:")
    #print(count)
    webbrowser.open('https://www.youtube.com/watch?v=V6ZYZmw4MI0')
    
