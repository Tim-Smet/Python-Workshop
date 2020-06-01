import os
import random

class Board():
    def __init__(self):
        self.cells = ["", "", "", "", "", "", "", "", "", ""]

    def drawBoard(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("---------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("---------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    def check_cell_empty(self, cell_no):
        #If string on given index is empty, this returns false
        return self.cells[cell_no]
  
    def update_cell(self, cell_no, player):
        if not self.check_cell_empty(cell_no):
            self.cells[cell_no] = player

    def who_won(self):
        #Diagonal
        if self.cells[1] == self.cells[5] and self.cells[5] == self.cells[9]:
            return self.cells[1]
        if self.cells[3] == self.cells[5] and self.cells[5] == self.cells[7]:
            return self.cells[3]
        
        #Horizontal
        if self.cells[1] == self.cells[2] and self.cells[2] == self.cells[3]:
            return self.cells[1]
        if self.cells[4] == self.cells[5] and self.cells[5] == self.cells[6]:
            return self.cells[4]
        if self.cells[7] == self.cells[8] and self.cells[8] == self.cells[9]:
            return self.cells[7]

        #Vertical
        if self.cells[1] == self.cells[4] and self.cells[4] == self.cells[7]:
            return self.cells[1]
        if self.cells[2] == self.cells[5] and self.cells[5] == self.cells[8]:
            return self.cells[2]
        if self.cells[3] == self.cells[6] and self.cells[6] == self.cells[9]:
            return self.cells[3]

    def refresh_screen(self):
        os.system("clear") 


class Players():
    def __init__(self):
        self.player = ""
        self.computer = ""
        self.signs = ["X", "O"]
    
    def decide_sign(self):
        rand_int = random.randint(0, 1)
        self.player = self.signs[rand_int]
        if self.player == "X":
            self.computer = "O"
        else:
            self.computer = "X"



#Game play
board = Board()
board.refresh_screen()
print("Decide who is who. X can start.")

obj = Players()
obj.decide_sign()
player = obj.player
computer = obj.computer

print("Player is: %s\n" %(player))
print("Computer is: %s\n" %(computer))
if player == "X":
    print("Player can start")
else:
    print("Computer will take first turn.")
print("\nLet the game begin!!!")
game_is_on = True
while game_is_on:
    board.drawBoard()
    player_move = int(input("Pick your move, 1-9: "))
    board.update_cell(player_move, player) 
    if board.who_won():
        if board.who_won() == player:
            board.drawBoard()
            print("Player has won.")
        else:
            board.drawBoard()
            print("Computer has won")
        game_is_on = False
    else:
        print("No winner yet.")

print("Thank you for playing")
