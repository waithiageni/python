Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def hello():
	print("hello AkiraChix")

	
>>> 
>>> hello
<function hello at 0x043293D8>
>>> hello()
hello AkiraChix
>>> 
>>> hello()
hello AkiraChix
>>> def hello(name):
	print("hello {}".format(name))

	
>>> hello("irene")
hello irene
>>> hello("james")
hello james
>>> hello("Aisha")
hello Aisha
>>> hello("Brianna")
hello Brianna
>>> 
>>> def sum(a,b):
	ans=a+b
	return ans
sum

>>> def sum(a,b):
	ans=a+b
	return ans

>>> 
>>> sum
<function sum at 0x040B5978>
>>> sum(a,b)

>>> def sum(a,b):
	ans=a+b
	return ans

>>> sum(10,15)
25
>>> sum(1000,1000)
2000
>>> sum(500000,500000)
1000000
>>> sum(10)

>>> sum(10,20,30)

>>> def sum(a,b)

>>> def sum(a,b):
	ans=a*b
	return ans

>>> sum(334,289)
96526
>>> def multiply(a,b):
	ans=a*b
	return ans

>>> multiply(a,b)

>>> def multiply(a,b):
	ans=a*b
	return ans

>>> multiply(334,289)
96526
>>> def divide(a,b):
	ans=a/b
	return ans

>>> 1136
1136
>>> divide(1134/6)

>>> divide(1134,6)
189.0
>>> def subtraction(a,b):
	ans=a-b
	return ans

>>> sutraction(375,189)

>>> subtraction(375,189)
186
>>> def modulues

>>> def modulues(a,b):

	ans=a%b
	return ans

>>> modulues(49,7)
0
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def age("irene",1996):
	

>>> def age("irene" ,1996):
	

>>> def age('irene' ,1996):
	

>>> def age(name,1996):
	

>>> def age("name" , 1996)

>>> def data(name,YOB):
	age=2019-YOB
	print("hello{} you are{} years old".format (name,age))

	
>>> data("irene",1996)
helloirene you are23 years old
>>> def data(name,YOB):
	age=2019-YOB
	print("hello {} you are{} years old".format (name,age))

	
>>> data(Irene,1996)

>>> data("Irene",1996)
hello Irene you are23 years old
>>> def data(name,YOB):
	age=2019-YOB
	print("hello {} you are {} years old".format (name,age))

	
>>> data(Irene,1996)

>>> data("Irene",1996)
hello Irene you are 23 years old
>>> data("Brianna",2017)
hello Brianna you are 2 years old
>>> data("Gabriel",1993)
hello Gabriel you are 26 years old
>>> data("Mary",1979)
hello Mary you are 40 years old
>>> data("Samuel",1970)
hello Samuel you are 49 years old
>>> def squares(numbers)
SyntaxError: invalid syntax
>>> def squares(numbers):
	for number in numbers:
		print (number*number)

		
>>> 
>>> x=[1,2,3,4,5,6]
>>> y=[100,200,300,400]
>>> squares(x)
1
4
9
16
25
36
>>> squares(y)
10000
40000
90000
160000
>>> def squares(numbers):
	for number in numbers:
		ans=number*number
		return ans

	
>>> x=[20,30,45,55]
>>> y=[33,44,55,66]
>>> sum(20,20)
400
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)
		return a

	
>>> x=[1,2,3,4,5,6]
>>> squaree(x)

>>> squares(x)
[1]
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)
		return a
	x=[1,2,3,4,5,6]
	y=[200,300,400,330,345,555]

	
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)
	return a

>>> x=[2,4,6,8,10]
>>> y=[5,15,20,25,30,35]
>>> squares(x)
[4, 16, 36, 64, 100]
>>> squares(y)
[25, 225, 400, 625, 900, 1225]
>>> def multiply(numbers):
	a=[]
	for number in numbers:
		s=number*10
		a.append(s)
	return a

>>> x=[2,4,6,8,10]
>>> y=[5,15,20,25,30,35]
>>> multiply(x)
[20, 40, 60, 80, 100]
>>> multiply(y)
[50, 150, 200, 250, 300, 350]
>>> 
