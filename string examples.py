
#letters pattern: 
# 29/05/2025

# to print take a string from user and print even part and odd part differently using slicing

s=input("Enter your string:")
# count=2

print(s[0: :2])
print(s[1: :2])



s="python"

print(s.find('y'))   # if true returns 1
print(s.rfind('y,2,5'))   # if false then returns -1
print(s.index('t'))
print(s.index('t',2,5))
# if not then value error
print(s.rindex('t'))
print(s.rindex('t',2,5))


s1=s.replace('p','r')
print(s1)
print(s.replace('p','r'))
print(s.replace('p','r',2))   #2 is optional i.e. count
print(id(s))
print(id(s1))



s='Python'
print(s.isalnum())  # alpha +  numbers
print(s.islower())
print(s.isupper())
print(s.istitle())
print(s.isspace())   
print(s.isalpha())  # all aphabets
print("\u1255".isdecimal())  # 0to 9
print(s.isdigit())    #0 to 9, sub,sup,unicode
print(s.isnumeric())    #0 to 9, sub,sup,fraction,roman


print("abcper".isprintable())
print("abc\tper".isprintable())
print("abcper".isidentifier())
print("123abcper".isidentifier())
print("_abcper".isidentifier())
print("abc$per".isidentifier())
print("-abcper".isidentifier())


u='sdfgh$fghj$122'
print(u.split())
print(u.split('$',2))
print(u.split('$'))



u="sdfgh$erty231"
print(u.partition("$"))


# to check given string is palindrome or not

n=input("Enter a number:")

print("Palindrome ",n[::]==n[::-1])

n=input("Enter a number:")

if n==n[::-1]:
    print("pali")
else:
    print(("not"))


#   get astring made up of the frist two and last two characters of a given string
# if str len <2  then print empty

n=input("Enter a number:")
if len(n)<2:
    print("empty string:")
else:

    s=n[0:2]
    p=n[:2:-1]

    print(s+p)



#to add ing at the end of the given string (len should be atleast 3)
# if given str aleady ends with ing then + ly at end
# if lenstr<3 print original string 



s=input("Enter a string:")

if s.endswith("ing"):
    print(s[:-3]+"ly")

if len(s)<=3:
    print(s)
# 30/05/2025


print("asdvb@ghm.com".just(20))
print(" ".rjust(20,'*'))

print("python".ljust(20))
print("python".ljust(20,'*'))

print("     python    ")
print("      python    ".strip())
print("sssspython".strip('s'))
print("python".lstrip())
print("    python".lstrip('s'))

print("python    ".rstrip())
print("python".rstrip('s'))


a="Python"
print("@@@@".join("python0"))

print("python".zfill(20))

b=a.maketrans('y','@')
print(b)
print(a.trnaslate(b))
print(a)
b=a.maketrans('y','@','o')
print(b)
print(a.trnaslate(b))


a='f\th\thd\tdf'

print(a[:-3].expandtabs(4))

# #  program to take a string from a user and check whetger the string upper oot not 
# if yes==convert lower case


n=input("ENter a string:")
if n.isupper():
    print(n.lower())

else:
    print(n)



# # to take a 2 strings from user and if ==replace first ch both sttring ($)
# else replace first ch with @


n=input("Enter a string:")
s=input("Enter a string:")
if n[0]==s[0]:
    print(s.replace(s[0],'$'))
    print(n.replace(n[0],'$'))

else:
    print(s.replace(s[0],'@'))
    print(n.replace(n[0],'@'))




#  to count digits alphabets ,special, symbols in a guiven string 

count=0
count1=0
count2=0

n=input("Enter a string")

for i in n:
    if i.isdigit():
        print()
        count+=1
    elif i.isalpha():
        print()
        count1+=1
    else:
        print()
        count2+=1
print("digits:",count,"alphabets:",count1,"special symbols:",count2)



# to take a string from user 
# and take a character from user
#  and find whether given character is in string or not
# if yes==replace ch  with # and fill given string with 3'0
# else :  fill 5'0

n=input("Enter string:")
s=input("Enter a character")

if s in n:
     p=n.replace(s,'#')
    #  print(n,p.zfill(10))
     print(p.zfill(len(s)+10))
else:
    print(n.zfill(len(n)+5))
    

    


1.
# # to string from user and check given string lower or not
# if yes==count first ch of string and split using [0] character
# else:
#     convert lowercase and partition using [1]

count=0
string=input("Enter a string:")

if string.islower():
    if string[0] in string:
        print(string.split(string[0]))
        print(string.count(string[0]))
else:
    part=string.lower()
    print(part.partition(part[1]))
    print(string.count(string[1]))

# 2.string[0]===replace string ==0 with $


string=input("Enter a string:")
# re=string[0]
print(string.replace(string[0],'$'))