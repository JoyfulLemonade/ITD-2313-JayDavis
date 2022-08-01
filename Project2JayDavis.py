import turtle
import random
#add basics of program
def cCurve (t, x1, y1, x2, y2, level):
    colors  = ["red","orange","purple","green","gray","blue","pink","yellow","brown"] 
def drawLine(x1, y1, x2, y2):
        t.up()
        t.goto(x1, y1)
        t.pencolor(random.choice(colors))
        t.down()
        t.goto(x2, y2)
        if level == 0:
            drawLine(x1, y1, x2, y2)
        else:
            xm = (x1 + x2 + y1 - y2) // 2
            ym = (x2 + y1 + y2 - x1) // 2
            cCurve(t, x1, y1, xm, ym, level - 1)
            cCurve(t, xm, ym, x2, y2, level - 1)
#main begin
def main():
    level = int(input("enter level (0 or greater): "))
    t = turtle()
    if level > 8:
        tracer(False)
        t.pencolor("purple")
        t.hideturtle()
        cCurve(t, 50, -50, 50, 50, level)
        if level > 8: update()
def cCurve (t, x1, y1, x2, y2, level):
    colors = ["red","orange","purple","green","gray","blue","pink","yellow","brown"]
def drawLine(x1, y1, x2, y2):
    t.up()
    t.goto(x1, y1)
    t.pencolor(random.choice(colors))
    t.down()
    t.goto(x2, y2)
#WOOOOO
