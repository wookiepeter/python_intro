## Nodes
Nodes are the fundamental building blocks of your game. They perform a variety of different functions and you can structure them in a tree to create complex objects. 

Nodes have
- a name
- editable properties
- can be extended (to have more functions)
- can be added to another node as a child
- __can receive callback from the engine for specific things__
	- for example when the object is first created in the game ("\_ready") or before each frame (\_process)
	- This is where we use code to make the nodes do exactly what we want!

Godot has builtin nodes for a lot of different things like: 
- Drawing a sprite
- Creating / Detecting Collision
- Playing a sound
- Navigation

![Node Tree](./assets/node_tree.png)

## Scenes
A scene is composed of a group of nodes organized hierarchically (in tree fashion). 

A Scene
- always has one root node
- can be saved to disk and loaded back
- can be _instanced_ (more on that later)

Scenes are for
- Creating gameplay sections like a full level
- Creating coherent objects in that level
	- For example the trap scene will have several nodes (Collider, Animation, Sound)
	- that trap scene can be reused freely in the this or other levels (instead of manually building the same tree of nodes every time we need a trap somewhere)
## Resources 
- Resources are **data containers**
- They don't do anything on their own
- Nodes use the data contained in resources
