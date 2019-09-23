import turtle
window = turtle.Screen()
window.bgcolor("pink")

a = turtle.Turtle() 
a.color("white")
a.shape("turtle")
a.circle(100) # circle with 100 radius

b=turtle.Turtle()
b.color("blue")
b.shape("circle")
b.speed(1)
b.forward(100)
b.right(90)
b.forward(100)
b.right(90)
b.forward(100)
b.right(90)
b.forward(100)
b.right(90)
window.exitonclick()
