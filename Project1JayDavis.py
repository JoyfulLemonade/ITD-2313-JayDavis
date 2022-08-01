import turtle
def drawCircle(t, centre, radius):
    (x,y) = centre
    t.up()
    t.setpos(x,y)
    t.left(3)
    t.down()
    t.circle(120)
    circumference = 2 * 3.14 * (radius/120)
    print ("distance moved: ", circumference)
    drawCircle(turtle(), (100,100), 20)
    def drawCircle(t, centrePosition, radius):
        t.up()
        t.setpos(centrePosition)
        t.left(3)
        t.down()
        t.circle(120)
        print ("Circumference moved is", (2 * 3.14 * (radius/120)))
turtle
        

