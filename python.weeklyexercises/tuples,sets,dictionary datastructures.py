Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=(1,2,3,4)
>>> b=('a','b','c','d')
>>> a.append(5)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.append(5)
AttributeError: 'tuple' object has no attribute 'append'
>>> b.remove('c')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b.remove('c')
AttributeError: 'tuple' object has no attribute 'remove'
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a.pop()
AttributeError: 'tuple' object has no attribute 'pop'
>>> b.pop()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    b.pop()
AttributeError: 'tuple' object has no attribute 'pop'
>>> a.reverse()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> b.sort()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    b.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> for x in a:
	print(x)

	
1
2
3
4
>>> c=list(a)
>>> d=(x for x in a)
>>> c
[1, 2, 3, 4]
>>> d
<generator object <genexpr> at 0x03EAACF0>
>>> d=[x for x in a]
>>> d
[1, 2, 3, 4]
>>> a
(1, 2, 3, 4)
>>> f=a+b
>>> f
(1, 2, 3, 4, 'a', 'b', 'c', 'd')
>>> a*3
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
>>> "b" in b
True
>>> "e" in b
False
>>> s in a
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s in a
NameError: name 's' is not defined
>>> 5 in a
False
>>> 1 in a
True
>>> y=(x)
>>> y
4
>>> y = (x)
>>> y
4
>>> y=(a)
>>> y
(1, 2, 3, 4)
>>> y=(z for z in x)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    y=(z for z in x)
TypeError: 'int' object is not iterable
>>> y=(x for x in a)
>>> y
<generator object <genexpr> at 0x03EAACF0>
>>> a=[1,2,3,1,4,2,5,3,7]
>>> a
[1, 2, 3, 1, 4, 2, 5, 3, 7]
>>> b=set(a)
>>> b
{1, 2, 3, 4, 5, 7}
>>> c={"a","b","c","c","a","d"}
>>> c
{'b', 'a', 'c', 'd'}
>>> d={'a','A','b','B'}
>>> d
{'B', 'A', 'a', 'b'}
>>> d={'a','A','b','B','a','B'}
>>> d
{'B', 'A', 'a', 'b'}
>>> s1={1,2.3.4}
SyntaxError: invalid syntax
>>> s1={1,2,3,4}
>>> s1
{1, 2, 3, 4}
>>> s2={3,4,5,6}
>>> s2
{3, 4, 5, 6}
>>> s2.add(7)
>>> s2
{3, 4, 5, 6, 7}
>>> s2.remove(7)
>>> s2
{3, 4, 5, 6}
>>> s1.discard(4)
>>> s1
{1, 2, 3}
>>> s2.remove(7)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    s2.remove(7)
KeyError: 7
>>> s2.discard(4)
>>> s2
{3, 5, 6}
>>> s1.difference(s2)
{1, 2}
>>> s2.difference(s1)
{5, 6}
>>> s1.intersection(s2)
{3}
>>> s2.intersecion(s1)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s2.intersecion(s1)
AttributeError: 'set' object has no attribute 'intersecion'
>>> s2.intersection(s1)
{3}
>>> s2.union(s1)
{1, 2, 3, 5, 6}
>>> si
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    si
NameError: name 'si' is not defined
>>> s1.union(s2)
{1, 2, 3, 5, 6}
>>> {1, 2, 3, 5, 6}
{1, 2, 3, 5, 6}
>>> s1.extend(s2)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s1.extend(s2)
AttributeError: 'set' object has no attribute 'extend'
>>> 
>>> 



>>> 

>>> 



>>> 

>>> 


>>> 

>>> 

>>> 


>>> 
>>> 

>>> 

>>> 

>>> 

>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 
>>> 



>>> 
>>> 


>>> 

>>> 



>>> 
>>> 



>>> 
>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> 


>>> 
>>> 


>>> 

>>> 


>>> 
>>> 



>>> 

>>> 



>>> 

>>> 



>>> 
>>> 



>>> 
>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> 


>>> 

>>> 


>>> 




>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 
>>> 
>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> 


>>> 

>>> 



>>> 

>>> 

>>> 


>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 

>>> 


>>> 
>>> 

>>> 


>>> 
>>> 



>>> 
>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 
>>> 


>>> 

>>> 



>>> 
>>> 



>>> 
>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 
>>> 


>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 
>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 
>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 


>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 



