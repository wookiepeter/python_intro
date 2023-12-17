# TASK 1
# Complete this function, the function signature is already provided. 
# The function is supposed to go through a list and find the number of occurances of a specific number occures in a provided list. 
# HINT: Look at this file https://github.com/wookiepeter/python_intro/blob/main/Loops.md to see how to iterate through a list! 
# Don't change the function signature, otherwise the provided tests will fail

def count_number_in_list(list, number):  
    count = 0
    for i in list: 
        if i == number: 
            count += 1

    return count

# These are some tests provided for the function -> do not remove them!
assert count_number_in_list([1, 2, 3, 4, 5, 1, 2], 1) == 2
assert count_number_in_list([], 1) == 0
assert count_number_in_list([8, 3, 5, 2, 3, 5, 6, 1, 2, 0, 0, 0, 0, 0, 1, 2, 3, 5, 0], 0) == 6

print("Task 1 Tests passed!")

# Task 2
# Complete this function, the function signature is already provided. 
# The function is supposed to compute and return the factorial of the provided number
# HINT: If you don't remember how to compute the factorial look at this link: https://de.wikipedia.org/wiki/Fakult%C3%A4t_(Mathematik)#Diskrete_Standarddefinition
def factorial(number): 
    if number == 0: 
        return 1
    result = 1
    for i in range(1, number + 1, 1): 
        result *= i
    return result


# These are some tests provided for the function -> do not remove them!
assert factorial(0) == 1
assert factorial(5) == 120
assert factorial(9) == 362880

print("Task 2 Tests passed")

# TASK 3
# Write a Python program that iterates the integers from 1 to 50. 
# For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". 
# For numbers that are multiples of three and five, print "FizzBuzz".
# HINT: Remember that you can use the modulo operator (%) to check the remainder of a division: 7 % 3 = 1

def fizzbuzz(): 
    print("Starting with FizzBuzz")
    for i in range(1, 51, 1): 
        result = ""
        if i % 3 == 0: 
            result += "Fizz"
        if i % 5 == 0: 
            result += "Buzz"
        if result == "": 
            result += str(i) 
        print(result)

fizzbuzz()




