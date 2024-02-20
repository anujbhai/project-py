places = ['tokyo', 'phuket', 'binsar', 'miami', 'florence']
print(places)
print(sorted(places))
print(places)

places_reverse = sorted(places, reverse=True)
print(f'\n{places_reverse}')
print(places)

places.reverse()
print(places)
places.reverse()
print(places)

places.sort()
print(places)
places.sort(reverse=True)
print(places)
