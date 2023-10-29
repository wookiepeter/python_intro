- each line is a statement -> cooking instruction
- statements can consist of
	- variables: a -> bowls we can label and put stuff into
	- operators: =,+,>,<  -> actions like adding, mixing, heating, taste-testing, etc.
	- values: 15, 23, true, "text" -> measuring units)
	- keywords: if / else: () -> special instructions that determine how if / how other instructions are executed, e.g. put cake into oven, once oven reaches a specific temperature 
	- functions: print(...) -> a separate recipe that we can call to do some of the work for us, e.g. prepping a sauce
		- we can write those ourselves but we will get to that later!
	- comments: #... -> a comment scribbled in between the recipe to explain something!
```python
bowl_a = 15
cup_b = 25
oven_temperature = 183 - 33
text = "Fire in the kitchen!"

if oven_temperature > 135: 
	print(text)
else: 
	print("Everything is fine!")

print(bowl_a + cup_b)
# this is the end of the program
```