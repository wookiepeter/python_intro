## Variables
### Python
```python
name = "MyName"
number = 15
name = "OtherName"
number = 10
```
### gdscript 
```
var name = "MyName"
var number = 15
name = "OtherName"
number = 10
```
- gdscript has a keyword for "declaring" variables -> creating them for the first time in the current context / code block
## Functions
### Python
```python
def some_function(name):
	print(name)
	return 5
```
### gdscript
```gdscript
func some_function(name):
	print(name)
	return 5
```
- different keyword for declaring a function -> __func__
- gdscript also has a new keyword called pass which simply does nothing
	- this is so the engine can generate empty functions (for you to implement later) without error messages
- function don't need to be defined before they are called
