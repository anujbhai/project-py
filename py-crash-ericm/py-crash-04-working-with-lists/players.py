players = ['charles', 'martina', 'michael', 'florence', 'eli']

# slice [index:count]
print(players[0:3])

# slice starting from beginning
print('\nHere are the first three players in my team:')
for player in players[:3]:
  print(player.title())

# slice starting from provided index
# upto the end of list
print(players[2:])

# slice last 3 items
print(players[-3:])
