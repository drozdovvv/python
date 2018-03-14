Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class klassa:
	def funk (self,zmienna):
		print ("wyw met 1")
	def funk2 (self):
		print ("wyw met 2")

		
>>> obiekt = klassa()
>>> obiekt.funk2
<bound method klassa.funk2 of <__main__.klassa object at 0x000002128D6CAA58>>
>>> 
>>> class klassa:
	atr1=None
	  atr2= None
	  
SyntaxError: unexpected indent
>>> class klassa:
	atr1=None
	atr2=None
	def setatr2(self,zm):
		self.__atr2=zm
	def setatr3(self, zm):
		self.atr3=zm
	def add(self):
		return self.atr1 +self.__atr2 + self.atr3

	
>>> ob =klassa()
>>> ob.atr1=5
>>> ob.setatr2(11)
>>> ob.setatr3(9)
>>> print (ob.add())
25
>>> ob.__klassa__atr2=12
>>> print (ob.add())
25
>>> 
>>> 
>>> class samochod:
	kolor= None
	def nsetkolor(self,kolor):
		self.kolor=kolor

		
>>> class osobowy(samochod):
	marka ="mers"

	
>>> samochod= osobowy
>>> samochod= osobowy()
>>> samochod.setkolor("nieb")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    samochod.setkolor("nieb")
AttributeError: 'osobowy' object has no attribute 'setkolor'
>>> class samochod:
	kolor= None
	def nsetkolor(self,kolor):
		self.kolor=kolor
class osobowy(samochod):
	marka ="mers"
	
SyntaxError: invalid syntax
>>> 
>>> class a(object):
	def metoda(self):
		print ("aaa")

		
>>> class b(a):
	def met(self):
		print("bbb")

		
>>> ob =b()
>>> ob.metoda()
aaa
>>> class b(a):
	def met(self):
		super(b,self).metoda()
		print("bbb")

		
>>> ob= b()
>>> ob.metoda()
aaa
>>> ob.met()
aaa
bbb
>>> class klasa (object):
	def __init__(self,zm):
		self.zm=zm
	def __add__(self,other):
		return self.zm +other.zm

	
>>> class liczbazesp:
	def dodaj(a,b):
		return a+b
	def odejmowanie(a,b):
		return a-b
	def mnoz (a,b)
	
SyntaxError: invalid syntax
>>> class liczbazesp:
	def dodaj(a,b):
		return a+b
	def odejmowanie(a,b):
		return a-b
	def mnoz (a,b):
		return a*b
	def dziel(a,b)
	
SyntaxError: invalid syntax
>>> import math
class liczbazesp:
	a=None
	b=None
	def zdefinA(zm):
		a=zm
	def zdefinB(zm):
		b=zm
	def dodaj(a,b):
		return a+b
	def odejmowanie(a,b):
		return a-b
	def mnoz (a,b):
		return a*b
	def dziel(a,b):
		return a/b
	def porownaj():
		if a>0 and b>0 :
			print ("liczby sa dodatnie")
		elif a<0 and b<0 :
			print ("liczby sa ujemne")
		if a>b :
			print ("a > b")
		elif b>a :
			print ("b > a")
	def modul(a,b):
		zm = a**2 + b**2
		print math.sqrt(zm)
		
SyntaxError: multiple statements found while compiling a single statement
>>> class liczbazesp:
	a=None
	b=None
	def zdefinA(zm):
		a=zm
	def zdefinB(zm):
		b=zm
	def dodaj(a,b):
		return a+b
	def odejmowanie(a,b):
		return a-b
	def mnoz (a,b):
		return a*b
	def dziel(a,b):
		return a/b
	def porownaj():
		if a>0 and b>0 :
			print ("liczby sa dodatnie")
		elif a<0 and b<0 :
			print ("liczby sa ujemne")
		if a>b :
			print ("a > b")
		elif b>a :
			print ("b > a")
	def modul(a,b):
		import math
		zm = a**2 + b**2
		print math.sqrt(zm)
		
SyntaxError: invalid syntax
>>> import math
>>> class liczbazesp:
	a=None
	b=None
	def zdefinA(zm):
		a=zm
	def zdefinB(zm):
		b=zm
	def dodaj(a,b):
		return a+b
	def odejmowanie(a,b):
		return a-b
	def mnoz (a,b):
		return a*b
	def dziel(a,b):
		return a/b
	def porownaj():
		if a>0 and b>0 :
			print ("liczby sa dodatnie")
		elif a<0 and b<0 :
			print ("liczby sa ujemne")
		if a>b :
			print ("a > b")
		elif b>a :
			print ("b > a")
	def modul(a,b):
		zm = a**2 + b**2
		print math.sqrt(zm)
		
