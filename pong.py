import turtle

# Set up the screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

# Create the left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# Create the right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# Create the ball
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("black")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Create the score board
left_player = 0
right_player = 0
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Left Player: 0 Right Player: 0",
            align="center", font=("Courier", 24, "normal"))

# Functions to move the paddles vertically


def paddleaup():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)


def paddleadown():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)


def paddlebup():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)


def paddlebdown():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)

# Function to restart the game


def restart_game():
    global left_player, right_player
    left_player = 0
    right_player = 0
    score.clear()
    score.write("Left Player: 0 Right Player: 0",
                align="center", font=("Courier", 24, "normal"))
    hit_ball.goto(0, 0)
    hit_ball.dx = 5
    hit_ball.dy = -5

# Function to exit the game


def exit_game():
    sc.bye()


# Keyboard input bindings
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")
sc.onkeypress(restart_game, "r")  # Bind "r" key to restart_game function
sc.onkeypress(exit_game, "q")  # Bind "q" key to exit_game function

# Main game loop
while True:
    sc.update()

    # Move the ball
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Border checking
    if hit_ball.ycor() > 290:
        hit_ball.sety(290)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -290:
        hit_ball.sety(-290)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 390:
        hit_ball.goto(0, 0)
        hit_ball.dx *= -1
        left_player += 1
        score.clear()
        score.write("Left Player: {} Right Player: {}".format(
            left_player, right_player), align="center", font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -390:
        hit_ball.goto(0, 0)
        hit_ball.dx *= -1
        right_player += 1
        score.clear()
        score.write("Left Player: {} Right Player: {}".format(
            left_player, right_player), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (hit_ball.dx > 0) and (350 < hit_ball.xcor() < 360) and (right_pad.ycor() + 50 > hit_ball.ycor() > right_pad.ycor() - 50):
        hit_ball.setx(340)
        hit_ball.dx *= -1
        right_player += 1
        score.clear()
        score.write("Left Player: {} Right Player: {}".format(
            left_player, right_player), align="center", font=("Courier", 24, "normal"))

    if (hit_ball.dx < 0) and (-360 < hit_ball.xcor() < -350) and (left_pad.ycor() + 50 > hit_ball.ycor() > left_pad.ycor() - 50):
        hit_ball.setx(-340)
        hit_ball.dx *= -1
        left_player += 1
        score.clear()
        score.write("Left Player: {} Right Player: {}".format(
            left_player, right_player), align="center", font=("Courier", 24, "normal"))

    # Check if either player has won
    if left_player >= 21 and left_player - right_player >= 2:
        score.clear()
        score.write("Left Player wins!", align="center",
                    font=("Courier", 24, "normal"))
        hit_ball.hideturtle()
        hit_ball.dx = 0
        hit_ball.dy = 0

    if right_player >= 21 and right_player - left_player >= 2:
        score.clear()
        score.write("Right Player wins!", align="center",
                    font=("Courier", 24, "normal"))
        hit_ball.hideturtle()
        hit_ball.dx = 0
        hit_ball.dy = 0

turtle.done()
