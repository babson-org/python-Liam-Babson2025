
'''
Liam, I really liked what you did with this lab.  Highest Grade in class.

Grade A+ (for adding that enhancement at the end of caesar)

Would like to see more thought going into what you write about
computational thinking for each problem.  I want to understand 
how your thinking lead to the solution.

so for the diamond problem where does height // 2 come from?
how did you determine the ranges() for the two loops?

'''
"""
Lab 1 – Python Basics
Author: Liam Maloney
Instructions: Complete each part below. Save your work and commit + sync in Codespaces.
"""

# ==============================
# Part 1: Draw a Diamond
# ==============================
'''
In this function i am using a formula to calculate the amount of spaces before the first * 
and between the two *s if we are not at the top or bottom of the diamond. first i use error handling
to make sure that the user enters a odd and positive integer, otherwise the program will not work. 
then i use floor division to find the width of the middle row, and to create a number that we use in
the formual to calculate the distance before and between the *s. to calculate the top of the diamond 
we start from the middle width and move down to -1 in order to create the expanding effect. for the 
bottom part of the diamond we do the oppostite and move up from from 1 to the widest width +1.
'''
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
'''
in this function i am asking the user for a block of text then creating variables for
letters, words, and sentances to store values for later. then i use a for loop to search
through each character in the text and use .isalpha() to count the letters. to count the sentances
i assume that every sentance has punctuation and because of that i add a sentance if there is a
punctuation. for words i use the .split function to seperate the words and then count the length, 
all of these counts are stored by using += 1 and adding to the original variables we created and then
printed out at the end.   
'''
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
'''
In this program i am going to be asking the user for 3 inputs of text, 
shift value and to encrypt or decrypt. then i will be going through each 
character in the text and assigning a value to each character using the ord function.
Then i will set each character to the first position by subracting "a" and then adding
the shift value in order to encrypt the text. i aslo saved any uppercase letters in a boolean 
so that once the text is encrypted i can keep the capitalized letters uppercase,
the program will then print out the encrypted text and if the user wants to decrypt
they will enter "d" and the program will run again but this time it makes the shift value
negative so the character values reverse back to the original position. then the code repeats.
'''
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
    while True:
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
