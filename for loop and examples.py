#for loop
#syntax:
#for variable in sequence:
         #statement1
         #statment2

#shorthand for loop
#for variable in sequence: stat1

#examples:
#write a python prog. to print cube of first 100 even numbers
for a in range(2,201,2):
     c=a**3
     print("the cube of", a,  "is:", c)

#Wap to find the sum of series of a number upto nth terms
n=int(input("Enter a number:"))
nth_term=int(input("Enter a term:"))
n1=n
sum=0
for i in range(0,nth_term):
         sum=sum+n
         n=n*10+n1
print(sum)


n=int(input("Enter a number:"))
nth_term=int(input("Enter a term:"))
n1=n
sum=0
for i in range(0,nth_term):
         print(n, end="+")
         sum=sum+n
         n=n*10+n1
print("=",sum)

#to take input from user and print n natural numbers in descending order using for loop
n=int(input("Enter a number:"))
for i in range(n,0,-1):
     print(i)

# range(start,end,step)
print(range(10))
print(range(1,10))
print(range(1,10,2))
for i in range(10):
    print(i , end = "")

    
#for vriable in sequenace
    #for i in range(6)

a=10
for i in range(6):
    print("hello")

#program too cube of first 100 even numbers using for loop

for i in range(2,201,2):
    i%2==0
    
    
    cube=i**3
    #sum=sum+i
    print(f"cube of{i} ",cube)
    
    #print(i)
# ANOTHER WAY
for i in range(2,10,2):
    print(i**3,end=" ")
   # not yet understand print("+" * (  2-i) )

for i in range(2,200,2):
    print(i**3,end=" ")

# program to finding the sum of series of a number upto n terms.

#example load
num=int(input("Enter number"))
term=int(input("Enter term"))
sum=0
while num>0 and n>sum:
    sum=sum+num
    num=sum+num*10
print(sum)


#another way

n,t=2,3
n1=n
sum=0
for i in range(0,t):
    sum+=n
    print(n,end="")
    if i!=t-1:
        print("+",end="")
    n=n*10+n1
print("=",sum)

#another way

n, t = 2, 3
n1 = n
sum = 0

# First loop to calculate and print terms with '+' (except after last term)
for i in range(t):
    sum += n
    print(n, end='')
    print("+" * (t - i - 1), end='')  # This prints '+' if not the last term
    n = n * 10 + n1

print("=", sum)


# prgram to print natural numbers in decending numbers using for loop

n=int(input("Enter your number"))

for i in range(n,-1 ):
    print(i)

