class GameDisplay:

    @staticmethod
    def show(board):
        result =  " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % \
            (board.grid[0], board.grid[1], board.grid[2],
                 board.grid[3], board.grid[4], board.grid[5],
                 board.grid[6], board.grid[7], board.grid[8])
        print(result)

    @staticmethod
    def log(text):
        print(text)

    @staticmethod
    def prompt(text):
        input_value = input(text)
        return input_value

    @staticmethod
    def logAsList(array):
        print(*array, sep='\n')
