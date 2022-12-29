import turtle
import time

scr = turtle.Screen()
scr.title("PONG!")
scr.bgcolor("black")
scr.setup(width = 1000, height = 600)

paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=6,stretch_len =2)
paddle_left.penup()
paddle_left.goto(-400,0)

paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=6,stretch_len =2)
paddle_right.penup()
paddle_right.goto(400,0)

ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 5
ball.dy = -5

lscore = 0
rscore = 0

tally = turtle.Turtle()
tally.speed(0)
tally.color("white")
tally.penup()
tally.hideturtle()
tally.goto(0,260)
tally.write("P1 : 0  P2 : 0",align = "center", font = ("Courier", 24, "normal"))

# Functions to move paddle vertically
def paddleaup():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)
 
 
def paddleadown():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)
 
 
def paddlebup():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)
 
 
def paddlebdown():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)
 
scr.listen()
scr.onkeypress(paddleaup, "e")
scr.onkeypress(paddleadown, "x")
scr.onkeypress(paddlebup, "Up")
scr.onkeypress(paddlebdown, "Down")

while True:
    scr.update()
    
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
 
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        
    if  ball.xcor() > 500: #if ball gone past paddle add point
        ball.goto(0, 0)
        ball.dy *= -1
        lscore += 1
        tally.clear()
        tally.write("P1 : {}    P2: {}".format(lscore, rscore), align="center",font=("Courier", 24, "normal"))
        
    if  ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        rscore += 1
        tally.clear()
        tally.write("P1 : {}    P2: {}".format(lscore, rscore), align="center",font=("Courier", 24, "normal"))
        
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < paddle_right.ycor()+40 and ball.ycor() > paddle_right.ycor()-40):
        ball.setx(360)
        ball.dx*=-1
        
    if (ball.xcor() < -360 and ball.xcor()>-370) and (ball.ycor() < paddle_left.ycor()+40 and ball.ycor() > paddle_left.ycor()-40):
        ball.setx(-360)
        ball.dx*=-1

