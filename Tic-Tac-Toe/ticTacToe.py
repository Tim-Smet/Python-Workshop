import os
import random

class Board():
    def __init__(self):
        self.cells = ["", "", "", "", "", "", "", "", "", ""] 
    
    def drawBoard(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("----------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("----------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))
           
    def check_cell_empty(self, cell_no):
        return self.cells[cell_no]

    def update_cell(self, cell_no, player): 
        self.cells[cell_no] = player
        
    def check_winner(self):
        #diagonals
        if self.cells[1] == self.cells[5] and self.cells[5] == self.cells[9]:
            return self.cells[1]
        if self.cells[3] == self.cells[5] and self.cells[5] == self.cells[7]:
            return self.cells[3]

        #Horizontals
        if self.cells[1] == self.cells[2] and self.cells[2] == self.cells[3]:
            return self.cells[1]
        if self.cells[4] == self.cells[5] and self.cells[5] == self.cells[6]:
            return self.cells[4]
        if self.cells[7] == self.cells[8] and self.cells[8] == self.cells[9]:
            return self.cells[7]
        
        #Verticals
        if self.cells[1] == self.cells[4] and self.cells[4] == self.cells[7]:
            return self.cells[1]
        if self.cells[2] == self.cells[5] and self.cells[5] == self.cells[8]:
            return self.cells[2]
        if self.cells[3] == self.cells[6] and self.cells[6] == self.cells[9]:
            return self.cells[3]
        
    def clear_screen(self):
        os.system("clear")

 
class Contestants():
    def __init__(self):
        self.player = ""
        self.computer = ""
        self.choice = ["X", "O"]

    def who_is_who(self):
        random_int = random.randint(0, 1)
        self.player = self.choice[random_int]
        if self.player == "X":
            self.computer = "O"
        else:
            self.computer = "X"


def check_winner_func(board):
    if board.check_winner() == player:
        print("Player has won.")
        return False
    elif board.check_winner() == computer:
        print("Computer has won")
        return False
    else:
        return True

def check_draw(board):
    if not board.check_winner():
        board.cells[0] = "X"
        if "" in board.cells:
            board.cells[0] = ""
        else:
            print("We have a draw!")
            return True

def player_turn(player):
    player_move = int(input("Enter a number 1-9: "))
    if player_move < 10 and player_move > 0:
        if not board.check_cell_empty(player_move):
            board.update_cell(player_move, player)
        else:
            print("Already taken")
            player_turn(player)
    else:
        print("Please enter a number from 1-9.")
        player_turn(player)
    
def computer_turn(computer):
    computer_move = random.randint(1, 9)
    if not board.check_cell_empty(computer_move):
        board.update_cell(computer_move, computer)
    else:
        computer_turn(computer)
        


board = Board()
board.clear_screen()
contestant = Contestants()
contestant.who_is_who()
player = contestant.player
computer = contestant.computer

if player == "X":
    print("Player will start")
    while check_winner_func(board):
        board.drawBoard()
        player_turn(player)
        if not check_winner_func(board):
            board.drawBoard()
            break
        elif check_draw(board):
            break
        else:
            computer_turn(computer)
            check_winner_func(board)
        
else:
    print("Computer will start")
    while check_winner_func(board):
        computer_turn(computer)
        board.drawBoard()        
        if not check_winner_func(board):
            break
        elif check_draw(board):
            break
        else:
            player_turn(player)
            if not check_winner_func(board):
                board.drawBoard()

print("Thank you for playing!")