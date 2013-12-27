# encoding=utf-8

f = open("abc.txt", "wt", encoding="utf-8")
f.write("Imagine non-English language here(鹭起)")
f.close()

text = open("abc.txt", encoding="utf-8").read()
print(text)
