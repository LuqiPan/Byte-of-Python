shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have {} items to purchase.'.format(len(shoplist)))

print('Items are:')
for item in shoplist:
  print(item)

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print("Sort!")
shoplist.sort()
print('Sorted: ', shoplist)

print('First item:', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
