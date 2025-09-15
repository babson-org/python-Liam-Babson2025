"""
Lab 1 – Python Basics
Author: Liam Maloney
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.
"""

# ==============================
# Part 1: Draw a Diamond
# ==============================
def draw_diamond():
    # Get valid odd number with error handling
    while True:
        try:
            height = int(input("Enter an odd number for the diamond height: "))
            # Check if odd
            if height % 2 == 0:
                print("Error: Please enter an odd number")
                continue
            # Check if positive
            if height <= 0:
                print("Error: Please enter a positive number")
                continue
            # If we get here, input is valid
            break 
        # Loop continues automatically
        except ValueError:
            print("Error: Please enter a valid number!")
    # Calculate the middle row index (this will be the widest part)
    mid = height//2
    # Create top half of the diamond
    # Loop from the middle down to 0 to create the expanding part
    for idx in range(mid, -1, -1):
        #calculate spaces before the first *
        before = " " * idx
        # calculate spaces between the two *s
        between = " " * ((mid-idx)*2-1)
        # print this if its the top point of the diamond
        if (mid-idx)*2-1 == -1:
            print(before + "*")
        # print a regular row with 2 *s
        else:
            print(before + "*" + between + "*")
    # Create bottom half of the diamond 
    # loop from 1 to the middle to make the contracting part
    for idx in range(1,mid +1):
        # Calculate spaces before the first *
        before = " " * idx
        #calculate the spaces between the two *s
        between = " " * ((mid-idx)*2-1)
        # if its the bottom point print this
        if (mid-idx)*2-1 == -1:
            print(before + "*")
        # for regular rows with two *s print this
        else:
            print(before + "*" + between + "*")

# ==============================
# Part 2: Count Letters, Words, and Sentences
# ==============================
def text_analysis():
    # ask user for a block of text
    text = input("Enter some text: ")
    # create empty variables to store amounts later
    letters = 0
    words = 0
    sentances = 0
    # search throught the characters in the block of text
    for char in text:
        # check if a character is a letter, if so add one value to letters
        if char.isalpha(): letters += 1
        # when there is punctuation, the sentace has ended, so add one value to sentances
        elif char in ('.', '!', '?'): sentances += 1
    # Count words using split
    words = len(text.split())
    # print out the total values of each of the variables
    print(f"Letters: {letters}")
    print(f"Words: {words}")       
    print(f"Sentences: {sentances}")   

# ==============================
# Part 3: Caesar Cipher – Encrypt and Decrypt
# ==============================

def caesar_cipher():
    # Get user input text
    text = input("Enter text: ")
    # Get shift value
    shift = int(input("Enter shift value (integer): "))
    # Ask user whether to encrypt or decrypt
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    # Create while loop to encrypt and decrypt in the same run
    while True:
            # Initialize result
        result = ""
        # If decrypting use negative shift but create seperate variable
        real_shift = shift
        if choice == "d":
            real_shift = -shift
            # Process each characer
        for char in text:    
            # sort only letters
            if char.isalpha():      
                # determine if upper case or lower case
                is_upper = char.isupper()                
                # convert to lower for processing
                char = char.lower()            
                # shift character through the alphabet
                shifted_pos = (ord(char) - ord('a') + real_shift) % 26             
                # convert back to character
                shifted_char = chr(shifted_pos + ord('a'))             
                # restore original case
                if is_upper:
                    shifted_char = shifted_char.upper()      
                result += shifted_char        
            # non letters stay the same
            else:
                result += char
        # Print the final result
        print("Result:", result)
        # Ask if they want to do the opposite operation on this result
        if choice == "d":
            opposite = "encrypt"
        else:
            opposite = "decrypt"  
        continue_choice = input(f"Would you like to {opposite} this result? (y/n): ").lower()
        if continue_choice == "y":  
            # Use the result as new input and do opposite operation
            text = result
            if choice == "d":
                choice = "e"  # Switch to encrypt
            else:
                choice = "d"  # Switch to decrypt 
            # Continue the loop with the new values
        else:
            print("Goodbye!")
            break  # Exit the loop

# ==============================
# Main Program
# ==============================
def main():
    print("Lab 1 - Python Basics")
    print("1. Draw Diamond")
    print("2. Text Analysis")
    print("3. Caesar Cipher")
    choice = input("Select part to run (1-3): ")
    
    if choice == "1":
        draw_diamond()
    elif choice == "2":
        text_analysis()
    elif choice == "3":
        caesar_cipher()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
