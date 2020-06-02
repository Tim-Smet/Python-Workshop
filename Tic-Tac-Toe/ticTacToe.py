import os
import random

# This is a guide. 
# If you want to build it completely from scratch please do so.
# But if you find it difficult then you can use the comments to guide you.
# If you are stuck, even with the comments, please ask me then.
# Try not to look at the solution.

# TODO
# Create class Board.

    # TODO
    # Write init method to initialize attributes for your board.
    # The board will exist of 9 squares/ boxes. 
    # Each square can either be empty, filled with X or filled with O.
    # I only made a list with 10 elements (Now I can disregard index 0 and work with 1-9). 
    # Please feel free to use whatever you feel necessary. 
    

    # TODO
    # Make a method that will print the board.
    # print(" %s | %s | %s " %(self.cells[], ...))
    # You can use something like this.
    # %s are placeholders for stings.
    

    # TODO
    # Method that checks if a certain square/cell/box (whatever you like to cal it) is empty.
    # I gave it one parameter.


    # TODO
    # Here I made a method that will update my list.
    # If the player or the computer made a move this method will update my attribute.
    # So the placed letter will be placed at the corresponding index in my list.
    # This I gave two parameters. 
    

    # TODO
    # Method that will check if there is a winner.
    # Just to clarify, you won when you have three in a row.
    # For you to figure out how many options there are to win.
    

    # TODO
    # Here I used a method to clear the terminal whenever I start a new game.
    

# So if you finished this you made the board class. Woehoew!! pfew pfew pfew (fireworks).
# Next the contestants class.
# This class I used to decide who will be the O and the X.


    # TODO with what did we start the board class?

    
    # TODO method that will decide who is who.
    

# Next is the Game play.
# I will write as much as I can here. 
# But I think it is a great exercise to think about the game play yourself and try to implement it.
# So we made a board class and we should make a board object.
# Just the same for the contestants. We need two players to play it.
# So I decided randomly who gets to be X and O. Either the computer or you can start that way.
# It are alternating turns. If you start, the next one is the computer and so on.
# It is good practice to check for a winner after every move.
# Also check if the cell where you want to make a move is free.
# (02/06/2020 ; 14:48) At this moment my code is not well formated, I am sorry.
# But it works.
# I am not sure how long this will take, but if there is time left I want to introduce the minimax algorithm.
# This makes the computer a little bit smarter. 
# Right now it decides where to make a move randomly, that is not so clever.
