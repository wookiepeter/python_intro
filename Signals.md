Signals allow a node to send out a "message" that other nodes can listen for and respond to. This is great for making code more organized, since we can keep the different functionality in separated nodes and reuse the already existing Nodes / Signals.  

## Signals
- Are emitted from a Sender!
- Can be listened to (connected to) by zero, one or even several Receivers
- You connect Signal to a specific function in the receiver 
	- These can be automatically created in the Node-UI or manually written and then selected
- Functions connected to Signals are executed immediately after the signal was  emitted 
	- i.e. our computer jumps to that spot, executes the function, and then jumps back to wherever he was before

## Code examples
```gdscript  
# defining a signal 
signal hit

func _ready(): 
	# emitting a signal
	hit.emit()
	# or 
	emit_signal("hit")

# potential function receiving the hit signal -> should probablybe in another node
func _on_hit(): 
	# do stuff here!
	pass

func _some_other_func(obj): 
	# connecting to a signal via code
	# connect method needs to be called on the sender object
	# 1st parameter: signal that should be connected
	# 2nd parameter: node that should listen to the signal
	# 3rd parameter: function in that node that should be connected 
	self.connect(hit, obj, _on_hit)
```

## Signals with parameters / values 
Just like functions signals can also have parameters. The Sender must define these and any receiving function should handle them appropriately!

```gdscript
# signal with 2 parameters
signal my_signal(value, other_value)

func _ready():
	# emitting a signal with 2 parameters
    emit_signal("my_signal", true, 42)
    # emitting  signal with 2 parameters
    my_signal.emit(true, 42)
```