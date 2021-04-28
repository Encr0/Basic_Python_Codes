from turtle import Turtle, Screen

def draw_square(some_turtle):
    for _ in range(4):
        some_turtle.forward(200)
        some_turtle.right(90)
#definimos
def draw_art():
    webos = Turtle(shape="turtle") #me disculpo por las definiciones, estaba aburrido 
    webos.color("red")
    webos.pensize(2)
    webos.speed(45)
    for _ in range(36):
        draw_square(webos)
        webos.right(10)
    #otro mas para las lineas que entran
    meci = Turtle(shape="turtle") # jajaja meci, me disculpo xdd
    meci.color("white")
    meci.pensize(2)
    meci.speed(50)
    size = 1
    for _ in range(198):
        meci.forward(size)
        meci.right(300)
        size += 1

window = Screen()
window.bgcolor("black")

draw_art()

window.exitonclick()
