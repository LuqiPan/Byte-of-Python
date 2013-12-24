number = 23
running = True

while running:
  guess = int(input('Enter an integer: '))

  if guess == number:
    print('Congrats')
    running = False
  elif guess < number:
    print('Guess higher')
  else:
    print('Guess lower')
else:
  print('Done')
