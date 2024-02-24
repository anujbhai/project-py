pizzas = ['margharita', 'pepperoni', 'supreme']
friends_pizzas = pizzas[:]

pizzas.append('farmhouse')
friends_pizzas.append('free')

for pizza in pizzas:
  print(f'I like {pizza.title()} pizza.')

for f_pizza in friends_pizzas:
  print(f'Friend likes {f_pizza.title()} pizza.')

print('\nI really love pizza.')

animals = ['pig', 'goat', 'chicken']

for animal in animals:
  print(f'{animal.title()} gives us meat and thus feeds us.')

print('any of these animals would make a great pet!')
