#!/usr/bin/python3
import multiprocessing as mp
import math
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def Calc(x):
    #print(mp.current_process())
    return x**x


def Render_Man(x,y,distance,field):
    if field == 1:
        color = (255,0,0)
    if field == 2:
        color = (100,100,0)
    if field == 3:
        color = (200,200,200)

    print ("Rendering...")
    xstart = x
    ystart = y

    for y in range(y, y+distance):
        for x in range(x, x+distance):
            image.putpixel((x,y),(color))
            x = x+1
        y = y+1
        x = xstart

def main():
    pool = mp.Pool(mp.cpu_count())
    result = pool.map(Calc, [4,2,3,5,3,2,1,2,6,6])
    result_set_2 = pool.map(Calc, [4,6,5,4,6,3,23,4,6,3,4,4,])

    res         = 200
    resx        = res
    resy        = res

    fields      = 9

    parts       = int(math.sqrt(fields))
    distance    = int(res/parts)

    print ("Resolution: ",res)
    print ("Sides will be devided in: ",parts)
    print ("Parts are:", distance)

    # create a black image object
    global image
    image = Image.new("RGB",(resx,resy),(0,0,0))

    count       = 1
    offset      = 0

    #Render_Man(800,400,distance,3)
    for squares in range(1, int(parts)+1):
        if count > 1:
            offset = distance
        xt = 1
        yt = 1
        Render_Man(int(xt)+offset,int(yt)+offset,distance,count)
        print ("runs: ", count)
        count = count+1
    #    offset = offset + int(resx)/parts
    #    xt = + offset
    #    yt = xt
    image.show()


if  __name__ == "__main__":
    main()
