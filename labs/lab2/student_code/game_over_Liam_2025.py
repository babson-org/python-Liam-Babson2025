from calc_score import calc_score


def game_over(board: list[int]):
    """
        After every move (see play_game) we check to see if the game 
        is over. The game is over if calc_score() returns 30 or -30
        or if there are no open moves left on the board
        Returns True if the game has a winner or no remaining moves, False otherwise.
    """
    
    # First check if someone won the game
    score = calc_score(board)
    if score == 30 or score == -30:
        # Someone won!
        return True
    
    # Check if all cells are filled (no moves left)
    for cell in board:
        # If we find a cell that's not 10 or -10, there's still a move available
        if abs(cell) != 10:
            return False
    
    # All cells are filled and no winner, so it's a tie
    return True