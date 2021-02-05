import turtle
from random import choice, randint

window = turtle.Screen()
window.title("Ping-pong")
window.setup(width=1.0, height=1.0)
window.bgcolor("black")
window.tracer(2)

border = turtle.Turtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

border.goto(0, 300)
border.color('white')
border.setheading(270)
for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

# rocket_a
rocket_a = turtle.Turtle()
rocket_a.color('white')
rocket_a.shape('square')
rocket_a.shapesize(stretch_len=1, stretch_wid=5)
rocket_a.penup()
rocket_a.goto(-450, 0)


def move_up():
    y = rocket_a.ycor() + 50
    if y > 250:
        y = 250
    rocket_a.sety(y)


def move_down():
    y = rocket_a.ycor() - 50
    if y < -250:
        y = -250
    rocket_a.sety(y)


# rocket_b
rocket_b = turtle.Turtle()
rocket_b.color('white')
rocket_b.shape('square')
rocket_b.shapesize(stretch_len=1, stretch_wid=5)
rocket_b.penup()
rocket_b.goto(450, 0)

FONT = ("Arial", 30)
score_a = 0
s_1 = turtle.Turtle(visible=False)
s_1.color('white')
s_1.shape()
s_1.penup()
s_1.setposition(-250, 300)
s_1.write(score_a, font=FONT)

score_b = 0
s_2 = turtle.Turtle(visible=False)
s_2.color('white')
s_2.shape()
s_2.penup()
s_2.setposition(250, 300)
s_2.write(score_b, font=FONT)


def move_up_2():
    y = rocket_b.ycor() + 10
    if y > 250:
        y = 250
    rocket_b.sety(y)


def move_down_2():
    y = rocket_b.ycor() - 10
    if y < -250:
        y = -250
    rocket_b.sety(y)


window.listen()
window.onkeypress(move_up, 'w')
window.onkeypress(move_down, 's')
window.onkeypress(move_up_2, 'Up')
window.onkeypress(move_down_2, 'Down')

ball = turtle.Turtle()
ball.penup()
ball.color('red')
ball.shape('circle')
ball.speed(0)
ball.dx = 3
ball.dy = -3

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() >= 490:
        score_b += 1
        s_2.clear()
        s_2.write(score_b, font=FONT)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if ball.xcor() <= -490:
        score_a += 1
        s_1.clear()
        s_1.write(score_a, font=FONT)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if ball.ycor() >= rocket_b.ycor() - 50 and ball.ycor() <= rocket_b.ycor() + 50 \
            and ball.xcor() >= rocket_b.xcor() - 5 and ball.xcor() <= rocket_b.xcor() + 5:
        ball.dx = -ball.dx

    if ball.ycor() >= rocket_a.ycor() - 50 and ball.ycor() <= rocket_a.ycor() + 50 \
            and ball.xcor() >= rocket_a.xcor() - 5 and ball.xcor() <= rocket_a.xcor() + 5:
        ball.dx = -ball.dx

window.mainloop()
