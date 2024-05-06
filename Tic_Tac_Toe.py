class Game():

    def __init__(self, player):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player = player
        self.current_player = 1

    def print_board(self):
        print('+---+---+---+')
        for row in range(3):
            row_str = '|'
            for col in range(3):
                row_str += ' ' + self.board[row][col] + ' |'
            print(row_str)
            print('+---+---+---+')

    def switch_player(self):
        if self.current_player == 1:
            self.player = 'o'
            self.current_player = 2
        else:
            self.current_player = 1
            self.player = 'x'

    def move(self):
        if self.current_player == 1:
            row = int(input('Player {} enter the row number (0, 1, 2): '.format(self.current_player)))
            col = int(input('Player {} enter the col number (0, 1, 2): '.format(self.current_player)))
        else:
            row = int(input('Player {} enter the row number (0, 1, 2): '.format(self.current_player)))
            col = int(input('Player {} enter the col number (0, 1, 2): '.format(self.current_player)))

        while row not in range(3) or col not in range(3):
            print('Error, please enter a number between 0 and 2')
            row = int(input('Player {} enter the row number (0, 1, 2): '.format(self.current_player)))
            col = int(input('Player {} enter the col number (0, 1, 2): '.format(self.current_player)))
            
        if 0 <= row <= 2 and 0 <= col <= 2:
            if self.board[row][col] == ' ':
                if self.current_player == 1:
                    self.board[row][col] = self.player
                else:
                    self.board[row][col] = self.player
                self.switch_player()
            else:
                print('This cell is already occupied. Please choose another one')

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == 'x' or self.board[i][0] == self.board[i][1] == self.board[i][2] == 'o':
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] == 'x' or self.board[0][i] == self.board[1][i] == self.board[2][i] == 'o':
                return True
            elif self.board[0][0] == self.board[1][1] == self.board[2][2] == 'x' or self.board[0][0] == self.board[1][1] == self.board[2][2] == 'o':
                return True
            elif self.board[0][2] == self.board[1][1] == self.board[2][0] == 'x' or self.board[0][2] == self.board[1][1] == self.board[2][0] == 'o':
                return True
        return False
    
    def won_game(self):
        return self.check_win() 

def game():
    print('---------------------------RULES---------------------------\n'
        'The game is played on a grid that\'s 3 squares by 3 squares. \n'
        'You are "x" , your friend is "o" . Players take turns putting their marks in empty squares. \n'
        'The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n'
        'When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n'
        '-------------------------GOOD LUCK-------------------------')
    while True:    
        n = 9
        x = Game('x')
        while n > 0:
            n -= 1
            x.print_board()
            x.move()
            if x.won_game() == True:
                x.print_board()
                print('Player {} wins. Congratulations!!!'.format(x.current_player))
                break
            elif n == 1:
                x.print_board()
                print('It\'s a tie. :(')
                break

        play_again = input('Do you want to play again? (yes/no): ')
        if play_again.lower() not in ['yes', 'y', 'ye']:
            break
        
if __name__ == '__main__':
    game()
    
    
    