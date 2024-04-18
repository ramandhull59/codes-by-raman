import turtle
# speed , colour and the baCKGROUND COLOUR for the  drawing 
turtle.speed(0)
turtle.bgcolor("black")
colors = ["red"]

for i in range(360):
    turtle.pencolor(colors[0])  # Access the first element in the colors list
    turtle.width(i / 100 + 1)
    turtle.forward(i)
    turtle.left(59)
turtle.done()
