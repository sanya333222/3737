x=0
def setup():
    size(500,600)
def draw():
    global x
    translate(x,100)
    rotate(radians(x))
    ellipse(0, 0, 60 ,90)
    x=x+1
