import turtle
import winsound

# Mark: Window

wn = turtle.Screen()
wn.title("Pong by AZ0iC")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Mark: Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0",
          align="center",
          font=("Courier", 24, "bold"))

# Mark: Score

score_a = 0
score_b = 0

# Mark: Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-320, 0)

# Mark: Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(320, 0)

# Mark: Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.3


# Mark: Function

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Mark: Keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Mark: Main game LOOP

while True:
    wn.update()

    # MARK:  Move the Ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Mark: Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
                  align="center",
                  font=("Courier", 24, "bold"))
        winsound.PlaySound("default", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
                  align="center",
                  font=("Courier", 24, "bold"))
        winsound.PlaySound("default", winsound.SND_ASYNC)

    # Mark: Paddles and Ball collisions

    if (ball.xcor() > 300 and ball.xcor() < 340) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(300)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -300 and ball.xcor() > -340) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-300)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)