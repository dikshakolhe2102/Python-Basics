# while Loop
# syntax
# while condition:
#    print()
# or
# while(condition):stat1;stat2


i=1
while(i<=100):
    print("Hello")# ans=100 times hello and end
    i=i+1
print("End")

i=1
while(i<=100):
    print("Hello")# ans=infinite times hello and once end
print("End")

#examples

#create table

number=int(input("Enter a number:"))
i=0
while i<=10:
    number+=number*i
    
    i=i+1

    print(f"{number}*{i}:")
    print(number)
    


n=5
i=10
while(i>=1):
    print(n,"*",i,"=",n*i)
    i=i-1
    




number=int(input("Enter a number"))
rev=0
rem=0

while(number>0):
    rem=number%10
    rev=rev*10+rem
    number=number//10
    
print(rev)


#program is palindrome or not

number=int(input("Enter a number"))
n2=number
rev=0
rem=0

while(number>0):
    rem=number%10
    rev=rev*10+rem
    number=number//10
    
print(rev)

if(n2==rev):
    print("palindrome")


#while statement
#while condition:
    #   stat1
    #   stat2
    #   stat3

#examples of while loop
i=10
while i<=100:
     print("hello")
     i=i+1
print("end")     

i=10
while i<=100:
     print("hello")
print("end")     

i=1
while True:
      i=input("enter a num")
      print(i)
print("End")


# while(condition):stat;stat2

# to print first 1000 natural numbers
i=1
while(i<=1000):
      print(i)
      i=i+1

# to print even number

i=2
while(i<=1000):
      i
      print(i)
      i=i+1

#while loop example
no1=int(input("enter a no:"))
no2=int(input("enter a no:"))
while(no1<no2):
    if(no1%2==0):
        print(no1)
        no1+=1
        
no=int(input('enter a no :'))
# rev=0
n2=no
sum=0
while(no>0):
    rem=no%10
    sum=sum+rem*rem*rem
    no=no//10
    if(sum==n2):
        print("it is amstrong no")
    else:
        print("it is not amstrong no")


# a=int(input("enter a no:"))
sum=0
b='y'
while(b=="y" or b=="Y"):
    a=int(input("enter a no:"))
    b=input("do u want to continue (y/n)")
    sum=sum+a
    print(sum)

