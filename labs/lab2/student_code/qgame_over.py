from calc_score import calc_score


def game_over(board: list[int]):
    """
        After every move (see play_game) we check to see if the game 
        is over.  The game is over if calc_score() returns 30 or -30
        or if there are no open moves left on the board
        Returns True if the game has a winner or no remaining moves, False otherwise.
    """

    # Check if someone has won (score is 30 or -30)
    score = calc_score(board)
    if score == 30 or score == -30:
        return True
    
    # Check if all cells are filled (no moves left)
    for cell in board:
        if abs(cell) != 10:
            # Found an open cell (value is 1-9, not ±10)
            return False
    
    # All cells filled and no winner = tie game (also game over)
    return True