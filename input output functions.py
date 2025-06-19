#print():Print a new line
print()

#print(String)
print("python")
print("")
print("programming")

#print(variable)
a="Python"
print(a)

#print(string,variable)
a="python"
b="programming" 
c=" "
print(" ",a,b,c)

#print(string+string): concatination of string
print("python"+"programming")

#print(variable,sep=):default value of separetor is whitespace
print(a,b,c,sep=':')
print(a,b,c,sep='')

#example
p=111
q=222
r=3
print(p,q,r,sep='###')

#print(variable ,end)
print(a,b,c,end='@')

#print(varaible,sep,end)
print(a,b,sep='!',end='#')

#use inverse, double quote inside single quote (single quote inside single quote not working and same for double quote) 
print("'python' program")
print('"python" program') 

#input():  use to take input from user and it returns a string value 
print("Enter a name")
s=input()
print(s)
print(type(s))

#input(string)
s=input("Enter a number")
print(s)
print(type(s))

