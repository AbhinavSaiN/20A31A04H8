Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a,b,c=10,20,30
>>> print(b,c,a,sep'?')
SyntaxError: invalid syntax
>>> print(b,c,a,sep='?')
20?30?10
>>> 
>>> print('99','12','2016',sep='-')
99-12-2016
>>> print('99','12','2016',sep='')
99122016
>>> print('99','12','2016',sep=' ')
99 12 2016
>>> 
>>> a=1
>>> b=2
>>> c=3
>>> print(a)
1
>>> print(b)
2
