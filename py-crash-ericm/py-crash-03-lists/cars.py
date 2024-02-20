# permanent sorting
cars1 = ['bmw', 'audi', 'porsche', 'mitsubishi']
cars1.sort(reverse=True)
print(cars1)

# temporary sorting
cars2 = ['renault', 'toyota', 'hyundai', 'honda']
print('Here is the original list:')
print(cars2)

print('\nHere is the temporarily sorted list:')
print(sorted(cars2))

print('\nHere is the original list again:')
print(cars2)

# reverse (no sorting)
cars3 = ['range rover', 'jeep', 'nissan', 'ford']
print(f'\n{cars3}')
cars3.reverse()
print(f'Reverse: \n{cars3}')
