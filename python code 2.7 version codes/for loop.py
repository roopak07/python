import os
a=os.listdir(r"C:\Users\roopak\Desktop\python\images_list")
print(a)
for b in a: #b is variable ,every single value or file in "a" is assigned to b and compared
    print(b)

for x in (0,10,20): #here we didnt mentioned range so it takes 0,10 and 20 as numbers 
    print ("x=%d"%(x))

for x in range(0,10): #here we mentioned rane so it takes all values between 0 and 10 ,including 0 and 10
    print(x)
input()
  