SyntaxError: invalid syntax
>>> class liczbazesp:
	a=None
	b=None
	def zdefinA(zm):
		a=zm
	def zdefinB(zm):
		b=zm
	def dodaj(a,b):
		return a+b
	def odejmowanie(a,b):
		return a-b
	def mnoz (a,b):
		return a*b
	def dziel(a,b):
		return a/b
	def porownaj():
		if a>0 and b>0 :
			print ("liczby sa dodatnie")
		elif a<0 and b<0 :
			print ("liczby sa ujemne")
		if a>b :
			print ("a > b")
		elif b>a :
			print ("b > a")
	def modul(a,b):
		zm = a**2 + b**2
		return math.sqrt(zm)
	def print(modul) :
		print ( "#a + #b ")
		print ("odpowiedz= #zm")

		
>>> obj= liczbazesp()
>>> obj.zdefin(4)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    obj.zdefin(4)
AttributeError: 'liczbazesp' object has no attribute 'zdefin'
>>> obj= liczbazesp()
>>> obj.zdefinA(5)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    obj.zdefinA(5)
TypeError: zdefinA() takes 1 positional argument but 2 were given
>>> class zesp (object):
	a=0
	b=0
	def __setattr__(self,name,value):
		if(name=="im")
		
SyntaxError: invalid syntax
>>> class zesp (object):
	a=0
	b=0
	def __setattr__(self,name,value):
		if(name=="im"):
			self.b= value
		elif(name=="re"):
			self.a= value
		elif(name=="attr"):
			self.b=value[0]
			self.a=value[1]
	def __str__(self):
		return("%d + %di" % (self.b,self.a))
	def __modul__(self):
		print (math.sqrt( self.b**2 + self.a**2 ))
	def dodaj(self):
		print ( self.a + self.b )
	def odejm(self):
		print ( self.b - self.a )
	def mnoz(self):
		print ( self.a * self.b )
	def dziel(self):
		print ( self.b / self.a )

		
>>> obj = zesp()
>>> obj.attr = (4,5)
>>> print (obj)
0 + 0i
>>> obj.dodaj()
0
>>> obj.im=5
>>> print (obj)
0 + 0i
>>> class zesp (object):
	a=0
	b=0
	def __setattr__(self,name,value):
		print ("nn")
		if(name=="im"):
			self.b= value
		elif(name=="re"):
			self.a= value
		elif(name=="attr"):
			self.b=value[0]
			self.a=value[1]
	def __str__(self):
		return("%d + %di" % (self.b,self.a))
	def __modul__(self):
		print (math.sqrt( self.b**2 + self.a**2 ))
	def dodaj(self):
		print ( self.a + self.b )
	def odejm(self):
		print ( self.b - self.a )
	def mnoz(self):
		print ( self.a * self.b )
	def dziel(self):
		print ( self.b / self.a )

		
>>> obj = zesp()
>>> obj.attr= (7,9)
nn
nn
nn
>>> class zesp (object):
	atr =[0,0]
	def __setattr__(self,name,value):
		if(name=="im"):
			self.atr[0]= value
		elif(name=="re"):
			self.atr[1]= value
		elif(name=="attr"):
			self.atr[0]=value[0]
			self.atr[1]=value[1]
	def __str__(self):
		return("%d + %di" % (self.atr[0],self.atr[1]))
	def __modul__(self):
		print (math.sqrt( self.atr[0]**2 + self.atr[1]**2 ))
	def dodaj(self):
		print ( self.atr[1] + self.atr[0] )
	def odejm(self):
		print ( self.atr[0] - self.atr[1] )
	def mnoz(self):
		print ( self.atr[1] * self.atr[0] )
	def dziel(self):
		print ( self.atr[0] / self.atr[1] )

		
