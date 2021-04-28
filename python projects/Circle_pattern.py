import turtle

turtle.bgcolor("black")
turtle.pensize(3)
turtle.speed(0)

b=["white","red","cyan","magenta"] #u can change colors btw / puedes cambiar los colores si quieres (nombres de colores en ingles)
for i in range(15):
    for a in b:
        turtle.color(a)
        turtle.circle(100)
        turtle.left(50)

turtle.mainloop()
