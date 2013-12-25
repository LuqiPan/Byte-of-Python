name = 'Swaroop'

if name.startswith('Swa'):
  print('Yes it starts with "Swa"')

if 'a' in name:
  print('Yes "a" is in the string')

if name.find('war') != -1:
  print('Yes, it contains "war"')

delimiter = '_*_'
mylist  = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
