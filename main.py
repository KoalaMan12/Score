import turtle

turtle.hideturtle()
turtle.color("White")
turtle.screensize(bg="black")

score = (1)

# write text
turtle.write(score)

while True:

  if input() == ("h"):
    score+=(1)
  
  turtle.clear()
  turtle.write(score)