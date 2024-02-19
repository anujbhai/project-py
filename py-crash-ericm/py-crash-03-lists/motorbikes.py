motorbikes = ['honda', 'triumph', 'ducati']
print(motorbikes)

# change an item
motorbikes[0] = 'yamaha'
print(motorbikes)

# add an item to the end of the list
motorbikes.append('honda')
print(motorbikes)

# insert an item to any desired position
# (moves every other items one space to the left)
motorbikes.insert(0, 'enfield')
print(motorbikes)

# remove an item
del motorbikes[1]
print(motorbikes)

# removing item with 'pop()' method
# (returns popped item)
last_owned =  motorbikes.pop()
motorbikes.append(last_owned)
print(motorbikes)
print(f'The last motorbike I owned was a {last_owned.title()}')

# remove item by value
expensive = 'ducati'
motorbikes.remove(expensive)
print(motorbikes)
print(f'\nA {expensive.title()} is too expensive for me.')
