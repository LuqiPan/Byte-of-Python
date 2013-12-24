number = 23
guess = int(input('Enter an integer:'))

if guess == number:
  print('Congrats')
  print('No prizes!')
elif guess < number:
  print('No, guess higher')
else:
  print('No, guess lower')

print('Done')
