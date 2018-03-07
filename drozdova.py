Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> liczby = range(0,20)
kwadraty = [x**2 for x in liczby]
print (kwadraty)
SyntaxError: multiple statements found while compiling a single statement
>>> print (5)
5
>>> str= "ala ma kota"
>>> odpowiedz= [ for x in str]
SyntaxError: invalid syntax
>>> a= "ala ma kota"
>>> odp = [ a[0], a[0].size ]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    odp = [ a[0], a[0].size ]
AttributeError: 'str' object has no attribute 'size'
>>> odp = [a[0],a[1]]
>>> print (odp)
['a', 'l']
>>> print ( a.length )
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print ( a.length )
AttributeError: 'str' object has no attribute 'length'
>>> print (a.size)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print (a.size)
AttributeError: 'str' object has no attribute 'size'
>>> a= [ "ala", "ma", "kota"]
>>> print ( a[1] )
ma
>>> a0= ( a[0], len(a[0]))
>>> a1= ( a[1], len(a[1]))
>>> a2= ( a[2], len(a[2]))
>>> print (a0, '\n' )
('ala', 3) 

>>> print (a0, '\n', a1, '\n', a2, '\n' )
('ala', 3) 
 ('ma', 2) 
 ('kota', 4) 

>>> 
>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> def funk( napis )
SyntaxError: invalid syntax
>>> def funk (napis):
end
SyntaxError: expected an indented block
>>> def fib (n)
SyntaxError: invalid syntax
>>> def fib (n , lista):
	for n in lista
	
SyntaxError: invalid syntax
>>> while n
SyntaxError: invalid syntax
>>> while n:
	lista.append( lista[-1] + lista[-2])
        n=n-1
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def fib (n , lista):
	while n:
	lista.append( lista[-1] + lista[-2])
	
SyntaxError: expected an indented block
>>> def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print map(fib, range(startNumber, endNumber))
SyntaxError: invalid syntax
>>> def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
print ( fib(5))
SyntaxError: invalid syntax
>>> lista = fib(6)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    lista = fib(6)
NameError: name 'fib' is not defined
>>> def fib(n):
    if n < 2:
	    print (n)
        return n
    print (' ',fib(n-2) + fib(n-1))
    return fib(n-2) + fib(n-1)
SyntaxError: unindent does not match any outer indentation level
>>> def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
fib(8)
SyntaxError: invalid syntax
>>> def F():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

        
>>> F
<function F at 0x0000028CB3D23AE8>
>>> & F
SyntaxError: invalid syntax
>>> 
>>> print F
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(F)?
>>> print (F)
<function F at 0x0000028CB3D23AE8>
>>> x = raw_input('What is your name?')
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    x = raw_input('What is your name?')
NameError: name 'raw_input' is not defined
>>> k=input()
9
>>> print (k)
9
>>> def f(x):
	if (x>0)
	
SyntaxError: invalid syntax
>>> def f(x):
	if (x>0):
		return " dodatn"
	return " ujemn"

>>> def ff( f, lista ):
	odpowiedz = [ f(x) for x in lista ]
	return odpowiedz
lista =[1,3,-2,-3,4,-6]
SyntaxError: invalid syntax
>>> lista = [1,3,4]
>>> lista = [-1,-4]
>>> lista = [-1,1]
>>> lista = [-1,3,-2,-4,5]
>>> print ( ff (f,lista))
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    print ( ff (f,lista))
NameError: name 'ff' is not defined
>>> def f(x):
	if (x>0):
		return " dodatn"
	return " ujemn"

>>> def ff( f, lista ):
	odpowiedz = [ f(x) for x in lista ]
	return odpowiedz
SyntaxError: invalid syntax
>>> def f(x):
	if (x>0):
		return " dodatn"
	return " ujemn"

>>> def ff( f, lista ):
	odpowiedz = [ f(x) for x in lista ]
	return odpowiedz

>>> lista = [-1,3,-2,-4,5]
>>> print ( ff )
<function ff at 0x0000028CB3D23BF8>
>>> print ( ff(f,lista))
[' ujemn', ' dodatn', ' ujemn', ' ujemn', ' dodatn']
>>> def f(x):
	if (x>0):
		return x

	
>>> def ff( f, lista ):
	odpowiedz = [ f(x) for x in lista ]
	return odpowiedz

>>> lista = [-1,3,-2,-4,5]
>>> print ( ff(f,lista))
[None, 3, None, None, 5]
>>> def f(x,odp):
	if (x>0):
		odp.append(x)

		
