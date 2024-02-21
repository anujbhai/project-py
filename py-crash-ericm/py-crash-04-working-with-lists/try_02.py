firearms = [
  'colt python revolver (.357 mag)',
  'sig sauer p360 pistol (9mm luger)',
  'mossberg pump-action shotgun (12 ga)',
  'savage single-shot shotgun (12 ga)',
  'mauser m18 bolt-action rifle (.308 win)',
  'winchester 1873 lever-action rifle (.357 mag)',
  'browning BAR semi-auto (.308 win)'
]
print('The first three item in the list are:')
for item1 in firearms[0:3]:
  print(item1)

print('\nThe three items from the middle of the list are:')
for item2 in firearms[2:5]:
  print(item2)

print('\nThe last three items in the list are:')
for item3 in firearms[-3:]:
  print(item3)