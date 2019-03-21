Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for y in range(0,100):
	if y%9==0 and y%11==0:
		print("{} is divisible by 9 and 11".format(y))
	else:
		print("{} is not divisible by 9 and 11".format(y))

		
0 is divisible by 9 and 11
1 is not divisible by 9 and 11
2 is not divisible by 9 and 11
3 is not divisible by 9 and 11
4 is not divisible by 9 and 11
5 is not divisible by 9 and 11
6 is not divisible by 9 and 11
7 is not divisible by 9 and 11
8 is not divisible by 9 and 11
9 is not divisible by 9 and 11
10 is not divisible by 9 and 11
11 is not divisible by 9 and 11
12 is not divisible by 9 and 11
13 is not divisible by 9 and 11
14 is not divisible by 9 and 11
15 is not divisible by 9 and 11
16 is not divisible by 9 and 11
17 is not divisible by 9 and 11
18 is not divisible by 9 and 11
19 is not divisible by 9 and 11
20 is not divisible by 9 and 11
21 is not divisible by 9 and 11
22 is not divisible by 9 and 11
23 is not divisible by 9 and 11
24 is not divisible by 9 and 11
25 is not divisible by 9 and 11
26 is not divisible by 9 and 11
27 is not divisible by 9 and 11
28 is not divisible by 9 and 11
29 is not divisible by 9 and 11
30 is not divisible by 9 and 11
31 is not divisible by 9 and 11
32 is not divisible by 9 and 11
33 is not divisible by 9 and 11
34 is not divisible by 9 and 11
35 is not divisible by 9 and 11
36 is not divisible by 9 and 11
37 is not divisible by 9 and 11
38 is not divisible by 9 and 11
39 is not divisible by 9 and 11
40 is not divisible by 9 and 11
41 is not divisible by 9 and 11
42 is not divisible by 9 and 11
43 is not divisible by 9 and 11
44 is not divisible by 9 and 11
45 is not divisible by 9 and 11
46 is not divisible by 9 and 11
47 is not divisible by 9 and 11
48 is not divisible by 9 and 11
49 is not divisible by 9 and 11
50 is not divisible by 9 and 11
51 is not divisible by 9 and 11
52 is not divisible by 9 and 11
53 is not divisible by 9 and 11
54 is not divisible by 9 and 11
55 is not divisible by 9 and 11
56 is not divisible by 9 and 11
57 is not divisible by 9 and 11
58 is not divisible by 9 and 11
59 is not divisible by 9 and 11
60 is not divisible by 9 and 11
61 is not divisible by 9 and 11
62 is not divisible by 9 and 11
63 is not divisible by 9 and 11
64 is not divisible by 9 and 11
65 is not divisible by 9 and 11
66 is not divisible by 9 and 11
67 is not divisible by 9 and 11
68 is not divisible by 9 and 11
69 is not divisible by 9 and 11
70 is not divisible by 9 and 11
71 is not divisible by 9 and 11
72 is not divisible by 9 and 11
73 is not divisible by 9 and 11
74 is not divisible by 9 and 11
75 is not divisible by 9 and 11
76 is not divisible by 9 and 11
77 is not divisible by 9 and 11
78 is not divisible by 9 and 11
79 is not divisible by 9 and 11
80 is not divisible by 9 and 11
81 is not divisible by 9 and 11
82 is not divisible by 9 and 11
83 is not divisible by 9 and 11
84 is not divisible by 9 and 11
85 is not divisible by 9 and 11
86 is not divisible by 9 and 11
87 is not divisible by 9 and 11
88 is not divisible by 9 and 11
89 is not divisible by 9 and 11
90 is not divisible by 9 and 11
91 is not divisible by 9 and 11
92 is not divisible by 9 and 11
93 is not divisible by 9 and 11
94 is not divisible by 9 and 11
95 is not divisible by 9 and 11
96 is not divisible by 9 and 11
97 is not divisible by 9 and 11
98 is not divisible by 9 and 11
99 is divisible by 9 and 11
>>> a=[]
>>> for y in range(0,100):
	if y%9==0:
		a.apppend(y)

		
Traceback (most recent call last):
  File "<pyshell#10>", line 3, in <module>
    a.apppend(y)
AttributeError: 'list' object has no attribute 'apppend'
>>> a=[]
>>> for x in range(0,100):
	if x%9==0:
		a.append(x)

		
