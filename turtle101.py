"""Draw a circle


"""

import turtle
from freegames import vector

t = turtle.Turtle() 


def line(start, end):
    "Draw line from start to end."
    t.up()
    t.goto(start.x, start.y)
    t.down()
    t.goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    t.up()
    t.goto(start.x, start.y)
    t.down()
    t.begin_fill()

    for count in range(4):
        t.forward(end.x - start.x)
        t.left(90)

    t.end_fill()

def circle(start, end):
    "Draw circle from start to end."
    t.up()
    t.goto(start.x, start.y)
    t.down()
    dist = abs(start-end)
    #print(dist)
    t.circle(dist)
    t.up()
    t.goto(end.x, end.y)
       
    
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
t.screen.setup(420, 420, 370, 0)
t.screen.onscreenclick(tap)
t.screen.listen()
t.screen.onkey(t.undo, 'u')
t.screen.onkey(lambda: color('black'), 'K')
t.screen.onkey(lambda: color('white'), 'W')
t.screen.onkey(lambda: color('green'), 'G')
t.screen.onkey(lambda: color('blue'), 'B')
t.screen.onkey(lambda: color('red'), 'R')
t.screen.onkey(lambda: store('shape', line), 'l')
t.screen.onkey(lambda: store('shape', square), 's')
t.screen.onkey(lambda: store('shape', circle), 'c')
t.screen.mainloop()