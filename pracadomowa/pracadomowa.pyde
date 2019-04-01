def setup():
    frameRate(60)
    size(400, 400)
    rectMode(CENTER)
    rect(50, height/2, 100, 50, 10)
    global x
    global y
    global krotkaZkolorami
    x = 50
    y = 200
    krotkaZkolorami = ((0,15,15),(200,0,100),(0,215,0),(0,0,114),(255,100,50),(20,100,0))
    krotkaZkolorami[1]
    stroke(*krotkaZkolorami[3])
    strokeWeight(8)
    background(255, 204, 0)
    fill(250,0,73)
def draw():
    global x
    global y
    if mousePressed:
        rect(x, y, 100, 50, 10)
        x+=1
        y-=1
        #tą część można było rozegrać w pętli
        if x>35:  #wóczas x zwiększał by się o taką samą wartość
            stroke(*krotkaZkolorami[0])  #a tu zwiększałby się index
        if x>70:
            stroke(*krotkaZkolorami[1])
        if x>105:
            stroke(*krotkaZkolorami[2])
        if x>135:
            stroke(*krotkaZkolorami[3])
        if x>170:
            stroke(*krotkaZkolorami[4])
        if x>205:
            stroke(*krotkaZkolorami[5])        
        if (x>width/2+25):
            exit()
        fill(random(255),random(255),random(255),random(255))
def mousePressed():
    loop()


    