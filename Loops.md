* Code block that is repeated several times depending on a condition
## Code block
- Block of cooking instructions
- Distinct section of code that only runs under certain circumstances 
- We've already been using these in if-statements
- in python they are distinguished with tabs (indentation -> Einzug)
		- all lines that follow are grouped together and have the same indentation form a code block
```python
if True: 
	print("stuff")
	print("otherstuff")
# codeblock ended here!
```
## while loop 
- Repeats a set of instructions until some condition is met
```python
while True: 
	print("Not Doing this forever")
	break
number = 0
while number < 5: 
	print(number)
	number += 1
```
- while in a loop the 'break' keyword can be used to exit said loop and continue with the remaining program instead
	- this is very often done with some sort of if statement!
 * while in a loop the 'continue' keyword can be used to immediately jump to the start of the next iteration of that loop
	 * again often used with some sort of if statement
## for loop 
- iterates over a collection of things and executes a codeblock for each one
	- this also introduces collections but don't worry about those for now!
	- that collection can also be stored in a separate value and can contain stuff other than numbers (for example strings)
```python
for i in [1, 2, 3, 4, 5]:
	print(i)
string_list = ["item 1", "item 2", "otherstuff", "some_name"]
for i in string_list: 
	print(i)
# range is a function that returns a sequence (list) of numbers over which you can iterate!
for i in range(5):
	print(i)
# this is a different variant of that function with the following signature: range(start, stop, step)
for i in range(10, 20, 2):
	print(i)
```
- range is a special function that generates a sequence of numbers 
	- signature: range(start, stop, step)
		- start: number where we should start our sequence
		- stop: number where we should end our sequence
		- step: amount we should add during each step
