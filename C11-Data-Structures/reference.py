print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']

mylist = shoplist

del shoplist[0]

print('shoplist', shoplist)
print('mylist', mylist)

mylist = shoplist[:]
del mylist[0]

print('shoplist', shoplist)
print('mylist', mylist)
