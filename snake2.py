"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
import random
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
color = random.choice(['green','blue','yellow'])
sp = 100

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    """
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    """

    if head.x < -200:
        head.x = 200
    if head.x > 200:
        head.x = -200
    if head.y < -200:
        head.y = 200
    if head.y > 200:
        head.y = -200
    
    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        global sp
        sp -= 10
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10
    else:
        snake.pop(0)


    clear()

    for body in snake:
        square(body.x, body.y, 9, color)

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, sp)

def movefood():
     #food.x = randrange(-15, 15) 
    #food.y = randrange(-15, 15) 
    i = random. randint(1,4)
    if i==1:
        food.x += 10
    elif i == 2:
        food.x -= 10
    elif i == 3:
        food.y -= 10
    else:
        food.y += 10
    ontimer(movefood, 1000)

setup(420, 420, 0, 0)
hideturtle()
tracer(False)
listen()



onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10 ), 'Down')
move()
movefood()
done()