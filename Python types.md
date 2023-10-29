## Types 
- Values can have different types: 
- The 4 basic types are: 
	- int -> Integer (a whole number or a number that is not a fraction)
		-  e.g. 5 or -3
	- float -> Floating point number (a number that is a fraction)
		- e.g. 1.25 or -0.00024101
	- String -> a set of characters that are stored and used together
		- can contain special characters like '\n' or '\t' to mark linebreaks or tabstops
	- bool -> a value to determine logic
		- only has 2 possible values 
			- True or False
		- used in to control the flow of programs (within if or while)
		- can be determined with comparison operators (e.g. 5 > 15 results in False)
- These types can be turned into others using the following functions
	- use str() to convert the other 3 types to string
	- use int() to convert float or string to an integer
	- use float() to convert int or string to a float
	- converting other types to bool will have unexpected results for inexperienced programmers
```python
whole_number = 1
float_number = 1.25
print(whole_number + float_number)
# float_number is turned into an integer and it's remainder is ignored!
print(whole_number + int(float_number))

some_string = "hello number"
print(some_string + ": " + str(whole_number))

some_bool = True
print(some_bool)
some_bool = 15 < 5
print("Should be negative: " + str(some_bool))
```