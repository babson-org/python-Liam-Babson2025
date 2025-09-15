
from classes.week00.second_class.utils import clear_screen
'''
#13 - Conditional Logic
Ask the user for a number and print whether it is positive, negative, or zero.
'''
# enter code here
num = int(input("enter a number: "))
if num == 0:
    print("Zero")
elif num <= 0:
    print("negative")
elif num >= 0:
    print ("posititve")



pause=input('pause')
clear_screen()

'''
#14 - Even/Odd Check
Ask the user for a number and print if it is even or odd.
'''
# enter code here
num1 = int(input("enter a number: "))
if num1%2 == 0:
    print("even")
else:
    print("odd")


pause=input('pause')
clear_screen()

'''
#15 - Boolean Operators
Ask the user for two numbers and check if both are positive, either is positive, or none is positive.
'''
# enter code here
txt= 'please enter a number: '
while True:
    try:
        num01 = int(input(txt))
        break
    except ValueError:
        txtm == 'a real number'
txt= 'please enter a number: '
while True:
    try:
        num02 = int(input(txt))
        break
    except ValueError:
        txtm == 'a real number'


if num01 > 0 and num02 > 0:
    print("both")
elif num01 > 0 or num02 > 0:
    print("one is positive")
else:
    print("neither")


pause=input('pause')
clear_screen()

'''
#16 - For Loop
Print all numbers from 1 to 20, skipping multiples of 3.
'''
# enter code here
for i in range(1,20):
    if i%3 == 0:
        continue
    print(i)
    


pause=input('pause')
clear_screen()

'''
#17 - While Loop
Ask the user to guess a secret number (hardcoded) until they get it right.
'''
# enter code here
secret = ("7")
while True:
    guess =input("enter your guess")
    if guess == secret:
        print("you got it")
        break
    else:
        print("try again")


pause=input('pause')
clear_screen()

'''
#18 - Break / Continue
Print numbers 1-10 but stop printing when you reach 7 and skip 3.
'''
# enter code here
for i in range(1,10):
    if i == 3:
        continue
    if i == 8:
        break
    print(i)



pause=input('pause')
clear_screen()

'''
#19 - Function Definition
Write a function square(x) that returns the square of a number and test it.
'''
# enter code here
def square(x):
    return x*x

print(square(5))





pause=input('pause')
clear_screen()

'''
#20 - Function with Mutable Argument
Write a function add_item(lst, item) that appends item to lst and observe the effect on the original list.
'''
# enter code here
list =[1,2,3,4,5]
list.append(6)
print(list)



pause=input('pause')
clear_screen()

'''
#21 - Comments / Documentation
Write a function greet(name) with single-line and multi-line comments explaining each step.
'''
# enter code here



pause=input('pause')
clear_screen()

'''
#22 - Combining Tools
Ask the user to enter 5 names. Store them in a list, capitalize each name, sort the list, and print it.
'''
# enter code here



pause=input('pause')
clear_screen()

