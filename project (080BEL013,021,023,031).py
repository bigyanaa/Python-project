# Tic-Tac-Toe Game Implementation

class TicTacToe:
    def __init__(self):
        """
        Constructor to initialize the game state.
        - The board is a list of 9 empty spaces (represented by ' ').
        - current_winner keeps track of the winner (either 'X' or 'O') or remains None if no one has won yet.
        """
        self.board = [' ' for _ in range(9)]  # Initialize the board as a list of 9 empty spaces.
        self.current_winner = None  # No winner at the beginning of the game.

    def print_board(self):
        """
        This method prints the current state of the board in a 3x3 format.
        It slices the board list into rows and formats them with '|' characters for readability.
        """
        # Iterating through each row to print the board.
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            # Join the row elements with '|' and print them.
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        """
        This method returns a list of available moves.
        It checks for all the indexes in the board list where the value is ' ' (empty).
        
        Returns:
            A list of indices (0-8) that are still available for a move.
        """
        # Using list comprehension to find all empty spots on the board.
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        """
        This method checks if there are any empty squares left on the board.
        
        Returns:
            True if there is at least one empty square, otherwise False.
        """
        return ' ' in self.board  # Check if there's at least one ' ' on the board.

    def make_move(self, square, letter):
        """
        This method allows a player to make a move.
        
        Args:
            square (int): The index on the board where the player wants to make a move.
            letter (str): The player's letter ('X' or 'O').
        
        Returns:
            True if the move is valid and successful, False otherwise.
        """
        # Check if the chosen square is empty.
        if self.board[square] == ' ':
            # Place the player's letter ('X' or 'O') in the chosen square.
            self.board[square] = letter
            
            # Check if the move resulted in a win.
            if self.winner(square, letter):
                self.current_winner = letter  # Update the winner if the current player has won.
            
            return True  # Move was successful.
        return False  # Invalid move (square already taken).

    def winner(self, square, letter):
        """
        This method checks if the last move made by the player resulted in a win.
        A player wins if they have three of their letters in a row, column, or diagonal.
        
        Args:
            square (int): The index on the board where the last move was made.
            letter (str): The player's letter ('X' or 'O').
        
        Returns:
            True if the player has won, False otherwise.
        """
        # Check row victory
        row_ind = square // 3  # Determine which row the square is in.
        row = self.board[row_ind * 3:(row_ind + 1) * 3]  # Get the full row.
        if all([spot == letter for spot in row]):  # Check if all spots in the row are the same letter.
            return True  # Player has won through a row.

        # Check column victory
        col_ind = square % 3  # Determine which column the square is in.
        column = [self.board[col_ind + i * 3] for i in range(3)]  # Get the full column.
        if all([spot == letter for spot in column]):  # Check if all spots in the column are the same letter.
            return True  # Player has won through a column.

        # Check diagonal victory (diagonals only possible on even-numbered squares: 0, 2, 4, 6, 8)
        if square % 2 == 0:  # Only even-numbered squares can be part of a diagonal.
            # Check the first diagonal (from top-left to bottom-right).
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Indices of the first diagonal.
            if all([spot == letter for spot in diagonal1]):  # Check if all spots in the diagonal are the same letter.
                return True  # Player has won through the first diagonal.

            # Check the second diagonal (from top-right to bottom-left).
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Indices of the second diagonal.
            if all([spot == letter for spot in diagonal2]):  # Check if all spots in this diagonal are the same letter.
                return True  # Player has won through the second diagonal.
        
        # If none of the above conditions are met, the player hasn't won yet.
        return False

def play_game():
    """
    This function controls the flow of the game.
    It alternates turns between two players ('X' and 'O') until there's a winner or the game ends in a tie.
    """
    game = TicTacToe()  # Create a new instance of the TicTacToe class.
    game.print_board()  # Print the initial empty board.

    letter = 'X'  # Player 'X' always starts first.
    
    # Continue the game as long as there are empty squares.
    while game.empty_squares():
        # Prompt the current player to choose a square (0-8).
        square = int(input(f"{letter}'s turn. Input move (0-8): "))
        
        # Attempt to make the move. If it's valid, update the board.
        if game.make_move(square, letter):
            game.print_board()  # Print the updated board after the move.
            
            # If there's a winner after the move, announce the winner and stop the game.
            if game.current_winner:
                print(f"{letter} wins!")  # Announce the winner.
                return  # Exit the function (end the game).
            
            # Switch players: If the current player is 'X', switch to 'O'; otherwise, switch to 'X'.
            letter = 'O' if letter == 'X' else 'X'
        else:
            # If the move is invalid (e.g., the square is already taken), prompt the player to try again.
            print("Invalid move. Try again.")

    # If the loop ends and there's no winner, it means the game is a tie.
    print("It's a tie!")  # Announce the tie.

# Example usage: Start the game.
play_game()  # Calls the function to begin the game.