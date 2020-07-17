#!/usr/bin/python3
# Load needed modules

import sys,getopt
import random
import math
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

#############################################################################################
# function to calculate the color of the pixel
#############################################################################################
def Mandel_Calc(k1, k1i, c, ci):
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

        # make output the new input
        k1 = ksum;
        k1i = kisum;
        #
        lco = lco + 1
        if betrag >= 2:
            break
    # return color
    # print(lco);
    return lco
#############################################################################################




#############################################################################################
# function to plot the pixel
#############################################################################################
def Plot_Pixel(x,y,color):
    proz = int(color)
    #proz = int(100*color/iterations)
    #print (proz)
#    if color<50:
#        #good
#        img.putpixel((x,y),((5*color)-10,20,20))
#    if (color>50) and (color<250):
#        #todo:
#        #img.putpixel((x,y),(18*(int(round(proz))),22*(int(round(proz))),20))
#        img.putpixel((x,y),(12*(int(round(proz))),50-(18*(int(round(proz)))),105))
#

    if color == iterations:
    # if the pixel is most likely within the set paint it black
       img.putpixel((x,y),(0,0,0))
    else:
       img.putpixel((x,y),(0,proz,0))
#############################################################################################

#############################################################################################
# function to correct the start position for the next image
#############################################################################################
def X_Corrector():
    xcorrect = 0
    return xcorrect

#############################################################################################
# function to draw the mandel pixels
#############################################################################################
def Draw_Mandel(xmin,xmax,ymin,ymax,resx,resy,count):
    print ("------------Image:",i,"--------------")
    print ("X:",xmin,"-->",xmax)
    print ("Y:",ymin,"-->",ymax)
    # calculate the distance between two dots
    stepsx = (xmax-xmin)/resx
    stepsy = (ymax-ymin)/resy
    # set starting dots
    xx = xmin
    yy = ymin

    # counter, needed to calculate the visual center
    countx = 0
    county = 0

    # is the visual center going out of the image?
    global alarm
    global correctx
    alarm = 0
    correctx = 0
    # as long as we are in the defined Y-Frame do:
    while (yy <= ymax):
        # do all the plotting for the current X-line
        while (xx <= xmax):
            # send the floats of the dots to function Mandel_Calc to calculate the color of the current pixel
            depth = Mandel_Calc(xx,yy,xx,yy)
            # plot the pixel to the canvas via function Plot_Pixel
            Plot_Pixel(countx,county,depth)

            # mark the area around the target coordinates green
            # the smaller the numer after coma, the bigger the area
            if (round(xx,1) == xdest) & (round(yy,1) == ydest):
                img.putpixel((countx,county),(0,255,0 ))
                # print countx,stepsx,count, xmin, "<",xx,">",xmax
                correctx = -1*(xx-stepsx)
                # print "CORR:", correctx
            # mark the middle of the screen white
            if (countx == resx/2) | (county == resy/2) :
                img.putpixel((countx,county),(255,255,255))
            # if the coordinate of interest is too far away from the view center:
            if (xx >= xdest) & (countx == resx/2) & (county == resy/2):
                print ("Alarm! Mitte bei: ", xx, "> ", xdest,"\n")
                alarm = 1
            #    correct = stepsx


            # increase to the next pixel on the X-line
            xx = xx + stepsx
            # increase # of runs for X
            countx = countx + 1
            # if the x-center of the viewport is right of the target x-coordinate:
        yy = yy + stepsy
        # "carrige-return" for X
        xx = xmin
        countx = 0
        # set plotter to the next Y-Line
        county = county + 1
        #
    font = ImageFont.load_default().font
    draw = ImageDraw.Draw(img)
    draw.text((20,0),str(i)+": X_min: "+str(xmin),(255,255,255),font=font)
    draw.text((20,10),str(i)+": Y_min: "+str(ymin),(255,255,255),font=font)
    #draw.text((20,10),str(correctx))



#############################################################################################

# the color depth of the pixels
#iterations = 1254


# Read in arguments
xdest = float(sys.argv[1])
ydest = float(sys.argv[2])
frame = float(sys.argv[3])
iterations = int(sys.argv[4])
images = int(sys.argv[5])


resx = 220
resy = 220


depth = 0.0

offsetx = 0


xmin = xdest - frame
xmax = xdest + frame
ymin = ydest - frame
ymax = ydest + frame



# How many images are to be rendered?
#images = 1
zoom = 2
# Do we know if the destitnation coordinates are in
# the center of the image?
center = True

for i in range(0, images):
    # only draw, if the target coordinates are centered
    if (center == True) :
        # create a black Image object
        img = Image.new("RGB",(resx,resy),(0,0,0))
        # render the image
        Draw_Mandel(xmin,xmax,ymin,ymax,resx-1,resy-1,i)
        img.show()

        zoom = zoom * 2
        xmin = xdest - frame/zoom
        xmax = xdest + frame/zoom
        ymin = ydest - frame/zoom
        ymax = ydest + frame/zoom
# Und nu?
