some_sequence = [1, 2, 3, 5, "Word1", "Word2"]
some_other_sequence = [2, 3, 5]

### Immutable sequence operations
# use 'in' or 'not in' to test if some element is in a sequence or not
if 1 in some_sequence: 
	print("This should print!")
	
if 4 not in some_sequence: 
	print("This should also print")	
# use len(sequence) to return the number of elements in a sequence
print("Length of the sequence: " + str(len(some_sequence)))

# use sequence[index] to access an element from a sequence
print("item at position 2 of that sequence" + str(some_sequence[2]))
some_number = some_sequence[0] + some_other_sequence[2]

### Mutable sequence operations
# you can modify an element in the sequence
some_sequence [0] = 5
some_sequence [2] += 2

# adds an element to the list
some_sequence.append(1.25)
some_sequence.append([2, 3])
# removes the first occurance of an element from the list
some_sequence.remove("Word1")

print(some_sequence)

# adds a sequence to the list
some_sequence.extend([4, 5])
# reverses the list
some_sequence.reverse()

print(some_sequence)

# Sorts this list
some_other_sequence.sort()
# This would fail because sorting is only supported for lists with only 1 type
# some_sequence.sort()

print(some_other_sequence)