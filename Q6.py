class TicTacToe:
    def __init__(self, board):
        """
        Initialize the Tic-Tac-Toe board.
        The board is represented as a 3x3 list of lists.
        """
        self.board = board

    def is_open_line(self, line, player, opponent):
        """
        Check if a line (row, column, or diagonal) is still open for a player.
        A line is open if it contains only the player's marks and empty spaces,
        and no marks of the opponent.
        """
        return all(cell == player or cell == ' ' for cell in line) and opponent not in line

    def calculate_heuristic(self, player, opponent):
        """
        Calculate the heuristic value of the board for the player.
        e(p) = (No. of complete rows, columns, or diagonals open for the player) -
               (No. of complete rows, columns, or diagonals open for the opponent)
        """
        open_for_player = 0
        open_for_opponent = 0

        # Check rows
        for row in self.board:
            if self.is_open_line(row, player, opponent):
                open_for_player += 1
            if self.is_open_line(row, opponent, player):
                open_for_opponent += 1

        # Check columns
        for col in range(3):
            column = [self.board[row][col] for row in range(3)]
            if self.is_open_line(column, player, opponent):
                open_for_player += 1
            if self.is_open_line(column, opponent, player):
                open_for_opponent += 1

        # Check diagonals
        diagonal1 = [self.board[i][i] for i in range(3)]  # Top-left to bottom-right
        diagonal2 = [self.board[i][2 - i] for i in range(3)]  # Top-right to bottom-left
        if self.is_open_line(diagonal1, player, opponent):
            open_for_player += 1
        if self.is_open_line(diagonal1, opponent, player):
            open_for_opponent += 1
        if self.is_open_line(diagonal2, player, opponent):
            open_for_player += 1
        if self.is_open_line(diagonal2, opponent, player):
            open_for_opponent += 1

        # Calculate heuristic
        heuristic = open_for_player - open_for_opponent
        return heuristic


# Driver Code
if __name__ == "__main__":
    # Example Tic-Tac-Toe board
    board = [
        ['X', 'O', ' '],
        [' ', 'X', ' '],
        ['O', ' ', ' ']
    ]

    # Player and opponent symbols
    player = 'X'
    opponent = 'O'

    # Initialize Tic-Tac-Toe board
    ttt = TicTacToe(board)

    # Calculate heuristic value
    heuristic_value = ttt.calculate_heuristic(player, opponent)

    # Print the board and heuristic value
    print("Tic-Tac-Toe Board:")
    for row in board:
        print(row)
    print(f"\nHeuristic Value for player '{player}': {heuristic_value}")
