import turtle
def moving_object(self): # Is move the self?
    self.fillcolor("orange")
    self.color("orange")  # stroke/line color
    self.begin_fill()
    self.circle(20)
    self.end_fill()

def line(step):
    startx, starty = move.pos()
    for i in range(2000):
        move.clear()
        startx += step
        starty += step
        moving_object(move)
        move.goto(startx, starty)
        screen.update()  # Updates the canvas when live trace is off

if __name__ == "__main__": # What is this again?
    screen = turtle.Screen()
    screen.setup(600,600)
    screen.bgcolor("green")
    screen.tracer(0) # Value 0 turns off the true-time drawing, used together with update() below that manually does the trace

    move = turtle.Turtle() # Creates a turtle object with the name move
    move.speed(0)
    move.width(2)
    move.hideturtle()
    move.penup()
    move.goto(-250,0)
    move.pendown()

    line(0.5)


# Next step: https://www.geeksforgeeks.org/create-a-simple-animation-using-turtle-in-python/

