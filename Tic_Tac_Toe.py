class Game():
    
    def __init__(self, player1, player2):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player1 = player1
        self.player2 = player2
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
            self.current_player = 2
        else:
            self.current_player = 1

    def move(self):
        while True:
            row = int(input('Enter the row number (0, 1, 2): '))
            col = int(input('Enter the col number (0, 1, 2): '))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if self.board[row][col] == ' ':
                    if self.current_player == 1:
                        self.board[row][col] = self.player1
                    else:
                        self.board[row][col] = self.player2
                    self.switch_player()
                    self.print_board()
            else:
                print('This cell is already occupied. Please choose another one')
        

if __name__ == '__main__':
    x = Game('x', 'o')
  
    x.print_board()
    x.move()
    
    
    