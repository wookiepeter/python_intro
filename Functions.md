- Code blocks you can define and then call from elsewhere in your program
	- Kitchen analogy: another recipe you can jump to and cook before going back to your main recipe potentially using the product from that other recipe
- Defining a function
	- use keyword 'def' to start defining a function
	- function name
	- () - brackets containing a list of parameters (values or variables) (can be empty) that should be provided to the function separated by ','
	- ':' and indentation to start the code block
	- variables defined in the function are not available outside of it
	- BUT you can use the keyword 'return' to return a value from your function and use it in your program
		- if a function returns a value you can use it in other function or assignments directly
		- a function can have multiple return statemens 
		- a return statement works similar to the break statement in loops -> no other statements in that function will be executed anymore
- Calling a function
	- To call a function you simply use the name of the function followed by normal brackets '()' -> function_name()
	- if the function has arguments, those must be provided in the brackets, several arguments are again separated by a ','
```python
def print_apple(): 
	# start of function
	print("Apple")
	# end of function

def say_name(name):
	print("my name is: " + name)

# you can define multiple parameters or 
def say_three_words(word_1, word_2, word_3): 
	print(word_1)
	print(word_2)
	print(word_3)

def give_higher_number(number): 
	higher_number = number + 1
	# use the return keyword to return some result to the caller
	return higher_number

# multiple returns
def pick_higher_number(number_1, number_2):
	if number_1 > number_2: 
		return number_1
	else: 
		return number_2

some_name = "Frodo"
other_name = "Sam"
say_name(some_name)
# you can provide values directly as arguments
say_name("Gandalf")
say_three_words("Hello", "Mr.", other_name)
number = give_higher_number(12)
print(number)
print(give_higher_number(15))
print(pick_higher_number(15, 13))
```