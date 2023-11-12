## Classes
Classes are a way for programmers to organize code into objects they can interact with. In a way classes are a way to create our own Types!

A good example of this would be a Vector in the [Thor task](https://www.codingame.com/ide/puzzle/power-of-thor-episode-1) we tracked positions using separate x and y values. We had to update their variables separately, we had to print them separately, etc. Wouldn't it be nice if instead we could just create an Object that had both those values and also provided us with the ability to also do some specific math operation with it?! That's exactly what classes are for. 


Classes (can) have: 
- properties (these are variables)
- methods (these are functions)
- constructors (a way to create an object of this class -> we will talk about those once we write our own classes!)

Simple example of how you can use the Vector2 class in gdscript
- To use a class property use: "variable_of_class.some_property"
- To use a class function use: "variable_of_class.some_method"
```gdscript
# Called when the node enters the scene tree for the first time.
func _ready():
	var vec = Vector2.ZERO
	
	print(vec)

	# here we interact with the properties (variables) of the Vector2 class
	vec.x = 1
	vec.y = 3
	
	print(vec)

	# here we interact with the methods (functions) of the Vector2 class
	print(vec.length())
	
	vec = vec.move_toward(Vector2.ZERO, 1.5)
	
	print(vec)
```
## Objects
Objects are Instances of classes. Similar to the basic types you can create separate instances of a single class, save them to variables and interact with them separately. They will keep track of their own individual properties for you and all share the common functions they have.
