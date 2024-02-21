my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My fav foods are:')
for my_food in my_foods:
  print(my_food.title())

print('\nMy friend\'s fav foods are:')
for frnd_food in friend_foods:
  print(frnd_food.title())
