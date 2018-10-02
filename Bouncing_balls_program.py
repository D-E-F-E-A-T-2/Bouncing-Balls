# Bouncing balls simulation program

import turtle
import random
import time

def atLeftEdge(ball, screen_width):
    if ball.xcor() <= -screen_width/2: # -400 is ocordinate...remember it's divided in half, here xcor() returns x-coordination.
        return True
    else:
        ball.setheading(random.randint(30, 270))
        return False

def atRightEdge(ball, screen_width):
    if ball.xcor() >= screen_width/2:
        return True
    else:
        ball.setheading(random.randint(30, 300))
        return False

def atTopEdge(ball, screen_width):
    if ball.ycor() <= -screen_height/2:
        return True
    else:
        ball.setheading(random.randint(30, 70))
        return False

def atBottomEdge(ball, screen_width):
    if ball.ycor() >= screen_height/2:
        return True
    else:
        ball.setheading(random.randint(30, 170))
        return False

def bounceBall(ball, new_direction):
    if new_direction == 'left' or new_direction == 'right':
        new_heading = 180
    elif new_direction == 'top' or new_direction == 'down':
        new_heading = 180

    return new_heading

def createBalls(num_balls):
    balls = []
    colors = ['red', 'green', 'blue', 'black', 'white', 'grey', 'yellow', 'orange']
    speeds = [0, 1, 3, 6, 10]
    for k in range(0, num_balls):
        new_ball = turtle.Turtle()
        new_ball.shape('circle')
        new_ball.fillcolor(colors[random.randint(0, 7)])
        new_ball.speed(speeds[random.randint(0, 4)])
        new_ball.penup()
        new_ball.setheading(random.randint(1, 359)) # if 360 then it means go across wall.
        balls.append(new_ball)

    return balls
        
# ----main
#   Program greeting
print('This program stimulates bouncing balls in a turtle screen')
print('for a specified number of time')

# init screen size
screen_width = 800
screen_height = 800
turtle.setup(screen_width, screen_height)

# create turtle window
window = turtle.Screen()
window.title('Bouncing Balls')

# prompt user for time and number of balls
while True:
    try:
        num_seconds = int(input('Enter the number of seconds to run: '))
        num_balls = int(input('Enter number of balls in simulation: '))
        break
    except:
        print('Make sure to enter positive Integer only')

# create balls
balls = createBalls(num_balls)

# set start time
start_time = time.time()

#begin simulation
terminate = False

while not terminate:
    for k in range(0, len(balls)):
        balls[k].forward(30)

        if atLeftEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k], 'left'))
        elif atRightEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k], 'right'))
        elif atTopEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k], 'up'))
        elif atBottomEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k], 'down'))

    if time.time() - start_time > num_seconds:
        terminate = True

#exit on close window
turtle.exitonclick()
