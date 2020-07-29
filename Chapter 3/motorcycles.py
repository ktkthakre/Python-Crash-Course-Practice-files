motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

#replacing one with other

motorcycles[0] = 'ducati'
print(motorcycles)

#appending list or adding an element to the end of the list

motorcycles.append('aprilia')
print(motorcycles)

#using insert() method

motorcycles.insert(0, 'harley')
print(motorcycles)

#remving elements
#using 'del' statement

del motorcycles[0]
print(motorcycles)
#harley was deleted

#using pop() method

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.pop()
#last element was popped
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
#saving popped element in a variable and using it later
print(popped_motorcycles)

#popping from any position

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycles)

#removing using remove() method

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)

