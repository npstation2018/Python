import turtle
#make the random module available for us to use
#this one allows us to generate random numbers

import random

#create a stamp
stamp = turtle.Turtle()

#make it a turtle shape
stamp.shape('turtle')

#lift the color of the stamp so we dont draw a continous line
stamp.penup()
#set RGB color mode to allow random colors in RGB
turtle.colormode(255)

#set some variable
#one for the initial distance to move (paces)
#and three more to hold the starting RGB values
paces = 20
random_red = 50
random_green = 50
random_blue = 50

#start a for loop to repeat the stamping code
#repeat 50 times

for i in range(50):
    #use random function to pick a random number for the red value

    random_red = random.randint(0,255)
    #repeat random function for green
    random_green = random.randint(0,255)
    #repeat random function for blue
    random_blue = random.randint(0,255)
    #set the stamp color with the randomly chosen RGB values
    stamp.color(random_red, random_green, random_blue)
    #STAMP -stamp a turtle with the colors from the last step
    stamp.stamp()
    #add more paces
    paces += 3
    #move fwd by the new number of paces
    stamp.forward(paces)
    #slighly turn direction as we move to start spiralling
    stamp.right(25)
    
