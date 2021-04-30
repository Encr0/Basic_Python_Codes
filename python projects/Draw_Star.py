import turtle

t = turtle

lenght=100
size=400

colors = ['red','magenta','orange', 'yellow','green','blue','white']

turtle.speed(0)
turtle.pensize(50)

for i in colors:
    size-=50
    turtle.penup()
    turtle.goto(-size/2,size/10)
    turtle.pendown()
    turtle.color(i)
    turtle.begin_fill()

    for j in range(5):
        turtle.fd(size)
        turtle.rt(144)
    turtle.end_fill()

turtle.mainloop()
