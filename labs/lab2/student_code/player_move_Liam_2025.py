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
             # Get input directly
            move = int(input("Select an empty cell (1-9): "))
            
            # Check if move is in valid range (1-9)
            if move < 1 or move > 9:
                print("Invalid. Try again with an empty cell index (1-9): ", end='')
                continue
            
            # Convert from 1-9 to index 0-8
            index = move - 1
            
            # Check if this cell is already taken
            if abs(board[index]) == 10:
                print("Invalid. Try again with an empty cell index (1-9): ", end='')
                continue
            
            # Valid move found - break out of loop
            break
            
        except ValueError:
            prompt = "Invalid input. Try again (1-9): "
    
    # Assign the player's score to the selected cell
    # Remember: move is 1-9, but board index is 0-8
    board[index] = score['player']