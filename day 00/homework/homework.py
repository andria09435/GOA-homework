from turtle import  *

#we want to paint a house

#step 1: draw a spuare


width(7)
color("purple")


forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of spuare

#drawing a door


begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)  # height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()


begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#draw a window
left(80)
color("white")
forward(40)
color("blue")
begin_fill()
left(40)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()


penup()
goto(140, 140)
begin_fill()
color("blue")
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()


exitonclick()