>>> obj = zesp()
>>> obj.attr=(8,9)
>>> obj.dodaj()
17
>>> class zesp (object):
	atr =[0,0]
	def __setattr__(self,name,value):
		if(name=="im"):
			self.atr[0]= value
		elif(name=="re"):
			self.atr[1]= value
		elif(name=="attr"):
			self.atr[0]=value[0]
			self.atr[1]=value[1]
	def __str__(self):
		return("%d + %di" % (self.atr[0],self.atr[1]))
	def modul(self):
		print (math.sqrt( self.atr[0]**2 + self.atr[1]**2 ))
	def dodaj(self):
		print ( self.atr[1] + self.atr[0] )
	def odejm(self):
		print ( self.atr[0] - self.atr[1] )
	def mnoz(self):
		print ( self.atr[1] * self.atr[0] )
	def dziel(self):
		print ( self.atr[0] / self.atr[1] )

		
>>> obj = zesp()
>>> obj.attr=(8,9)
>>> obj.modul()
12.041594578792296
>>> a=8
>>> print ("a= "+ a)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    print ("a= "+ a)
TypeError: must be str, not int
>>> print ("a= %d" % a)
a= 8
>>> class zesp (object):
	atr =[0,0]
	def __setattr__(self,name,value):
		if(name=="im"):
			self.atr[0]= value
		elif(name=="re"):
			self.atr[1]= value
		elif(name=="attr"):
			self.atr[0]=value[0]
			self.atr[1]=value[1]
	def __str__(self):
		return("%d + %di" % (self.atr[0],self.atr[1]))
	def modul(self):
		print ("modul= %d" % math.sqrt( self.atr[0]**2 + self.atr[1]**2 ))
	def dodaj(self):
		print ( self.atr[1] + self.atr[0] )
	def odejm(self):
		print ( self.atr[0] - self.atr[1] )
	def mnoz(self):
		print ( self.atr[1] * self.atr[0] )
	def dziel(self):
		print ( self.atr[0] / self.atr[1] )

		
>>> obj = zesp()
>>> obj.attr=(8,9)
>>> obj.modul()
modul= 12
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> class b(a):
	def met(self):
		super(b,self).metoda()
		print("bbb")

		
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    class b(a):
TypeError: int() takes at most 2 arguments (3 given)
>>> class 2D(object):
	
SyntaxError: invalid syntax
>>> class punkt2D(object):
	A= [0,0]
	B= [0,0]
	def __setattr__(self,name,value):
		if(name=="pierwszy"):
			self.A[0]=value[0]
			self.A[1]=value[1]
		elif(name=="drugi"):
			self.B[0]=value[0]
			self.B[1]=value[1]
		
	def odleglosc(self):
		print ( "|AB|= %d" % math.sqrt((self.B[0]-self.A[0])**2 + (self.B[1]-self.A[1])**2) )

		
>>> class punkt3D( punckt2D):
	C= [0,0]
	def __setattr__(self,name,value):
		if(name=="pierwszy"):
			self.A[0]=value[0]
			self.A[1]=value[1]
		elif(name=="drugi"):
			self.B[0]=value[0]
			self.B[1]=value[1]
		elif(name=="trzeci"):
			self.C[0]=value[0]
			self.C[1]=value[1]
	def odleglosc(self):
		super(punkt2D,self).odleglosc()
		print ( "|AB|= %d" % math.sqrt((self.B[0]-self.A[0])**2 + (self.B[1]-self.A[1])**2 + (self.C[1]-self.C[0])**2 ) )

		
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    class punkt3D( punckt2D):
NameError: name 'punckt2D' is not defined
>>> class punkt2D(object):
	A= [0,0]
	B= [0,0]
	def __setattr__(self,name,value):
		if(name=="pierwszy"):
			self.A[0]=value[0]
			self.A[1]=value[1]
		elif(name=="drugi"):
			self.B[0]=value[0]
			self.B[1]=value[1]
		
	def odleglosc(self):
		print ( "|AB|= %d" % math.sqrt((self.B[0]-self.A[0])**2 + (self.B[1]-self.A[1])**2) )

		
>>> class punkt3D( punkt2D):
	C= [0,0]
	def __setattr__(self,name,value):
		if(name=="pierwszy"):
			self.A[0]=value[0]
			self.A[1]=value[1]
		elif(name=="drugi"):
			self.B[0]=value[0]
			self.B[1]=value[1]
		elif(name=="trzeci"):
			self.C[0]=value[0]
			self.C[1]=value[1]
	def odleglosc(self):
		super(punkt2D,self).odleglosc()
		print ( "|AB|= %d" % math.sqrt((self.B[0]-self.A[0])**2 + (self.B[1]-self.A[1])**2 + (self.C[1]-self.C[0])**2 ) )

		
