import turtle #importing turtle module
window = turtle.Screen() # assigning turtle screen layer to window variable
window.bgcolor("blue") #applying blue colour to bacground
papi = turtle.Turtle() #in turtle there is another module called Turtle ,we are assigning that to variable papi
papi.shape("turtle") #we change shape of turtle
papi.color("black") #we change colour of turtle
papi.speed(2) #we change speed of turtle
papi.forward(100) #moving our Turtle forward with 100 steps
papi.right(90) # saying our turtle to turn 90 degrees
papi.forward(100)
papi.right(90)
papi.forward(100)
papi.right(90)
papi.forward(100)
papi.right(90)
window.exitonclick() #saying turtle window to close or exit if we click on it