>>> 
>>> a
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
>>> b=[]
>>> for x in range(0,100):
	if x%11==0:
		b.append(x)

		
>>> b
[0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> c=a+b
>>> c
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> c.sort()
>>> c
[0, 0, 9, 11, 18, 22, 27, 33, 36, 44, 45, 54, 55, 63, 66, 72, 77, 81, 88, 90, 99, 99]
>>> student1={"name":"Aisha","YOB":1998}
>>> student2={"name":"Sharon","YOB":1997}
>>> student3={"name":"Evelyn","YOB":1999}
>>> student4={"name":"Naima","YOB":2000}
>>> student5={"name":"Iene","YOB":1996}
>>> students=(student1,student2,student3,student4,student5)
>>> students
({'name': 'Aisha', 'YOB': 1998}, {'name': 'Sharon', 'YOB': 1997}, {'name': 'Evelyn', 'YOB': 1999}, {'name': 'Naima', 'YOB': 2000}, {'name': 'Iene', 'YOB': 1996})
>>> for student in students:
	age in days=(2019-student[YOB])*365:
		
SyntaxError: invalid syntax
>>> for student in students:
	age in days=(2019-student[YOB])*365
	
SyntaxError: can't assign to comparison
>>> for student in students:
	ageindays=(2019-student[YOB])*365
	ageindays=("hello {},your year of birth is {},hence your age in days is {} days".format(student["name"],student["YOB"],ageindays)
		   print(ageindays)
		   
SyntaxError: invalid syntax
>>> for student in students:
	ageindays=(2019-student[YOB])*365
	ageindays=("hello {},your year of birth is {},hence your age in days is {} days".format(student["name"],student["YOB"],ageindays)
	print(ageindays)
		   
SyntaxError: invalid syntax
>>> 
		   
>>> students=[student1,student2,student3,student4,student5]
		   
>>> students
		   
[{'name': 'Aisha', 'YOB': 1998}, {'name': 'Sharon', 'YOB': 1997}, {'name': 'Evelyn', 'YOB': 1999}, {'name': 'Naima', 'YOB': 2000}, {'name': 'Iene', 'YOB': 1996}]
>>> for student in students:
	ageindays=(2019-student[YOB])*365
	ageindays=("hello {},your year of birth is {},hence your age in days is {} days".format(student["name"],student["YOB"],ageindays)
	print(ageindays)
		   
SyntaxError: invalid syntax
>>> for student in students:
	ageindays=(2019-student[YOB])*365
	sms=("hello {},your year of birth is {},hence your age in days is {} days".format(student["name"],student["YOB"],ageindays)
	print(sms)
	     
SyntaxError: invalid syntax
>>> 
for student in students:
	ageindays=(2019-student[YOB])*365
	sms="hello {},your year of birth is {},hence your age in days is {} days".format(student["name"],student["YOB"],ageindays)
	print(sms)

	     
Traceback (most recent call last):
  File "<pyshell#49>", line 3, in <module>
    ageindays=(2019-student[YOB])*365
NameError: name 'YOB' is not defined
>>> for student in students:
	ageindays=(2019-student['YOB'])*365
	sms="hello {},your year of birth is {},hence your age in days is {} days".format(student["name"],student["YOB"],ageindays)
	print(sms)

	     
hello Aisha,your year of birth is 1998,hence your age in days is 7665 days
hello Sharon,your year of birth is 1997,hence your age in days is 8030 days
hello Evelyn,your year of birth is 1999,hence your age in days is 7300 days
hello Naima,your year of birth is 2000,hence your age in days is 6935 days
hello Iene,your year of birth is 1996,hence your age in days is 8395 days




        
             
        

        

             

SyntaxError: invalid syntax
>>> for L in range(2019,2119):
	     if L%4==0:
	     print(L)
	     
SyntaxError: expected an indented block
>>> 
	     
>>> for p in range(2019,2119):
	     if p%4==0:
	     print(p)
	     
SyntaxError: expected an indented block
>>> for p in range(2019,2119):
	     if p%4==0:
	         print(p)

	     
2020
2024
2028
2032
2036
2040
2044
2048
2052
2056
2060
2064
2068
2072
2076
2080
2084
2088
2092
2096
2100
2104
2108
2112
2116
>>> 
