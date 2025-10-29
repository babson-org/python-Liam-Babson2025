def calc_score(board: list[int]):
    """
        Determines if there's a winner on the board.
        Returns 30 if X wins, -30 if O wins, 0 otherwise.
         
        there are 8 ways to win: 3 rows, 3 columns, 2 diagnols
        if the cells in a row, column or diagnol add up to 30 return 30
        if they add upto -30 return -30
        else return 0
    """
     
    def line_sum(a, b, c):
        '''
            line_sum takes 3 numbers and if the sum is either 30
            or -30 returns that sum otherwise do not return
        '''         
        # Sum the three board positions
        total = board[a] + board[b] + board[c]
        
        # If sum is 30 (X wins) or -30 (O wins), return it
        if total == 30 or total == -30:
            return total
        # Otherwise, don't return anything (returns None implicitly)
     
    # Check all 8 winning combinations
    
    # Check the 3 rows
    result = line_sum(0, 1, 2)  # Top row
    if result: return result
    
    result = line_sum(3, 4, 5)  # Middle row
    if result: return result
    
    result = line_sum(6, 7, 8)  # Bottom row
    if result: return result
    
    # Check the 3 columns
    result = line_sum(0, 3, 6)  # Left column
    if result: return result
    
    result = line_sum(1, 4, 7)  # Middle column
    if result: return result
    
    result = line_sum(2, 5, 8)  # Right column
    if result: return result
    
    # Check the 2 diagonals
    result = line_sum(0, 4, 8)  # Top-left to bottom-right
    if result: return result
    
    result = line_sum(2, 4, 6)  # Top-right to bottom-left
    if result: return result
    
    # No winner found, return 0 (tie or game still in progress)
    return 0