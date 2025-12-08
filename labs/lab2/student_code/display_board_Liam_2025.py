from student_repo.labs.lab2.student_code.utils_Liam_2025 import clear_screen

def print_board(board: list[int]):
    """
        Display the Tic-Tac-Toe board with human-friendly layout.
        Remember the board may look like:
        [10, 2, 3, 4, -10, 6, 7, 8, 10] after 3 moves and print_board
        
        should display:
        
           |   |   
         X | 2 | 3 
           |   |   
        -----------
           |   |   
         4 | O | 6 
           |   |   
        -----------
           |   |   
         7 | 8 | X 
           |   |   
    """
    
    def cell(value: int) -> str:
        # If the value is 10, that's an X
        if value == 10:
            return 'X'
        # If the value is -10, that's an O
        elif value == -10:
            return 'O'
        # Otherwise, show the number (1-9)
        else:
            return str(value)
    
    # Clear the screen before drawing
    clear_screen()
    print()
    
    # Loop through each of the 3 rows
    for row in range(3):
        # For this row, get the 3 cells that belong to it
        row_values = []
        for col in range(3):
            # Calculate which board index this is
            index = row * 3 + col
            # Get what should be displayed for this cell
            row_values.append(cell(board[index]))
        
        # Print the row with the board layout
        print('   |   |   ')
        print(f' {row_values[0]} | {row_values[1]} | {row_values[2]} ')
        print('   |   |   ')
        
        # Print separator line between rows (but not after last row)
        if row < 2:
            print('--------c--')
    
    print()