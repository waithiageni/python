Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> customer1={"name":"irene", "balance",:10000}
SyntaxError: invalid syntax
>>> customer1={"name":"irene", "balance", :10000}
SyntaxError: invalid syntax
>>> customer1={"name":"irene", "balance":10000}
>>> customer2={"name":"brianna", "balance":5000}
>>> customer2={"name":"mercy", "balance":2500}
>>> customer3={"name":"eva", "balance"300"}
	       
SyntaxError: invalid syntax
>>> customer3={"name":"eva", "balance300}
	       
SyntaxError: EOL while scanning string literal
>>> customer3={"name":"eva", "balance:300}
	       
SyntaxError: EOL while scanning string literal
>>> customer3={"name":"eva", "balance":300}
	       
>>> customer4={"name":"mary", "balance":25000}
	       
>>> customer5={"name":"samuel","balance":100000}
	       
>>> customers
	       
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    customers
NameError: name 'customers' is not defined
>>> customers=[customer1,customer2,customer3,customer4,customer5]
	       
>>> customers
	       
[{'name': 'irene', 'balance': 10000}, {'name': 'mercy', 'balance': 2500}, {'name': 'eva', 'balance': 300}, {'name': 'mary', 'balance': 25000}, {'name': 'samuel', 'balance': 100000}]
>>> for customer in customers:
	       sms="hi{}, your balance is{}".format(customer["name"],customer["balance"])

	       
>>> sms
	       
'hisamuel, your balance is100000'
>>> 
	       
>>> for customer in customers:
	       sms="hi{}, your balance is{}".format(customer["name"],customer["balance"])
	       print(sms)

	       
hiirene, your balance is10000
himercy, your balance is2500
hieva, your balance is300
himary, your balance is25000
hisamuel, your balance is100000
>>> for customer in customers:
	       sms="hi {}, your balance is {}".format(customer["name"],customer["balance"])
	       print(sms)

	       
hi irene, your balance is 10000
hi mercy, your balance is 2500
hi eva, your balance is 300
hi mary, your balance is 25000
hi samuel, your balance is 100000
>>> for customer in customers:
	       loan= customer["balance"]/2.9
	       for customer in customers:
	 sms="hi {}, your balance is Ksh {}, you qualify for a loan of upto {}".format(customer["name"],customer["balance"],["loan"])
	       	       print(sms)
	       
SyntaxError: unindent does not match any outer indentation level
>>> for customer in customers:
	       loan= customer["balance"]/2.9
	 sms="hi {}, your balance is Ksh {}, you qualify for a loan of upto {}".format(customer["name"],customer["balance"],["loan"])
	       	       print(sms)
	       
SyntaxError: unindent does not match any outer indentation level
>>> for customer in customers:
	       loan= customer["balance"]/2.9
	       sms="hi {}, your balance is Ksh {}, you qualify for a loan of upto {}".format(customer["name"],customer["balance"],["loan"])
	       print(sms)

	       
hi irene, your balance is Ksh 10000, you qualify for a loan of upto ['loan']
hi mercy, your balance is Ksh 2500, you qualify for a loan of upto ['loan']
hi eva, your balance is Ksh 300, you qualify for a loan of upto ['loan']
hi mary, your balance is Ksh 25000, you qualify for a loan of upto ['loan']
hi samuel, your balance is Ksh 100000, you qualify for a loan of upto ['loan']
>>> for customer in customers:
	       loan= customer["balance"]/2.9
	       sms="hi {}, your balance is Ksh {}, you qualify for a loan of upto {}".format(customer["name"],customer["balance"],[loan])
	       print(sms)

	       
hi irene, your balance is Ksh 10000, you qualify for a loan of upto [3448.2758620689656]
hi mercy, your balance is Ksh 2500, you qualify for a loan of upto [862.0689655172414]
hi eva, your balance is Ksh 300, you qualify for a loan of upto [103.44827586206897]
hi mary, your balance is Ksh 25000, you qualify for a loan of upto [8620.689655172415]
hi samuel, your balance is Ksh 100000, you qualify for a loan of upto [34482.75862068966]
>>> for customer in customers:
	       loan= customer["balance"]/2.9
	       sms="hi {}, your balance is Ksh {}, you qualify for a loan of upto {}".format(customer["name"],customer["balance"],loan)
	       print(sms)

	       
hi irene, your balance is Ksh 10000, you qualify for a loan of upto 3448.2758620689656
hi mercy, your balance is Ksh 2500, you qualify for a loan of upto 862.0689655172414
hi eva, your balance is Ksh 300, you qualify for a loan of upto 103.44827586206897
hi mary, your balance is Ksh 25000, you qualify for a loan of upto 8620.689655172415
hi samuel, your balance is Ksh 100000, you qualify for a loan of upto 34482.75862068966
>>> for x in range (0,10):
	       if x%3==0:
	       print(x)
	       
SyntaxError: expected an indented block
>>> for x in range (0,10):
	       if x%3==0:
	               print(x)

	       
0
3
6
9
>>> for x in range (0,10):
	       if x%3==0
	       
SyntaxError: invalid syntax
>>> 
	       
;
>>> for x in range (0,10):
	       if x%3==0:
	               print(x)

	       
0
3
6
9
>>> for x in range(0,10):
	       if x%3===0:
	       
SyntaxError: invalid syntax
>>> for x in range(0,10):
	       if x%3=0:
	       
SyntaxError: invalid syntax
>>> for x in range (0,10):
	       if x%3!=0:
	         print(x)

	       
1
2
4
5
7
8
>>> for x in range (0,10):
	       if x%3==0:
	       print("{} is divisible by 3".format(x)
		     
SyntaxError: expected an indented block
>>> for x in range (0,10):
	       if x%3==0:
	        print("{} is divisible by 3".format(x)
		      else:
		      
SyntaxError: invalid syntax
>>> for x in range (0,10):
	       if x%3==0:
	        print("{} is divisible by 3".format(x)
	       else:
		      
SyntaxError: invalid syntax
>>> for x in range (0,10):
	       if x%3==0:
	        print("{} is divisible by 3".format(x))
	       else:
		print("{} is not divisible by 3".format(x))
		      
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for x in range (0,10):
	       if x%3==0:
	        print("{} is divisible by 3".format(x))
	       else:
		print("{} is not divisible by 3".format(x))
		      
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for x in range(0,10)
		      
SyntaxError: invalid syntax
>>> for x in range(0,10):
	if x%3==0:
	       print("{} is divisible by 3".format(x))
	else:
		print("{} is not divisible by 3".format(x))

		      
0 is divisible by 3
1 is not divisible by 3
2 is not divisible by 3
3 is divisible by 3
4 is not divisible by 3
5 is not divisible by 3
6 is divisible by 3
7 is not divisible by 3
8 is not divisible by 3
9 is divisible by 3
>>> for range(0,20):
		      
SyntaxError: invalid syntax
>>> for range(0,20:
	      
SyntaxError: invalid syntax
>>> 
	      


>>> for x in range(0,20):
	      if x%3==0:
	         print("{} is divsible by 3".format(x))
	      elif x%5==0:
	          print("{} is divisible by 5".format(x))
	      else:
	         print("{} is not divisible by 3 or 5".format(x))

	      
0 is divsible by 3
1 is not divisible by 3 or 5
2 is not divisible by 3 or 5
3 is divsible by 3
4 is not divisible by 3 or 5
5 is divisible by 5
6 is divsible by 3
7 is not divisible by 3 or 5
8 is not divisible by 3 or 5
9 is divsible by 3
10 is divisible by 5
11 is not divisible by 3 or 5
12 is divsible by 3
13 is not divisible by 3 or 5
14 is not divisible by 3 or 5
15 is divsible by 3
16 is not divisible by 3 or 5
17 is not divisible by 3 or 5
18 is divsible by 3
19 is not divisible by 3 or 5
>>> for x in range(0,100):
	      if x%7==0:
	         print("{} is divisible by 7".format(x))

	      
0 is divisible by 7
7 is divisible by 7
14 is divisible by 7
21 is divisible by 7
28 is divisible by 7
35 is divisible by 7
42 is divisible by 7
49 is divisible by 7
56 is divisible by 7
63 is divisible by 7
70 is divisible by 7
77 is divisible by 7
84 is divisible by 7
91 is divisible by 7
98 is divisible by 7
>>> for x in range(0,100):
	      if x%7==0:
	         print("{} is divisible by 7".format(x))
	      else:
	         print("{} is not divisible by 7".format(x))

	      
0 is divisible by 7
1 is not divisible by 7
2 is not divisible by 7
3 is not divisible by 7
4 is not divisible by 7
5 is not divisible by 7
6 is not divisible by 7
7 is divisible by 7
8 is not divisible by 7
9 is not divisible by 7
10 is not divisible by 7
11 is not divisible by 7
12 is not divisible by 7
13 is not divisible by 7
14 is divisible by 7
15 is not divisible by 7
16 is not divisible by 7
17 is not divisible by 7
18 is not divisible by 7
19 is not divisible by 7
20 is not divisible by 7
21 is divisible by 7
22 is not divisible by 7
23 is not divisible by 7
24 is not divisible by 7
25 is not divisible by 7
26 is not divisible by 7
27 is not divisible by 7
28 is divisible by 7
29 is not divisible by 7
30 is not divisible by 7
31 is not divisible by 7
32 is not divisible by 7
33 is not divisible by 7
34 is not divisible by 7
35 is divisible by 7
36 is not divisible by 7
37 is not divisible by 7
38 is not divisible by 7
39 is not divisible by 7
40 is not divisible by 7
41 is not divisible by 7
42 is divisible by 7
43 is not divisible by 7
44 is not divisible by 7
45 is not divisible by 7
46 is not divisible by 7
47 is not divisible by 7
48 is not divisible by 7
49 is divisible by 7
50 is not divisible by 7
51 is not divisible by 7
52 is not divisible by 7
53 is not divisible by 7
54 is not divisible by 7
55 is not divisible by 7
56 is divisible by 7
57 is not divisible by 7
58 is not divisible by 7
59 is not divisible by 7
60 is not divisible by 7
61 is not divisible by 7
62 is not divisible by 7
63 is divisible by 7
64 is not divisible by 7
65 is not divisible by 7
66 is not divisible by 7
67 is not divisible by 7
68 is not divisible by 7
69 is not divisible by 7
70 is divisible by 7
71 is not divisible by 7
72 is not divisible by 7
73 is not divisible by 7
74 is not divisible by 7
75 is not divisible by 7
76 is not divisible by 7
77 is divisible by 7
78 is not divisible by 7
79 is not divisible by 7
80 is not divisible by 7
81 is not divisible by 7
82 is not divisible by 7
83 is not divisible by 7
84 is divisible by 7
85 is not divisible by 7
86 is not divisible by 7
87 is not divisible by 7
88 is not divisible by 7
89 is not divisible by 7
90 is not divisible by 7
91 is divisible by 7
92 is not divisible by 7
93 is not divisible by 7
94 is not divisible by 7
95 is not divisible by 7
96 is not divisible by 7
97 is not divisible by 7
98 is divisible by 7
99 is not divisible by 7
>>> for x in range(0,20):
	      if x%3==0 and x%5==0:
	          print(x)

	      
0
15
>>> for x in range(0,20):
	      if x%3==0 or x%5==0:
	          print(x)

	      
0
3
5
6
9
10
12
15
18
>>> true and true
	      
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    true and true
NameError: name 'true' is not defined
>>> True and True
	      
True
>>> True and False
	      
False
>>> False and True
	      
False
>>> False and False
	      
False
>>> True or True
	      
True
>>> True or False
	      
True
>>> False or True
	      
True
>>> False or False
	      
False
>>> for x in range(900,950):
	      if x%5==0 and x%3==0:
	         print(fizzbuzz)

	      
Traceback (most recent call last):
  File "<pyshell#102>", line 3, in <module>
    print(fizzbuzz)
NameError: name 'fizzbuzz' is not defined
>>> for x in range(900,950):
	      if x%5==0 and x%3==0:
	         print("fizzbuzz".format(x))

	      
fizzbuzz
fizzbuzz
fizzbuzz
fizzbuzz
>>> for x in range(900,950):
	      if x%5==0 
	         print("fizz".format(x))
	      
SyntaxError: invalid syntax
>>> for x in range(900,950):
	      if x%5==0:
	         print("fizz".format(x))
	      else:
	         print("buzz".format(x))

	      
fizz
buzz
buzz
buzz
buzz
fizz
buzz
buzz
buzz
buzz
fizz
buzz
buzz
buzz
buzz
fizz
buzz
buzz
buzz
buzz
fizz
buzz
buzz
buzz
buzz
fizz
buzz
buzz
buzz
buzz
fizz
buzz
buzz
buzz
buzz
fizz
buzz
buzz
buzz
buzz
fizz
buzz
buzz
buzz
buzz
fizz
buzz
buzz
buzz
buzz
>>> for x in range(900,950):
	      if x%5==0 and x%3==0:
	         print("fizzbuzz".format(x))
	      if x%5==0:
	        print("fizz".format(x)
	      if x%3==0:
		      
SyntaxError: invalid syntax
>>> for x in range(900,950):
	      if x%5==0 and x%3==0:
	         print("fizzbuzz".format(x))
	      if x%5==0:
	        print("fizz".format(x)
	      if x%3==0:
		      
SyntaxError: invalid syntax
>>> for x in range(900,950):
	      if x%5==0 and x%3==0:
	         print("fizzbuzz".format(x))
	      if x%5==0:
	        print("fizz".format(x)
	      if x%3==0
		print("buzz".format(x)
		      
SyntaxError: invalid syntax
>>> for x in range(900,950):
	      if x%5==0 and x%3==0:
	         print("fizzbuzz")
	      elif x%5==0:
	        print("fizz")
	      elif x%3==0:
		print("buzz")
		      
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for x in range(900,950):
	      if x%5==0 and x%3==0:
	         print("fizzbuzz")
	      elif x%5==0:
	        print("fizz")
	      elif x%3==0:
		print("buzz")
		      
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for x in range(900,950):
	      if x%5==0 and x%3==0:
	         print("fizzbuzz")
	      elif x%5==0:
	        print("fizz")
	      elif x%3==0:
		print("buzz")
		      
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for x in range(900,950):
	      if x%5==0 and x%3==0:
	         print("fizzbuzz".format(x))
	      if x%5==0:
	        print("fizz".format(x))
	      if x%3==0
		print("buzz".format(x))
		      
SyntaxError: invalid syntax
>>> for x in range(900,950):
	      if x%5==0 and x%3==0:
	         print("fizzbuzz".format(x))
	      elif x%5==0:
	        print("fizz".format(x))
	      elif x%3==0:
		print("buzz".format(x))
		      
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for x in range(900,950):
	     if x%5==0 and x%3==0:
		 print("fizzbuzz")
		      
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for x in range(900,950):
         if x%5==0 and x%3==0:
                print("fizzbuzz")
	 elif x%5==0:
		      
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for x in range(900,950):
         if x%5==0 and x%3==0:
                print("fizzbuzz")
	 elif x%5==0:
		      
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for x in range(900,950):
         if x%5==0 and x%3==0:
		      print("fizzbuzz")
		      
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
		      
>>> 