>>> 

>>> 


>>> 

>>> 


>>> 

>>> 

>>> s2.update({10,11,12,})
>>> s2
{3, 5, 6, 10, 11, 12}
>>> codes={"kenya":254, "uganda":256, "tanzania":255}
>>> codes
{'kenya': 254, 'uganda': 256, 'tanzania': 255}
>>> codes["kenya"]
254
>>> codes["kenya"]=250
>>> codes
{'kenya': 250, 'uganda': 256, 'tanzania': 255}
>>> codes["kenya"]=254
>>> codes
{'kenya': 254, 'uganda': 256, 'tanzania': 255}
>>> codes["rwanda"]=252
>>> codes
{'kenya': 254, 'uganda': 256, 'tanzania': 255, 'rwanda': 252}
>>> codes.pop("rwanda")
252
>>> codes
{'kenya': 254, 'uganda': 256, 'tanzania': 255}
>>> codes.keys()
dict_keys(['kenya', 'uganda', 'tanzania'])
>>> codes.values()
dict_values([254, 256, 255])
>>> 
>>> for key in codes.keys():
	print(key)

	
kenya
uganda
tanzania
>>> for value in codes.values():
	print(value)

	
254
256
255
>>> m=dict()
>>> m
{}
>>> m[a"
      
SyntaxError: EOL while scanning string literal
>>> m["a"]=10
      
>>> m["b"]=20
      
>>> m
      
{'a': 10, 'b': 20}
>>> n=range(0,10)
      
>>> n
      
range(0, 10)
>>> n
      
range(0, 10)
>>> for r in:
      
SyntaxError: invalid syntax
>>> for r in:
      n=range(0,10)
      
SyntaxError: invalid syntax
>>> n=range(0,10)
      
>>> n
      
range(0, 10)
>>> for r in n:
      print(r)

      
0
1
2
3
4
5
6
7
8
9
>>> p=dict()
      
>>> p["q"]=r
      
>>> p["s"]=r*r
      
>>> m
      
{'a': 10, 'b': 20}
>>> p
      
{'q': 9, 's': 81}
>>> for r in n:
      print(r)

      
0
1
2
3
4
5
6
7
8
9
>>> h=[r*r for r in n]
      
>>> h
      
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> p=dict()
      
>>> p=dict()
      
>>> p[]=r
      
SyntaxError: invalid syntax
>>> p["r"]=r
      
>>> p["r"]=r*r
      
>>> p
      
{'r': 81}
>>> p=dict()
      
>>> p[0,1,2,3,4,5,6,7,8,9]=r
      
>>> p[0,1,2,3,4,5,6,7,8,9]=r*r
      
>>> p
      
{(0, 1, 2, 3, 4, 5, 6, 7, 8, 9): 81}
>>> h
      
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> p=dict()
      
>>> p["key"]=r
      
>>> p["values"]=r*r
      
>>> p
      
{'key': 9, 'values': 81}
>>> p["key"]=r
      
>>> p["values"]=h
      
>>> p
      
{'key': 9, 'values': [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]}
>>> p["n"]=r
      
>>> p["h"]=r*r
      
>>> p
      
{'key': 9, 'values': [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], 'n': 9, 'h': 81}
>>> r.keys
      
Traceback (most recent call last):
  File "<pyshell#500>", line 1, in <module>
    r.keys
AttributeError: 'int' object has no attribute 'keys'
>>> dict keys()
      
SyntaxError: invalid syntax
>>> h
      
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> h=dict()
      
>>> h
      
{}
>>> h["key"]=r
      
>>> h["values"]=r*r
      
>>> h
      
{'key': 9, 'values': 81}
>>> h["key"]=0,1,2,3,4,5,6,7,8,9
      
>>> h["values"]=0,1,4,9,16,25,36,49,64,81
      
>>> h
      
{'key': (0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 'values': (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)}
>>> h=dict()
      
>>> h
      
{}
>>> h[r]=r*r
      
>>> h
      
{9: 81}
>>> h=dict()
      
>>> h
      
{}
>>> h[n]=r*r
      
>>> h
      
{range(0, 10): 81}
>>> h=dict()
      
>>> h
      
{}
>>> for r in range(10)
      
SyntaxError: invalid syntax
>>> for r in range(10):
      h[r]=r*r

      
>>> 
      
>>> h
      
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> 
