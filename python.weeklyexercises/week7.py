Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def initial(first,second):
	x=first[0]
	y=second[0]
	ans=x+y
	return ans

>>> initial("irene","nyambura")
'in'
>>> def initial(first,second):
	x=first
	y=second
	print len(x)
	print len(y)
	
SyntaxError: invalid syntax
>>> def initial(first,second):
	x=len(first)
	y=len(second)
	print(x)
	print(y)

	
>>> initial("irene" , "nyambura")
5
8
>>> def initial(first,second):
	x=first[3]
	y=second[3]
	print(x)
	print(y)

	
>>> def initial("irene" , "nyambura")
SyntaxError: invalid syntax
>>>  initial("irene" , "nyambura")
SyntaxError: unexpected indent
>>> initial("irene" , "nyambura")
n
m
>>> fruits = ['watermelon','mango','banana','grapes','berries']
>>> fruits[2]
'banana'
>>> 
