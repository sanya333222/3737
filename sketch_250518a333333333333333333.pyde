x=0
def setup():
    size(500,600)
def draw():
    global x
    translate(100,100)
    rotate(radians(x))
    fill(random(0,250),random(0,250),random(0,250))
    ellipse(0, 0, 60,90)
    rect(0,0,30,50)
    triangle(0, 0, 30, 20,20,40)
    x=x+1
