# discovereed in 1989
# by guido van rossum,
# python name inspired by a cartoon 


# 111.we can write on console and run it ,

# python is loosely type launguage
# --it is dyanamic language
# it is open source


5+6
11

#First code
#Hello program
print("hello")
#hello
 
#python identifiers declaration rules
#1)It is combination of Alphanumeric character or underscore(_)
abc=10
print(abc)
#10
a_b_c=20
print(a_b_c)
#20
abc123=20
print(abc123)
#20

#2)It can't  be start with a digit.
#1abc=10              //SyntaxError

#3)They should not contain  whitespace and speical characters
#abc pqr =10            //SyntaxError
#abc@pqr =100            //SyntaxError

# 4) They are case sensitive 
a=50
A=50

#5) They should not be  a keywords
# if=10                 SyntaxError: invalid syntax


If=99
print(If)
99
_x=56
_x
56


# 22.for importing keyword 
#  import keyword

#  keyword.kwlist
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
#  'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#  'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']



# 33. for  checking a types of 
#  a=-10
#  type(a)
# <class 'int'>
#  a=0b1111
#  type(a)
# <class 'int'>
#  a=0x111111
# type(a)
# <class 'int'>
#  b=10.3
#  type(a)
# <class 'int'>
#  type(b)
# <class 'float'>

  
# 33.comlex numbers
# real number + imaginary number
# imaginary number showed by "j"
 
#  a=3+2j
#  type(a)
# <class 'complex'>
#  a.real
# 3.0
#  a.imag
# 2.0
#  c=0b1111+2j
#  type(c)
# <class 'complex'>


 
#  e=3+2556j
#  f=5+8694j
#  e+f
# (8+11250j)
#  e-f
# (-2-6138j)
#  e*f
# (-22221849+38862j)
#  e/f
# (0.29399596042429266-0.0001759857600504413j)
#  a=True+True
#  a
# 2

