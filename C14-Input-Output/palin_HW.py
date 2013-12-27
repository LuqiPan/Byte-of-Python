#Set containing all the forbidden characters
forbidden = set(['!', ' ', '?', ',', '.'])

def remove(text):
  #Store the string with forbidden characters removed
  new_text = ''

  for i in text:
    if not i in forbidden:
      #Append it to the new text
      new_text += i

  #convert it to lower case
  return new_text.lower()

def reverse(text):
  return text[::-1]

def is_palindrome(text):
  return remove(text) == reverse(remove(text))

something = input('Enter text: ')
if (is_palindrome(something)):
  print('Yes, palindrome')
else:
  print('No')