>>> def ff( f, lista ):
	 f(x) for x in lista
	 
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> krotki =[(1,2), (4,2), (8,5)]
>>> for x in krotki
SyntaxError: invalid syntax
>>> for x in krotki:
	print ( krot[x])

	
Traceback (most recent call last):
  File "<pyshell#106>", line 2, in <module>
    print ( krot[x])
NameError: name 'krot' is not defined
>>> krot = [ (x) for x in krotki]
>>> print (krot)
[(1, 2), (4, 2), (8, 5)]
>>> def odleglosc( punkt, krotki ):
	odl = [ ((( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0,5) for x in krotki ]

	
>>> def odleglosc( punkt, krotki ):
	odl = [ ((( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0,5) for x in krotki ]
	return odl

>>> def odleglosc( punkt, krotki ):
	odl = [ ( krotki[x], (( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0,5) for x in krotki ]
	return odl

>>> krotki = [(2,3), (43,2), (0,2)]
>>> punkt = (0,0)
>>> print ( odleglosc (punkt, krotki))
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    print ( odleglosc (punkt, krotki))
  File "<pyshell#119>", line 2, in odleglosc
    odl = [ ( krotki[x], (( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0,5) for x in krotki ]
  File "<pyshell#119>", line 2, in <listcomp>
    odl = [ ( krotki[x], (( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0,5) for x in krotki ]
TypeError: list indices must be integers or slices, not tuple
>>> od = odleglosc (punkt, krotki)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    od = odleglosc (punkt, krotki)
  File "<pyshell#119>", line 2, in odleglosc
    odl = [ ( krotki[x], (( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0,5) for x in krotki ]
  File "<pyshell#119>", line 2, in <listcomp>
    odl = [ ( krotki[x], (( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0,5) for x in krotki ]
TypeError: list indices must be integers or slices, not tuple
>>> krotki = [(2,3), (43,2), (0,2)]
>>> print ( krotki[2][1])
2
>>> odl = [ ( krotki[x], (( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0,5) for x in krotki ]
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    odl = [ ( krotki[x], (( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0,5) for x in krotki ]
  File "<pyshell#126>", line 1, in <listcomp>
    odl = [ ( krotki[x], (( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0,5) for x in krotki ]
TypeError: list indices must be integers or slices, not tuple
>>> odl = [ (  (( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0,5) for x in krotki ]
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    odl = [ (  (( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0,5) for x in krotki ]
  File "<pyshell#127>", line 1, in <listcomp>
    odl = [ (  (( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0,5) for x in krotki ]
TypeError: list indices must be integers or slices, not tuple
>>> odl = [ (  (( x[0]-punkt[0])**2 + ( x[1]-punkt[1])**2)**0,5) for x in krotki ]
>>> print ( odl)
[(1, 5), (1, 5), (1, 5)]
>>> odl = [ (  (( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0.5) for x in krotki ]
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    odl = [ (  (( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0.5) for x in krotki ]
  File "<pyshell#130>", line 1, in <listcomp>
    odl = [ (  (( krotki[x][0]-punkt[0])**2 + ( krotki[x][1]-punkt[1])**2)**0.5) for x in krotki ]
TypeError: list indices must be integers or slices, not tuple
>>> odl = [ (  (( x[0]-punkt[0])**2 + ( x[1]-punkt[1])**2)**0.5) for x in krotki ]
>>> print (odl)
[3.605551275463989, 43.04648650006177, 2.0]
>>> odl = [ ( krotki[x], (( x[0]-punkt[0])**2 + ( x[1]-punkt[1])**2)**0.5) for x in krotki ]
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    odl = [ ( krotki[x], (( x[0]-punkt[0])**2 + ( x[1]-punkt[1])**2)**0.5) for x in krotki ]
  File "<pyshell#133>", line 1, in <listcomp>
    odl = [ ( krotki[x], (( x[0]-punkt[0])**2 + ( x[1]-punkt[1])**2)**0.5) for x in krotki ]
TypeError: list indices must be integers or slices, not tuple
>>> odl = [ ( x, (( x[0]-punkt[0])**2 + ( x[1]-punkt[1])**2)**0.5) for x in krotki ]
>>> print (odl)
[((2, 3), 3.605551275463989), ((43, 2), 43.04648650006177), ((0, 2), 2.0)]
>>> sortow = sorted ( odl , key = lambda tup : tup[1])
>>> print (sortow)
[((0, 2), 2.0), ((2, 3), 3.605551275463989), ((43, 2), 43.04648650006177)]
>>> sortow = sorted ( odl , key = lambda tup : tup[0][1])
>>> print (sortow)
[((43, 2), 43.04648650006177), ((0, 2), 2.0), ((2, 3), 3.605551275463989)]
>>> 
