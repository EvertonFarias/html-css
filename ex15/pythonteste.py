import turtle

# Configurar a janela e o cursor
window = turtle.Screen()
window.bgcolor("white")
spider = turtle.Turtle()

# Desenhar o Homem-Aranha
spider.speed(0)
spider.color("black", "red")
spider.begin_fill()
spider.circle(100)
spider.end_fill()
spider.penup()
spider.goto(-40, 50)
spider.pendown()
spider.color("white", "white")
spider.begin_fill()
spider.circle(30)
spider.end_fill()
spider.penup()
spider.goto(40, 50)
spider.pendown()
spider.begin_fill()
spider.circle(30)
spider.end_fill()
spider.penup()
spider.goto(-70, -80)
spider.pendown()
spider.color("black", "blue")
spider.begin_fill()
for i in range(2):
    spider.forward(50)
    spider.left(90)
    spider.forward(10)
    spider.left(90)
spider.end_fill()
spider.penup()
spider.goto(20, -80)
spider.pendown()
spider.begin_fill()
for i in range(2):
    spider.forward(50)
    spider.left(90)
    spider.forward(10)
    spider.left(90)
spider.end_fill()

# Esconder o cursor e manter a janela aberta
spider.hideturtle()
turtle.done()
