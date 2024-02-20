guests = ['maddy', 'vickey', 'manu']
guests.insert(0, 'obit')
guests.insert(1, 'sonu')
guests.insert(2, 'khati')

guest_unavailable = guests.pop(-1)
guest_replacement = 'vivek'
# print(f'{guest_unavailable.title()} is unavailable and will not be present among us.')
# print(f'{guest_replacement.title()} is available and will be joining us tonight.')

guests.append(guest_replacement)

cancelled_guests = []
cg1 = guests.pop()
cg2 = guests.pop()
cg3 = guests.pop()
cg4 = guests.pop()

cancelled_guests.append(cg1)
cancelled_guests.append(cg2)
cancelled_guests.append(cg3)
cancelled_guests.append(cg4)

for cg in cancelled_guests:
  print(f'Dear {cg.title()}, I am sorry, I cannot invite you for dinner tonight.')

for i in guests:
  print(f'Dear {i.title()}, hearty invitations for dinner tonight at my residence.')

# announcement = 'This invitation extends now to a few more of my wellwishers, for I have arranged a bigger table for tonight\'s event.'
# print(announcement)

print(f'This invitation now extends to {len(guests)} person.')

del guests[0]
del guests[0]
print(f'Guests remaining: {guests}')
