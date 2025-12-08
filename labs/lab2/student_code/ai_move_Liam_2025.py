def ai_move(board: list[int]):
    """
        Simple AI that selects the first available cell.
        Remember board is a list that starts with items 1 - 9
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        after two moves with X choosing 1 and O choosing 5 the board looks like:
        [10, 2, 3, 4, -10, 6, 7, 8, 9]
        
        so in this case your function should return 1 (the index of cell 2)
    """
    # Loop through each cell in the board
    for i in range(len(board)):
        # Get the value at this position
        cell = board[i]
        # Check if this cell is available (not 10 or -10)
        if abs(cell) != 10:
            # Return the index of this available cell
            return i