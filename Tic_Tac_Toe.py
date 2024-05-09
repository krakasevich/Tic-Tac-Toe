class Game_Board:

    def __init__(self):
        '''
        Initialize a new instance of the Game_Board class.

        The game board is represented as a 2D list of 3x3 cells.
        Each cell is initially empty, represented by a space (' ').

        Parameters:
        None

        Returns:
        None
        '''

        self.board = [[' ' for j in range(3)] for i in range(3)]

    def print_board(self):
        '''
        Prints the current state of the game board.
        
        The game board is represented as a 3x3 grid, where each cell can contain
        either an empty space (' '), 'x', or 'o'.
        
        Parameters:
        None
        
        Returns:
        None
        '''

        print('+---+---+---+')
        for row in range(3):
            row_str = '|'
            for col in range(3):
                row_str += ' ' + self.board[row][col] + ' |'
            print(row_str)
            print('+---+---+---+')

    def check_win(self):
        '''
        Checks if a player has won the game.

        The function iterates over the game board to check if any player has three marks in a row,
        either horizontally, vertically, or diagonally.

        Parameters:
        None

        Returns:
        bool: True if a player has won, otherwise False
        '''

        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == 'x' or \
                self.board[i][0] == self.board[i][1] == self.board[i][2] == 'o':
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] == 'x' or \
                self.board[0][i] == self.board[1][i] == self.board[2][i] == 'o':
                return True
            
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 'x' or \
            self.board[0][0] == self.board[1][1] == self.board[2][2] == 'o':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == 'x' or \
            self.board[0][2] == self.board[1][1] == self.board[2][0] == 'o':
            return True

        return False
    
    def won_game(self):
        '''
        Checks if the game has been won by any player.

        This method calls the `check_win` method to determine if a player has three marks in a row,
        either horizontally, vertically, or diagonally.

        Parameters:
        None

        Returns:
        bool: True if a player has won, otherwise False.
        '''

        return self.check_win() 

class Player:

    def __init__(self, player, game_board):
        '''
        Initialize a new Player instance.

        Parameters:
        player (str): The symbol ('x' or 'o') representing the player.
        game_board (Game_Board): The game board instance to which the player belongs.

        Returns:
        None
        '''

        self.game_board = game_board
        self.player = player 
        self.current_player = 1
        
    def move(self):
        '''
        This method allows a player to make a move on the game board.

        The player is prompted to enter the row and column numbers for their move.
        If the entered row and column are within the valid range (0-2) and the cell is empty,
        the player's symbol ('x' or 'o') is placed in the cell, and the player's turn is switched.
        If the entered row and column are not within the valid range or the cell is already occupied,
        an error message is displayed, and the player is prompted to enter a new row and column.

        Parameters:
        None

        Returns:
        None
        '''

        row = int(input('Player {} enter the row number (0, 1, 2): '.format(self.current_player)))
        col = int(input('Player {} enter the col number (0, 1, 2): '.format(self.current_player)))
        
        while row not in range(3) or col not in range(3):
            print('Error, please enter a number between 0 and 2')
            row = int(input('Player {} enter the row number (0, 1, 2): '.format(self.current_player)))
            col = int(input('Player {} enter the col number (0, 1, 2): '.format(self.current_player)))
            
        if 0 <= row <= 2 and 0 <= col <= 2:
            if self.game_board.board[row][col] == ' ':
                self.game_board.board[row][col] = self.player
                self.switch_player()
            else:
                print('This cell is already occupied. Please choose another one')

    def switch_player(self):
        ''' 
        Switches the current player from 'x' to 'o' or vice versa.

        This method is called after each player's move. It updates the 'player' and 'current_player' attributes
        to reflect the turn of the next player.

        Parameters:
        None

        Returns:
        None
        '''

        if self.current_player == 1:
            self.player = 'o'
            self.current_player = 2
        else:
            self.current_player = 1
            self.player = 'x'

def game():
    '''
    This function starts a game of Tic Tac Toe. It prints the rules, initializes the game board,
    and allows two players to take turns making moves. The game continues until a player wins or
    all squares are filled, at which point the game ends. The function also prompts the user to
    play again.

    Parameters:
    None

    Returns:
    None
    '''

    print('---------------------------RULES---------------------------\n'
        'The game is played on a grid that\'s 3 squares by 3 squares. \n'
        'You are "x" - 1 , your friend is "o" = 2. Players take turns putting their marks in empty squares. \n'
        'The first player to get 3 of her marks in a row (horizontally, vertically, or diagonally) is the winner.\n'
        'When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n'
        '-------------------------GOOD LUCK-------------------------')
    game_board = Game_Board()
    while True:
        num_of_moves = 9
        play = Player('x', game_board)
        while num_of_moves >= 0:
            num_of_moves -= 1
            game_board.print_board()
            play.move()
            if game_board.won_game():
                game_board.print_board()
                print('Player {} wins. Congratulations!!!'.format(1 if play.current_player == 2 else 2))
                break
            elif num_of_moves == 0:
                game_board.print_board()
                print('It\'s a tie. :(')
                break

        play_again = input('Do you want to play again? (yes/no): ')
        if play_again.lower() in ['yes', 'y', 'ye']:
            game_board = Game_Board()
            continue
        else:
            break
        
if __name__ == '__main__':
    game()