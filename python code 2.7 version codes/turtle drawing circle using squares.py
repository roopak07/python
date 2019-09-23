import turtle #importing turtle module
window = turtle.Screen() # assigning turtle screen layer to window variable
window.bgcolor("blue") #applying blue colour to bacground
papi = turtle.Turtle() #in turtle there is another module called Turtle ,we are assigning that to variable papi
papi.shape("turtle")
papi.color("black")
for y in range (0,36):
    for x in range(0,4):
        papi.forward(100) #moving our Turtle forward with 100 steps
        papi.right(90) # saying our turtle to turn 90 degrees
    papi.right(10)
window.exitonclick() #saying turtle window to close or exit if we click on it

# if you clcik on the screen while drawing it will through an error (no need to worry with error) ,if we stay till the drawing complets we wont get any erro 
