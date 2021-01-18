'''
-------------------------------------------------------------------------------
Name:		main.py
Purpose:	A dating simulator.

Author:	Soon Fah.M
Created:	date in 18/01/2021
------------------------------------------------------------------------------
'''

import pygame
 
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
 
pygame.init()
  
# Set the width and height of the screen [width, height]
size = (750, 580)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
  

    # --- Game logic should go here
    print()
    print("Welcome! This is a text based game in a sense. Sure there are pictures, but this isn't the type of dating sim with buttons. It's one where you have to type the answers. When the choices are printed they will have ' ' around them and then you'll be able to type one of the given answers. (Please don't type the ' '.)")

    print()
    mc = input("What is your name: ")
    print()

    char = input("Okay. Next up is who do you want to date? A 'boy' or a 'girl': ")




    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.
    screen.fill(white)
 
    # --- Drawing code should go here
     
    
     
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()