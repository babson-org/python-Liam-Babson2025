def player_move(board: list[int], score: dict[str, int]):
    """
        Prompts the player to choose a valid move.
        Remember score is a dictionary from play_game()
        It has two keys 'player' and 'ai' associated values
        are 10 and -10 depending on who goes first.
    """
    
    prompt = "Select an empty cell (1-9): "
    while True:
        try:
            # Get input and convert to integer
            move = int(input(prompt))
            
            # Validate move is in range (1-9)
            if move < 1 or move > 9:
                prompt = "Out of range. Try again (1-9): "
                continue
            
            # Convert to board index (1-9 becomes 0-8)
            index = move - 1
            
            # Check if the cell is available (not already taken)
            if abs(board[index]) == 10:
                prompt = "Cell already taken. Try again (1-9): "
                continue
            
            # Valid move found - break out of loop
            break
            
        except ValueError:
            prompt = "Invalid input. Try again (1-9): "
    
    # Assign the player's score to the selected cell
    # Remember: move is 1-9, but board index is 0-8
    board[index] = score['player']