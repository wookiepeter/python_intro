# Task 1
# create 2 variables and use them to read 2 integer values from input, then add them and print the result if it's larger than 20 and a message otherwise

number_a = int(input())
number_b = int(input())

result = number_a + number_b
if result > 20: 
    print("The result is: " + str(result))
else: 
    print("Too small")

# Task 2
# Use a loop to add all the numbers from 1 to 10 and print the result.
sum = 0
for i in range(11): 
    sum += i
print("The sum is: " + str(sum))