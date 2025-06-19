#type(): Returns a type of given object

#1) integer data type
a=50
print(type(a))       #<class 'int'>

a=-10
print(type(a))       #<class 'int'>

a=0b1111
print(type(a))         #<class 'int'>

a=0xffff
print(type(a))         #<class 'int'>

a=0o122
print(type(a))         #<class 'int'>

# 2)float

b=10.3
print(type(b))        # <class 'float'>

b=1.23e2
print(type(b))        # <class 'float'>


"""3)complex : 1)In python imaginary part declared using 'j' only  
             2)format of complex number is a+bj (a,b will be number)
             3)imaginary part of complex number is always decimal number only """
              
#a=3+2i               SyntaxError: invalid decimal literal

a=3+2j
print(type(a))         #<class 'complex'>

# a=3+j2                   # NameError: name 'j2' is not defined

print(a.real)
print(a.imag)

a=0b1111+2j
print(a)                   # (15+2j)

a=0x1111+2j
print(a)                 #(4369+2j)   

# a=2+ob1111j           NameError: name 'ob1111j' is not defined

#4) boolean
a=True
print(type(a))                 #<class 'bool'>

# a=true                       # NameError: name 'true' is not defined.

print(True/True)

print(True/False)            # ZeroDivisionError: division by zero

print(True*False)

print(99/True)

print(0==False)


#WAP to perform artihmatic operation on two complex number 
a=3+5j
b=5+8j
print(a+b)
print(a-b)
print(a*b)
print(a/b)




