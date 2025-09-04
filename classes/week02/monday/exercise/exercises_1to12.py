from classes.week00.second_class.utils import clear_screen
'''
# 1

Write down the steps a program would need to make a cup of tea. Then implement a Python 
function make_tea() that prints each step.
'''
# enter your code here
Step1 = "boil water"
step2 = "put tea bag in water"
step3 = "let tea steep"
step4 ="drink tea"
def make_tea():
    input("do you want to make tea, Yes or No?")
    if input.lower == "Yes":
        print(Step1,step2,step3,step4)
    else:
        print("No tea for you")
        


pause=input('pause')
clear_screen()
'''
#2

Given a list [2, 4, 6, 8, 10], write a program that prints the next three numbers in the list.  
(the ones after 10)
'''
# enter your code here
numbers = [2, 4, 6, 8, 10]
difference = numbers[1] - numbers[0]
lastnumber = numbers[-1]
print("the next three numbers are:")
for i in range(1, 4):
    nextnumber = lastnumber + (difference * i)
    print(nextnumber)





pause=input('pause')
clear_screen()


'''
#3

Write a program that asks the user for their first and last name, then prints a greeting:
"Hello, <first name> <last name>!"
'''
# enter your code here
def greeting():
    firstname =input("enter your first name: ")
    lastname = input("enter your last name:")
    print("hello" + firstname " " + lastname +"nice to meet you!")

pause=input('pause')
clear_screen()
'''
#4

Write a program that prints your Python version and platform using the sys and platform modules.
'''
# enter your code here
 

pause=input('pause')
clear_screen()
'''
#5

Ask the user to input two numbers. Calculate and print their sum, difference, product, 
and division (both / and //).
'''
# enter your code here
num1 =input("type a number")
num2 =input("type another number")
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1/num2
floor = num1//num2
print("sum =" + sum)
print("difference = " + difference)
print("product = " + product)
print("quotient = " + quotient)
print("floor = " + floor)
      

pause=input('pause')
clear_screen()
'''
#6

Ask the user to input a sentence. Print it in uppercase, lowercase, with the first letter 
capitalized, and split it into words.
'''

# enter your code here
sentance = input("enter a sentance: ")
print(sentance.upper)
print(sentance.lower)
print(sentance.capitalize)
print(sentance.title)
print(sentance.split)



pause=input('pause')
clear_screen()
'''
#7

Calculate the result of the following without parentheses and then with parentheses:
10 + 2 * 5 / 2 - 3 ** 2
'''
# enter your code here
calc1= 3**2
calc2= 2*5
calc3=calc2/2
calc4=calc3-calc1
final=10+calc4
print(final)

pause=input('pause')
clear_screen()
'''
#8

Create a list of your three favorite foods. Replace the second item with a new one, 
then print the list.
'''
# enter your code here
foods = ["burger", "sushi", "steak"]
foods[1] = "pizza"
print("new list: " + foods)



pause=input('pause')
clear_screen()
'''
#9

Create a tuple with four numbers. Try to change the first number (observe the error) 
and then print the tuple.
'''
# enter your code here
list = (1,2,3,4,)
list[0] = 7
print(list)



pause=input('pause')
clear_screen()
'''
#10

Create a dictionary representing a student (name, age). Update the age. Create a list of 
favorite numbers and add a new number.
'''
# enter your code here
student ={"name":"liam", "age": 19}
student["age"] = 20
print(student)
favorite_numbers = [1,5,3,7,22]
favorite_numbers.append(43)
print(favorite_numbers)



pause=input('pause')
clear_screen()
'''
#11

Ask the user to input their favorite quote. Save it to a file quotes.txt 
and read it back to print it.
'''
# enter your code here

quote =input("enter your favorite quote: ")

with open("quotes.txt", "w") as file:
    file.write(quote)

with open("quote.txt", "r") as file:
    saved_quote =file.read()

print("\nQuote read from file")
print(saved_quote)




pause=input('pause')
clear_screen()
'''
#12
Ask the user to input 5 numbers (one at a time), store them in a list, and print the sum and average.
'''
# enter your code here
numbers =[]

for i in range(5):
    numb = float(input(f"enter number {i+1}: "))
    numbers.append(numb)

print("numbers: " + numbers)
print("total: " + total)
print("average: " + average)

pause=input('pause')
clear_screen()