>>> obj = punkt3D()
>>> obj.pierwszy= (3,4)
>>> obj.drugi= (8,5)
>>> class punkt2D(object):
	A= [0,0]
	B= [0,0]
	def __setattr__(self,name,value):
		if(name=="pierwszy"):
			self.A[0]=value[0]
			self.A[1]=value[1]
		elif(name=="drugi"):
			self.B[0]=value[0]
			self.B[1]=value[1]
		
	def odleglosc(self):
		print ( " W 2D odleglosc: |AB|= %d" % math.sqrt((self.B[0]-self.A[0])**2 + (self.B[1]-self.A[1])**2) )

		
>>> class punkt3D( punkt2D):
	
	def __setattr__(self,name,value):
		if(name=="pierwszy"):
			self.A[0]=value[0]
			self.A[1]=value[1]
			self.A[2]=value[2]
		elif(name=="drugi"):
			self.B[0]=value[0]
			self.B[1]=value[1]
			self.B[2]=value[2]
	def odleglosc(self):
		super(punkt2D,self).odleglosc()
		print ( "W 2D odleglosc: |AB|= %d" % math.sqrt((self.B[0]-self.A[0])**2 + (self.B[1]-self.A[1])**2 + (self.B[2]-self.B[2])**2 ) )

		
>>> obj = punkt3D()
>>> obj.pierwszy= (3,4,6)
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    obj.pierwszy= (3,4,6)
  File "<pyshell#185>", line 7, in __setattr__
    self.A[2]=value[2]
IndexError: list assignment index out of range
>>> class punkt2D(object):
	A= [0,0,0]
	B= [0,0,0]
	def __setattr__(self,name,value):
		if(name=="pierwszy"):
			self.A[0]=value[0]
			self.A[1]=value[1]
		elif(name=="drugi"):
			self.B[0]=value[0]
			self.B[1]=value[1]
		
	def odleglosc(self):
		print ( " W 2D odleglosc: |AB|= %d" % math.sqrt((self.B[0]-self.A[0])**2 + (self.B[1]-self.A[1])**2) )

		
>>> class punkt3D( punkt2D):
	
	def __setattr__(self,name,value):
		if(name=="pierwszy"):
			self.A[0]=value[0]
			self.A[1]=value[1]
			self.A[2]=value[2]
		elif(name=="drugi"):
			self.B[0]=value[0]
			self.B[1]=value[1]
			self.B[2]=value[2]
	def odleglosc(self):
		super(punkt2D,self).odleglosc()
		print ( "W 2D odleglosc: |AB|= %d" % math.sqrt((self.B[0]-self.A[0])**2 + (self.B[1]-self.A[1])**2 + (self.B[2]-self.B[2])**2 ) )

>>> obj = punkt3D()
>>> obj.pierwszy= (3,4,6)
>>> obj.odleglosc()
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    obj.odleglosc()
  File "<pyshell#190>", line 13, in odleglosc
    super(punkt2D,self).odleglosc()
AttributeError: 'super' object has no attribute 'odleglosc'
>>> class punkt2D :
	x= [0,0]
	y= [0,0]
	def set( self, x[] , y[] ):
		self.x= x
		self.y= y
	def odleglosc(self):
		print ( " W 2D odleglosc: |AB|= %d" % math.sqrt((self.x[1]-self.x[0])**2 + (self.y[1]-self.y[0])**2) )
		
SyntaxError: invalid syntax
>>> class punkt2D :
	x= [0,0]
	y= [0,0]
	def set( self, x[] , y[] ):
		self.x= x
		self.y= y
	def odleglosc(self):
		print ( " W 2D odleglosc: |AB|= %d" % math.sqrt((self.x[1]-self.x[0])**2 + (self.y[1]-self.y[0])**2) )class punkt2D :
	x= [0,0]
	y= [0,0]
	def set( self, x[] , y[] ):
		self.x= x
		self.y= y
	def odleglosc(self):
		print ( " W 2D odleglosc: |AB|= %d" % math.sqrt((self.x[1]-self.x[0])**2 + (self.y[1]-self.y[0])**2) )
		
SyntaxError: invalid syntax
>>> class punkt2D :
	x= [0,0]
	y= [0,0]
	def set( self, x=[] , y=[] ):
		self.x= x
		self.y= y
	def odleglosc(self):
		print ( " W 2D odleglosc: |AB|= %d" % math.sqrt((self.x[1]-self.x[0])**2 + (self.y[1]-self.y[0])**2) )

		
>>> 
