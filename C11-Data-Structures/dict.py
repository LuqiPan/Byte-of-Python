ab = { 'Swaroop' : 'swaroop@swaroopch.com', 
'Larry' : 'larry@wall.org',
'Matsumoto' : 'matz@ruby-lang.org',
'Spammer' : 'spammer@hotmail.com' }

print('Swaroop', ab['Swaroop'])
del ab['Spammer']

print("There are {} contacts in the addressbook".format(len(ab)))

for name, address in ab.items():
  print('Contact {} at {}'.format(name, address))

ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
  print("Guido's address is", ab['Guido'])
