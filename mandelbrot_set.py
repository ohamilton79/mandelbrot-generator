#ohamilton79
#09/06/2020
#Mandlebrot set generator
import numpy as np
import matplotlib.pyplot as plt
  
#SETTINGS - Modify as desired
magnification = 2
maxIterations = 255
xDisplacement = 0
yDisplacement = 0
#Step size (resolution) - number of points to create between start and end of image 
step = 3000
#Grayscale flag - if false the image is in colour
grayscale = False

#Get the start points and end points based on the magnification
startY = (-1.8) / magnification  - yDisplacement
endY = (1.8) / magnification  - yDisplacement
startX = (-2.4) / magnification + xDisplacement
endX = (1.2) / magnification + xDisplacement

#Create lists for x and y values
y, x = np.ogrid[ startY:endY:step*1j, startX:endX:step*1j ]

#Create complex number lists
c = x + y*1j
z = c

#Number of iterations required for each point - defaults to 255
iterationsList = maxIterations + np.zeros(z.shape, dtype=int)

#Loop over complex number list for the number of iterations provided
for iteration in range(maxIterations):
    #Map z to new complex number
    z = z**2 + c
    #If the real part of the complex number is more than 4 or less than 4,
    #it is diverging
    divergingMask = np.absolute(z.real) > 4

    #Get a mask for if it diverging NOW (its current iteration value is still
    #the default - the value of the max iterations variable
    divergingNowMask = divergingMask & (iterationsList==maxIterations)
    #Apply the mask, setting the values in these places to the value of the iteration variable
    iterationsList[divergingNowMask] = iteration
    
    #Set the values in the z variable equal to 0 so they don't slow down the rest of the program
    z[divergingMask] = 0

#Set the image size
plt.figure(figsize=(step/100, step/100))

#Set the colours list
colours = iterationsList

#If the grayscale flag is set
if grayscale:
    #Set plot to grayscale
    plt.gray()
    #Invert the colours
    colours = np.absolute(iterationsList - 255)
    
#Save the image to the disk, using the parameters to define the image name
plt.imshow(colours)
imageName = "mandlebrot%" + str(xDisplacement) + "%" + str(yDisplacement) + "x" + str(magnification) + ".png"
plt.savefig(imageName)
