Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> thislist = ["apple", "banana", "cherry"]
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> print(thislist[1])
banana
>>> print(thislist[0])
apple
>>> thislist[1] = "blackcurrant"
>>> print
<built-in function print>
>>> print(thislist)
['apple', 'blackcurrant', 'cherry']
>>> thislist = ["apple", "banana", "cherry"]
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> thislist = ["apple", "banana", "cherry"]
>>> for x in thislist:
	print(x)

	
apple
banana
cherry
>>> for x in "cherry"
SyntaxError: invalid syntax
>>> 
>>> for x in "cherry":
	print(x)

	
c
h
e
r
r
y
>>> thislist = ["apple", "banana", "cherry"]
>>> for x in thislist:
	print(x)
	if x =="banana":
		break

	
apple
banana
>>> thistupple = ("apple", "banana", "cherry")
>>> print(thistupple)
('apple', 'banana', 'cherry')
>>> print(thistupple[1])
banana
>>> thistupple[1] = "blackcurrant"
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    thistupple[1] = "blackcurrant"
TypeError: 'tuple' object does not support item assignment
>>> thistupple = ("apple", "banana", "cherry")
>>> for x in thistupple
SyntaxError: invalid syntax
>>> thistupple = ("apple", "banana", "cherry")
>>> for x in thistupple
SyntaxError: invalid syntax
>>> thistupple = ("apple", "banana", "cherry")
>>> for x in thistupple:
	print(x)

	
apple
banana
cherry
>>> for x in "banana":
	print(x)

	
b
a
n
a
n
a
>>> thisset = {"apple", "banana","cherry"}
>>> print(thisset)
{'apple', 'cherry', 'banana'}
>>> 
