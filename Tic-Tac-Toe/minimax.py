import os
import random
import math

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


class Contestants():
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

    def player_move(self, board, player):
        player_move = int(input("Pick your move, 1-9: "))
        
        player_turn = True
        while player_turn:
            if not board.check_cell_empty(player_move):
                board.update_cell(player_move, player)
                break
            else:
                print("This spot is already taken")

    def make_best_move(self, board, computer):
        bestScore = -math.inf
        bestMove = None
        move = 1
        for move in range(1, len(board.cells)):
            if board.cells[move] == "":
                board.update_cell(move, computer)
                score = self.minimax(False, board, computer)
                empty_string = ""
                board.update_cell(move, empty_string)
                if (score > bestScore):
                    bestScore = score
                    bestMove = move
        board.update_cell(bestMove, computer)

    def minimax(self, isMaxTurn, board, computer):
        if board.who_won() == None:
            return 0
        elif board.who_won():
            return 1 if board.who_won() == computer else -1

        scores = []
        for move in range(len(board.cells)):
            if board.cells[move] == "":
                board.update_cell(move, computer)
                scores.append(self.minimax(not isMaxTurn, board, computer))
                empty_string = ""
                board.update_cell(move, empty_string)
                
            #if (isMaxTurn and max(scores) == 1):
             #   break

        return max(scores) if isMaxTurn else min(scores)


#Game play
board = Board()
board.refresh_screen()
print("Decide who is who. X can start.")

contestant = Contestants()
contestant.decide_sign()
player = contestant.player
computer = contestant.computer

print("Player is: %s\n" %(player))
print("Computer is: %s\n" %(computer))
if player == "X":
    print("Player can start")
    print("\nLet the game begin!!!")
    game_is_on = True
    while game_is_on:
        board.drawBoard()
        contestant.player_move(board, player)
        
        if board.who_won():
            if board.who_won() == player:
                board.drawBoard()
                print("Player has won.")
            else:
                board.drawBoard()
                print("Computer has won")
            game_is_on = False

        elif "" not in board.cells:
            print("This is a draw")
            game_is_on = False

        else:
            contestant.make_best_move(board, computer)
        
            if board.who_won():
                if board.who_won() == computer:
                    board.drawBoard()
                    print("Computer has won.")
                else:
                    board.drawBoard()
                    print("Player has won")
                game_is_on = False
        
        
else:
    print("Computer will take first turn.")
    print("\nLet the game begin!!!")
    game_is_on = True
    while game_is_on:
        contestant.make_best_move(board, computer)
        board.drawBoard()
        
        if board.who_won():
            if board.who_won() == computer:
                board.drawBoard()
                print("Computer has won.")
            else:
                board.drawBoard()
                print("Player has won")
            game_is_on = False

        elif "" not in board.cells:
            print("This is a draw")
            game_is_on = False

        else:
            contestant.player_move(board, player)

            if board.who_won():
                if board.who_won() == player:
                    board.drawBoard()
                    print("Player has won.")
                else:
                    board.drawBoard()
                    print("Computer has won")
                game_is_on = False
        

print("Thank you for playing")
