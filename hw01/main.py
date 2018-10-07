
from turtle import *

penup()
left(180)
forward(700)
right(90)
forward(395)
right(180)
pendown()


color("red")
begin_fill()

forward(780)
left(90)
forward(1300)
left(90)
forward(780)
left(90)
forward(1300)
left(90)
forward(780)

end_fill()

penup()
left(180)
forward(620)
right(90)
forward(85)
pendown()


color("yellow")
begin_fill()
for x in range(1,6):
    forward(200)
    right(144)
end_fill()


penup()
forward(300)
left(90)
forward(60)
pendown()

color("yellow")
begin_fill()
for x in range(1,6):
    forward(80)
    right(144)
end_fill()


penup()
left(180)
forward(80)
left(90)
forward(40)
pendown()

color("yellow")
begin_fill()
for x in range(1,6):
    forward(80)
    right(144)
end_fill()


penup()
right(90)
forward(120)
pendown()

color("yellow")
begin_fill()
for x in range(1,6):
    forward(80)
    right(144)
end_fill()


penup()
right(45)
forward(150)
pendown()

color("yellow")
begin_fill()
for x in range(1,6):
    forward(80)
    right(144)
end_fill()


 

done()
