class Game():
    
    def __init__(self, symbol):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.symbol = symbol
        # self.player2 = 'o'

    def print_board(self):
        print('+----+----+----+')
        for row in range(3):
            row_str = '|'
            for col in range(3):
                row_str += '  ' + self.board[row][col] + ' |'
            print(row_str)
            print('+----+----+----+')

    def move(self):
        row = int(input('Enter the row number (0, 1, 2): '))
        col = int(input('Enter the col number (0, 1, 2): '))

        # проверка ввода

        if 0 <= row <= 2 and 0 <= col <= 2:
            if self.board[row][col] == ' ':
                if self.symbol == 'x':
                    self.symbol == 'o'
                else:
                    self.symbol == 'x'
                self.board[row][col] == self.symbol
            else:
                print('This cell is already occupied. Please choose another one')
        self.print_board()

if __name__ == '__main__':
    x = Game('x')
  
    x.print_board()
    x.move()
    
    
    