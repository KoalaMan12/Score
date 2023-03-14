import turtle

# Create the first turtle and set its properties
turtle1 = turtle.Turtle()
turtle1.color("red")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-100, 0)

# Create the second turtle and set its properties
turtle2 = turtle.Turtle()
turtle2.color("green")
turtle2.shape("turtle")
turtle2.penup()

# Create the third turtle and set its properties
turtle3 = turtle.Turtle()
turtle3.color("blue")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(100, 0)

# Make the turtles move forward a bit
turtle1.forward(50)
turtle2.forward(50)
turtle3.forward(50)

turtle.done()
