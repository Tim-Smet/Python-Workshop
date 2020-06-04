import os
import random

# This is a guide. 
# If you want to build it completely from scratch please do so.
# But if you find it difficult then you can use the comments to guide you.
# If you are stuck, even with the comments, please ask me then.
# Try not to look at the solution.

# TODO
# Create class Board.
class Board():

    # TODO
    # Write init method to initialize attributes for your board.
    # The board will exist of 9 squares/ boxes. 
    # Each square can either be empty, filled with X or filled with O.
    # I only made a list with 10 elements (Now I can disregard index 0 and work with 1-9). 
    # Please feel free to use whatever you feel necessary.
    def __init__(self):
        self.cells = ["", "", "", "", "", "", "", "", "", ""] 
    

    # TODO
    # Make a method that will print the board.
    # print(" %s | %s | %s " %(self.cells[], ...))
    # You can use something like this.
    # %s are placeholders for stings.
    def drawBoard(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("----------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("----------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))
           

    # TODO
    # Method that checks if a certain square/cell/box (whatever you like to cal it) is empty.
    # I gave it one parameter.
    def check_cell_empty(self, cell_no):
        return self.cells[cell_no]


    # TODO
    # Here I made a method that will update my list.
    # If the player or the computer made a move this method will update my attribute.
    # So the placed letter will be placed at the corresponding index in my list.
    # This I gave two parameters.
    def update_cell(self, cell_no, player): 
        self.cells[cell_no] = player
        

    # TODO
    # Method that will check if there is a winner.
    # Just to clarify, you won when you have three in a row.
    # For you to figure out how many options there are to win.
    def check_winner(self):
        #diagonals
        if self.cells[1] == self.cells[5] == self.cells[9]:
            return self.cells[1]
        if self.cells[3] == self.cells[5] == self.cells[7]:
            return self.cells[3]

        #Horizontals
        if self.cells[1] == self.cells[2] == self.cells[3]:
            return self.cells[1]
        if self.cells[4] == self.cells[5] == self.cells[6]:
            return self.cells[4]
        if self.cells[7] == self.cells[8] == self.cells[9]:
            return self.cells[7]
        
        #Verticals
        if self.cells[1] == self.cells[4] == self.cells[7]:
            return self.cells[1]
        if self.cells[2] == self.cells[5] == self.cells[8]:
            return self.cells[2]
        if self.cells[3] == self.cells[6] == self.cells[9]:
            return self.cells[3]
        

    # TODO
    # Here I used a method to clear the terminal whenever I start a new game.
    def clear_screen(self):
        os.system("clear")

 

# So if you finished this you made the board class. Woehoew!! pfew pfew pfew (fireworks).
# Next the contestants class.
# This class I used to decide who will be the O and the X.
class Contestants():

    # TODO with what did we start the board class?
    def __init__(self):
        self.player = ""
        self.computer = ""
        self.choice = ["X", "O"]
    
    # TODO method that will decide who is who.
    def who_is_who(self):
        random_int = random.randint(0, 1)
        self.player = self.choice[random_int]
        if self.player == "X":
            self.computer == "O"
        else:
            self.computer == "X"


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
board = Board()
board.clear_screen()
board.drawBoard()

contestant = Contestants()
contestant.who_is_who()
player = contestant.player
computer = contestant.computer

if player == "X":
    print("Player will start")
    game_is_on = True
    while game_is_on:
        board.drawBoard()
        player_turn = True
        while player_turn:
            player_move = int(input("Enter a number 1-9: "))
            if not board.check_cell_empty(player_move):
                board.update_cell(player_move, player)
                player_turn = False
            else:
                print("Already taken")
                player_move = int(input("Enter a number 1-9: "))
            
        if board.check_winner():
            if board.check_winner() == player:
                board.drawBoard()
                print("Player has won.")
            else:
                board.drawBoard()
                print("Computer has won")
            game_is_on = False
        
        computer_turn = True
        while computer_turn:
            computer_move = random.randint(1, 10)
            if not board.check_cell_empty(computer_move):
                board.update_cell(computer_move, computer)
                computer_turn = False
            else:
                print("Already taken")
                computer_move = random.randint(1, 10)
    
        if board.check_winner():
            if board.check_winner() == computer:
                board.drawBoard()
                print("Computer has won.")
            else:
                board.drawBoard()
                print("Player has won")
            game_is_on = False
else:
    print("Computer will start")
    game_is_on = True
    while game_is_on:
        board.drawBoard()
        computer_turn = True
        while computer_turn:
            computer_move = random.randint(1, 10)
            if not board.check_cell_empty(computer_move):
                board.update_cell(computer_move, computer)
                computer_turn = False
    
        if board.check_winner():
            if board.check_winner() == computer:
                board.drawBoard()
                print("Computer has won.")
            else:
                board.drawBoard()
                print("Player has won")
            game_is_on = False
        
        player_turn = True
        while player_turn:
            player_move = int(input("Enter a number 1-9: "))
            if not board.check_cell_empty(player_move):
                board.update_cell(player_move, player)
                player_turn = False
            
        if board.check_winner():
            if board.check_winner() == player:
                board.drawBoard()
                print("Player has won.")
            else:
                board.drawBoard()
                print("Computer has won")
            game_is_on = False
print("Thank you for playing!")