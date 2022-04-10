import turtle

win = turtle.Screen()
win.title("Pong")
win.bgcolor("blue")
win.setup(width=1920, height=1080)
win.tracer(0)

# keeping score
p1_score = 0
p2_score = 0

# add the paddle and ball
# paddle 1 modulename.classname
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("pink")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-900, 0)

# paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("pink")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(900, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("pink")
ball.penup()
ball.goto(0, 0)

# creating the scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 475)
scoreboard.write(f"Player A: {p1_score} Player B: {p2_score}", align="center", font=("Courier", 30, "normal"))

# ball movement
ball.dx = .5
ball.dy = -.5


# function
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
        y = paddle_1.ycor()
        y -= 20
        paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
        y = paddle_2.ycor()
        y -= 20
        paddle_2.sety(y)


# keyboard interaction
win.listen()
win.onkeypress(paddle_1_up, "w")
win.onkeypress(paddle_1_down, "s")
win.onkeypress(paddle_2_up, "Up")
win.onkeypress(paddle_2_down, "Down")

# game loop
while True:
    win.update()

    # moving the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # make sure ball doesn't leave board
    if ball.ycor() > 500:
        ball.sety(500)
        ball.dy *= -1

    if ball.ycor() < -500:
        ball.sety(-500)
        ball.dy *= -1

    if ball.xcor() > 950:
        ball.setx(0)
        ball.dx *= -1
        p1_score += 1
        # need to clear the scoreboard to not overlap the old one
        scoreboard.clear()
        scoreboard.write(f"Player A: {p1_score} Player B: {p2_score}", align="center", font=("Courier", 30, "normal"))

    if ball.xcor() < -950:
        ball.setx(0)
        ball.dx *= -1
        p2_score += 1
        scoreboard.clear()
        scoreboard.write(f"Player A: {p1_score} Player B: {p2_score}", align="center", font=("Courier", 30, "normal"))

    # paddle and ball collision
    if (ball.xcor() > 890 and ball.xcor() < 900) and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(890)
        ball.dx *= -1

    if (ball.xcor() < -890 and ball.xcor() > -900) and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-890)
        ball.dx *= -1




