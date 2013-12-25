#decimal (.) precision of 3
print('{0:.3}'.format(1/3))

#fill with underscores (_) with the text centered
print('{0:_^11}'.format('luqi'))

#keyword-based format
print('{name} wrote {book}'.format(name='Luqi', book='no books'))

#no new line
print("No ", end="")
print("new line")
