#!/usr/bin/python3
import multiprocessing as mp
import math
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def Calc(x):
    #print(mp.current_process())
    return x**x

def f1(args):
    a, b, c = args[0] , args[1] , args[2]
    return a+b+c


def Render_Man(x,y,distance,field):
    color = field * 30
    xstart = x

    for y in range(y, y+distance):
        for x in range(x, x+distance):
            image.putpixel((x,y),(0,color,0))
            x = x+1
        y = y+1
        x = xstart


def main():
    pool = mp.Pool(mp.cpu_count())
    result = pool.map(Calc, [4,2,3,5,3,2,1,2,6,6])
    result_set_2 = pool.map(Calc, [4,6,5,4,6,3,23,4,6,3,4,4,])

    res         = 240
    resx        = res
    resy        = res

    fields      = 9

    parts       = int(math.sqrt(fields))
    distance    = int(res/parts)

    #print ("Resolution: ",res)
    #print ("Sides will be devided in: ",parts)
    #print ("Pixel distance is: ", distance)

    # create a black image object
    global image
    image = Image.new("RGB",(resx,resy),(255,0,0))

    count       = 1
    xoffset     = 0
    yoffset     = 0
    xt          = 0
    yt          = 0

    xsqrs = int(math.sqrt(fields))
    ysqrs = xsqrs

    print (pool)
    for ycount in range(1, 4):
        for xcount in range(1, 4):

            #print ("X-off: ",xoffset,"Y-off: ",yoffset,"X: ",xt,"Y: ",yt)
            print ("X: ",xt,"Y: ",yt,"Farbe: ",count)
            Render_Man(xt,yt,distance,count)
            #xoffset = xoffset+distance
            xt = xt + distance
            #print ("X-off: ",xoffset,"Y-off: ",yoffset,"X: ",xt,"Y: ",yt)

            #print("Field ", count, "done.")
            count = count + 1
            #print("\\\\\\\\\\\\\\\\\\\\\\\\///////////////////////////")

        #yoffset = yoffset+distance
        yt = yt+distance
        xt = 0
        #print ("runs: ", count)
        #print ("xoffset: ", xoffset,"yoffset: ", yoffset)
        print ("-----------------------------------------")
    image.show()
    #    offset = offset + int(resx)/parts
    #    xt = + offset
    #    yt = xt

    pool = mp.Pool(4)
    #resalt = pool.map(f1, [ (0,0,1)(0,40,2)(0,80,3)])
    #print(resalt)
    print(result)



if  __name__ == "__main__":
    main()
