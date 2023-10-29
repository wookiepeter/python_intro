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
## for loop 
- iterates over a collection of things and executes a codeblock for each one
	- this also introduces collections but don't worry about those for now!
```python
for i in [1, 2, 3, 4, 5]:
	print(i)
# range is a function that returns a sequence (list) of numbers over which you can iterate!
for i in range(5)
	print(i)
# this is a different variant of that function with the following signature: range(start, stop, step)
for i in range(10, 20, 2)
	print(i)
```
- range is a special function that generates a sequence of numbers 
	- signature: range(start, stop, step)
		- start: number where we should start our sequence
		- stop: number where we should end our sequence
		- step: amount we should add during each step