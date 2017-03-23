# 2008/11/07 
# Author: Jose Lopes de Oliveira Junior
#     http://versaopropria.blogspot.com
#     jlojunior _at_ gmail _dot_ com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307,
# USA.

class TicTacToe:
    
    """Implements modules which enable to play Tic-tac-toe game."""
    
    def __init__(self):
        
        """Initialization of the board."""
        
        print "\nC'mon, bro! Let's play TIC-TAC-TOE!!! :-)\n"
        
        # 0 for empty; 1 for X; 2 for O.
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    def __del__(self):
        
        """Prints a good bye message on object's destroy."""
        
        print "Bye!\n"
    
    def __str__(self):
        
        """Object's string representation."""
        
        return "Tic-Tac-Toe is cool!"
    
    
    def print_board(self):
        
        """Prints the board on screen."""
        
        row_number = 1  # Counts the number of rows
        print "\n  1 2 3"  # Prints the header of the board
        
        # Iterates printing the number of the row and its contents.
        for row in self.board:
            print row_number,
            row_number += 1
            
            for item in row:
                if item == 1: print 'X',
                
                elif item == 2: print 'O',
                
                else: print '-',
            
            print
        
        print
    
    def set_item(self, x, y, value):
        
        """Change the value of a determined item of the board.
        
        Requires the coordinate to change, given in x and y
        variables and the new value. x and y must be between
        1 and 3. If another value will passed, an error will
        be returned. This function also corrects the value of
        x and y variables. For the player, these variables
        can be 1, 2 or 3. Internally, the program work with
        0, 1 or 2.
        Returns 0 for success and 1 for fail.
        
        """
        
        if self.board[x - 1][y - 1]:
            return 1
        
        else:
            self.board[x - 1][y - 1] = value
            return 0
    
    def look_for_winner(self):
        
        """Compares the values of the rows, columns and 
        diagonals, looking for a winner.
        
        Returns 0 for no winner or the number of the 
        winner (1 or 2).
        
        """
        
        # Horizontals
        if (self.board[0][0] != 0) and ((self.board[0][0] == 
                                         self.board[0][1]) and 
                                         (self.board[0][0] == 
                                          self.board[0][2])):
            return self.board[0][0]
        
        elif (self.board[1][0] != 0) and ((self.board[1][0] == 
                                           self.board[1][1]) and 
                                           (self.board[1][0] == 
                                            self.board[1][2])):
            return self.board[1][0]
        
        elif (self.board[2][0] != 0) and ((self.board[2][0] == 
                                           self.board[2][1]) and 
                                           (self.board[2][0] == 
                                            self.board[2][2])):
            return self.board[2][0]
        
        # Verticals
        elif (self.board[0][0] != 0) and ((self.board[0][0] == 
                                           self.board[1][0]) and 
                                           (self.board[0][0] == 
                                            self.board[2][0])):
            return self.board[0][0]
        
        elif (self.board[0][1] != 0) and ((self.board[0][1] == 
                                           self.board[1][1]) and 
                                           (self.board[0][1] == 
                                            self.board[2][1])):
            return self.board[0][1]
        
        elif (self.board[0][2] != 0) and ((self.board[0][2] == 
                                           self.board[1][2]) and 
                                           (self.board[0][2] == 
                                            self.board[2][2])):
            return self.board[0][2]
        
        
        # Diagonals
        elif (self.board[0][0] != 0) and ((self.board[0][0] == 
                                           self.board[1][1]) and 
                                           (self.board[0][0] == 
                                            self.board[2][2])):
            return self.board[0][0]
        
        elif (self.board[0][2] != 0) and ((self.board[0][2] == 
                                           self.board[1][1]) and 
                                           (self.board[0][2] == 
                                            self.board[2][0])):
            return self.board[0][2]
        
        # No winner
        else:
            return 0
    
    def play(self):
        
        """The main method of the class. Implements the game play."""
        
        change = True  # Change between player 1 and 2
        turn = 1  # Counts the number of plays
        
        # Iterates until a winner is detected or until 
        # +there are no plays left.
        while (not self.look_for_winner()) and (turn < 10):
            
            # Set the number of the player, starting with 1.
            if change:
                player = 1
                
            else:
                player = 2
            
            x = int(raw_input("Enter with the X coordinate for \
player %d (1-3): " % player))
            y = int(raw_input("Enter with the Y coordinate for \
player %d (1-3): " % player))
            
            # Check the values of coordinates
            if not ((0 < x < 4) and (0 < y < 4)):
                print "X & Y coordinates MUST be between 1 and 3!"
                continue
            
            check = self.set_item(x, y, player)
            
            if check:
                print "You can't play in this coordinate. Choose another."
                continue
            
            change = not change  # Change player
            self.print_board()
            turn += 1
        
        # Game over. Prints appropriate message.
        if not self.look_for_winner():
            print "Draw!"
            
        else:
            print "Player %d won! Congratulations!!!" % self.look_for_winner()


# Main
ttt = TicTacToe()
ttt.play()