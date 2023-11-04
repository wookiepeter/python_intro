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