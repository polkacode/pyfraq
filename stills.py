#!/usr/bin/python3
import multiprocessing as mp
import math
import matplotlib.cm
import sys,getopt
import random
import argparse 

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from mpmath import mp as mpm
import mpmath.libmp

def CreateInferno():
    # viridis, cividis, magma, plasma, inferno
    cmap1 = matplotlib.cm.get_cmap("magma")
    cmap2 = matplotlib.cm.get_cmap("magma")
    cmap3 = matplotlib.cm.get_cmap("magma")
    cmap4 = matplotlib.cm.get_cmap("magma")
    for i in range (0,255):
        #print (cmap.colors[i])
        color = cmap1.colors[i]
        r = int(color[0]*255)
        g = int(color[1]*255)
        b = int(color[2]*255)
        rgb = r,g,b
        inferno.append(rgb)
    for i in range (255, 0, -1):
        #print (cmap.colors[i])
        color = cmap1.colors[i]
        r = int(color[0]*255)
        g = int(color[1]*255)
        b = int(color[2]*255)
        rgb = r,g,b
        inferno.append(rgb)
    for i in range (0,255):
        #print (cmap.colors[i])
        color = cmap2.colors[i]
        r = int(color[0]*255)
        g = int(color[1]*255)
        b = int(color[2]*255)
        rgb = r,g,b
        inferno.append(rgb)
    for i in range (255, 0, -1):
        #print (cmap.colors[i])
        color = cmap2.colors[i]
        r = int(color[0]*255)
        g = int(color[1]*255)
        b = int(color[2]*255)
        rgb = r,g,b
        inferno.append(rgb)
    for i in range (0,255):
        #print (cmap.colors[i])
        color = cmap3.colors[i]
        r = int(color[0]*255)
        g = int(color[1]*255)
        b = int(color[2]*255)
        rgb = r,g,b
        inferno.append(rgb)
    for i in range (255, 0, -1):
        #print (cmap.colors[i])
        color = cmap3.colors[i]
        r = int(color[0]*255)
        g = int(color[1]*255)
        b = int(color[2]*255)
        rgb = r,g,b
        inferno.append(rgb)
    for i in range (0,255):
        #print (cmap.colors[i])
        color = cmap4.colors[i]
        r = int(color[0]*255)
        g = int(color[1]*255)
        b = int(color[2]*255)
        rgb = r,g,b
        inferno.append(rgb)
    for i in range (255, 0, -1):
        #print (cmap.colors[i])
        color = cmap4.colors[i]
        r = int(color[0]*255)
        g = int(color[1]*255)
        b = int(color[2]*255)
        rgb = r,g,b
        inferno.append(rgb)

def Plot_Pixel(x,y,color):
    #index = int(color/icount*255)
    index = int(color*len(inferno)/iterations)
    if color == iterations:
    # if the pixel is most likely within the set paint it black
       img.putpixel((x,y),(0,0,0))
    else:
       img.putpixel((x,y),(inferno[index]))

def Crunch(args):
    k1, k1i, x, y = args[0] , args[1] , args[2] , args[3]

    c = k1
    ci = k1i
    ksum = 0
    kisum = 0
    kprod = 0
    kiprod = 0
    betrag = 0
    lco = 0

    for a in range(0, iterations):
        # Multiplikation der Komplexen Zahl (k1+k1i)G mit sich selbst (k1+k1i)^2 :
        kprod = (k1 * k1) + (k1i * k1i) * -1
        kiprod = (k1 * k1i) + (k1i * k1)
        #System.out.println("Komplexes Produkt:"+kprod+"+"+kiprod);
        # Addition von (c+ci) auf das Ergebnis von (k1+k1i)^2
        ksum = kprod + c
        kisum = kiprod + ci
        # System.out.println("Komplexe Summe:"+ksum+"+"+kisum);
        # Ermitteln des Betrags
        betrag = math.sqrt((ksum * ksum) + (kisum * kisum));
        #print (betrag)
        # make output the new input
        k1 = ksum;
        k1i = kisum;
        #
        lco = lco + 1
        if betrag >= 2:
            break
    positions = x,y,lco
    return positions

def FillCoord(xmin,xmax,ymin,ymax,resx,resy):
    # This function creates an array - coord[] - that contains
    # all the real numbers coordinates and the pixel coordinates,
    # which will be later on Crunched in parralel

    # calculate the distance between two pixels
    incrx = (xmax-xmin)/(resx-1)
    incry = (ymax-ymin)/(resy-1)
    # set starting dots
    xx = xmin
    yy = ymin
    # counter, needed to determine plotting positions
    countx = 0
    county = 0

    # as long as we are in the defined Y-distance do:
    while (yy <= ymax):
        # do all the plotting for the current X-line
        while (xx <= xmax):
            # create an athe payload for the heavy crunching later on
            pyload = xx, yy, countx, county
            coord.append (pyload)
            # increase to the next pixel on the X-line
            xx = xx + incrx
            # increase # of runs for X
            countx = countx + 1
            # if the x-center of the viewport is right of the target x-coordinate:
        yy = yy + incry
        # "carrige-return" for X
        xx = xmin
        countx = 0
        # set plotter to the next Y-Line
        county = county + 1

# set precision

if len(sys.argv) == 1:
    #print("stills.py: missing operand\n Try 'stills.py -h' for more information.")
    print("Usage: \n stills.py X Y radius iterations number_off_images X-resolution filename precisision")
    print("\n Example: ./stills.py 0.432539867562523 0.22611867595189 .00000000000000000023 2000 1 320 dive")

    exit()


mpm.dps = 30 

xdest = mpm.mpf(float(sys.argv[1]))
ydest = mpm.mpf(float(sys.argv[2])*-1)
offset = mpm.mpf(float(sys.argv[3]))
iterations = int(sys.argv[4])
images = int(sys.argv[5])
resx = int(sys.argv[6])
filename = (sys.argv[7])


print ("Radius: ", offset)

percx = 0
percy = 0


offsetx = offset
offsety = offsetx*.5625

resy = int(resx*.5625)

# Define start positions
xmin = xdest - offsetx
ymin = ydest - offsety
xmax = xdest + offsetx
ymax = ydest + offsety

# declare an empty list for all coordinates and colors (will be used in FillCoord)
coord = []
# declare an empy list for all colors (will be used in the CreateInferno function)
inferno = []
CreateInferno()
# create an empty canvas in the img opject
img = Image.new("RGB",(resx,resy),(0,0,0))



for i in range(0, images):

    # create the list with all coordinates (real numbers and coordinates in the images)
    FillCoord(xmin,xmax,ymin,ymax,resx,resy)

    # create a parallel pool and get the testing done by executing the Crunch()
    # function in parallel pool = mp.Pool(mp.cpu_count()) would claim all cores
    # As a result pcoords contains a list of all x und y coordinate and the corresponding color

    # Just 10 cores:
    pool = mp.Pool(200)
    pcoords = pool.map(Crunch, coord)
    pool.terminate()

    # Iterate through the list and let the pixels be drawn
    for pos in pcoords:
        Plot_Pixel(pos[0],pos[1],pos[2])

    #img.show()
    img.save( filename + str(i) + ".png")
    print (filename+str(i),".png written.")

    percx = 95*offsetx/100
    percy = 95*offsety/100
    print ("image: ",i)
    ymax = ydest + percy
    xmin = xdest - percx
    xmax = xdest + percx
    ymin = ydest - percy
    offsetx = percx
    offsety = percy

#  ./stills.py 0.432539867562523 0.22611867595189 .00000000000000000023 2000 3  280 test

