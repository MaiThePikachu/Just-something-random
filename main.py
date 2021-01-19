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
 
pygame.display.set_caption("Dating an NPC")
 
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
    # Welcome, starting questions, and start of the story
    print()
    print("Welcome! This is a text based game in a sense. Sure there are pictures, but this isn't the type of dating sim with buttons. It's one where you have to type the answers. When the choices are printed they will have ' ' around them and then you'll be able to type one of the given answers. (Please don't type the ' '. Also check if you typed the answers correctly because I don't have anything that will prevent you from mispelling.)")

    print()
    mc = input("What is your name: ")
    print()

    char = input("Okay. Next up is who do you want to date? A 'boy' or a 'girl': ")

    print()

    print("Hmmmmm...Should I give you the power to name them? Would be easier so I don't need to make their name lol.")

    print()

    char_name = input("What do you want their name to be: ")

    print()

    print("Perfect! Now that we have that done you can start the story. This takes place in (I guess) your bedroom and you're playing a game on your computer. It was an oddly popular game because in a way it was ''magical''. Alas it was some first-person, futuristic yet medieval polygon game. It had a couple of bugs allowing you to clip through many of the games objects. Things like trees and entire buildings even. Your walking through the forest clipping though a couple trees out of boredom. All of a sudden some bushes start moving.")

    if char == boy:
      print("An oddly realistic boy jumps out and lunges at your charater driving his sword into it's stomach. You roll your swivel chair (aka spinny chair) backwards from surprize wondering if this game really is buggy. You turn around the chair wondering if you saw your character corretly when you hear a loud thump.")

      print()

      option_1 = input("Do you 'turn_around' or do you 'stay': ")

      if option_1 == turn_around:
        print("???: Okay foolish human where did you send me.")
        print("He holds a blade towards you.")
        print("???: Who are you? Are you an apprentice to that wall phasing fool?")

        print("")








      elif option_1 == stay:
        print("???: What is this room? Where did this foolish human send me?"

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