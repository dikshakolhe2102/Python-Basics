# id,type,len
# general purpose functions of string


a="Python@12345"
b="Python@12345"

print("a==b:",a==b)
print("a!=b:",a!=b)
print("a>=b:",a>=b)
print("a<=b:",a<=b)
print("a<b:",a<b)
print("a>b:",a>b)



# program to take take a 2 string from user and check whether they are equal or not

string1=input("Enter a string:")
string2=input("Enter asecond string:")

# print("Equal ",string1==string2)

if string1==string2:
    print("equal:")
else:
    print("not equal:")


a="hElLo WoRlD"

print(a*3)
print("hi"+a)
print("length",len(a))

# strings methods

print("capitalize",a.capitalize())

print("capitalize",a.lower())


print("capitalize",a.upper())

print("capitalize",a.swapcase())


print("capitalize",a.title())

print("capitalize",a.casefold())


s1="Straeß"

print(s1.lower())
print(s1.casefold())


# center    width,sign
print(s1.center(10))
print(s1.center(150,'*'))
print("count(string):","126547852121".count("2"))
print("count(string):","126547852121".count("2",5,10))



print("Endswith(suffix)","458745211387".endswith("1"))
print("Endswith(suffix,start,end)","458745211387".endswith("3",5,10))

print("Endswith(prefix)","458745211387".endswith("1"))
print("Endswith(prefix,start,end)","458745211387".endswith("1",5,10))


# letters pattern 


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





# 31/05/2025

# Encoding and decoding functions


# encode(encoding errors):encodes a stringn into bytes using a spacified encoding and error handling scheme.

text="pythón"
print(text.encode('utf-8'))# b'pyth\xc3\xb3'

print(text.encode('ascii')) # raises unicode encoder error

#ignore non ascii
print(text.encode('ascii',errors='ignore'))  #b'pythn'

#replace non ascii
print(text.encode('ascii',errors='replace'))   #b'pyth?n'

#'xmlcharrelfreplace'(replaces with xml character reference)
print(text.encode('ascoo',errors='xmlcharrefreplace')) #b'pyth&#243;

#'backslashreplace'(replaces with python-style unicode escape)
print(text.encode('ascii',errors='backslashreplace'))  # b'pyth\\xf3



# 'namereplace'(python 3.5+- replaces with \n{...}names)
print(text.encode('ascii',errors='nameplace'))  # b'pyth\\N{LATIN SMALL LETTER 0 WITH ACUTE}


sum=0
avg=0
count=0
i="Python@123987P"

# while int(i)<len(i):
for r in i:
    if r.isdecimal():
        # print(r)
        sum=sum+int(r)
        
        
        count+=1
avg=sum/count
print("sum is:",sum)
print("avg is :",avg)
print("count is:",count)



#
a="Python123 programing abc12"

print(len(a.split(" ")))
for i in a:
    x=a.split()
    for x in a:
        if x.isalnum():
            count+=1


count=0
for r in a():
    if r.isalnum():
        print(" ")



text = "Python123 programing abc12"
text=input("Enter a text:")
# Step 1: Split the string by '-'
split_text = text.split("-")

# Step 2: Get the first part (after split)
first_part = split_text[0]  # In this case: 'Python123 programing abc12'

# Step 3: Get the first word from that part
first_word = first_part.split()[0]  # Result: 'Python123'

# Step 4: Detect and count only alphabetic characters
alphabet_count = 0
n_count=0
for char in first_word:
    if char.isalpha():
        if char.isdeciaml():
            n_count+=1
        alphabet_count += 1

# comparison of string
a = "Python"
b = "python"

print("a==b", a==b)
print("a!=b", a!=b)
print("a>b", a>b)
print("a<b", a<b)
print("a>=b", a>=b)
print("a<=b", a<=b)

#
a = "Python@12345"
b = "Python@12345"

print("a==b", a==b)
print("a!=b", a!=b)
print("a>b", a>b)
print("a<b", a<b)
print("a>=b", a>=b)
print("a<=b", a<=b)


#traversing of string
a="hello world"
for i in a:
    print(i,end="")

#built-in  method of strings
a="hElLo WoRlD"
print(a*3)
print("hi "+a)
print("length of string is : ", len(a))

#String Methods For Manipulating Case
print("capitalize() : ",a.capitalize())
print("upper(): ",a.upper())
print("lower(): ",a.lower())
print("swapcase(): ",a.swapcase())
print("title: ",a.title())
print("casefold: ",a.casefold())

s1 = "Straße"     # German word for "street" 
print("lower with german: ",s1.lower())    
print("casefold with german: ",s1.casefold())

print("Center(width): ",a.center(10))
print("Center(width,fillchar): ",a.center(10,'*'))
print("count(string) : ","12345634432122".count("2"))
print("count(string,start,end) : ","12345634432122".count("2",5,10))

# endswith() : It returns True if a string ends with the specified suffix.otherwise it returns False.
print("endswith(suffix) : ","123453578931".endswith("1"))
print("endswith(suffix,start,end) : ","123453578931".endswith("3",5,10))
# startswith() : It returns True if a string starts with the specified prefix.otherwise it returns False.
print("startswith(prefix) : ","123453578931".startswith("1"))
print("startswith(prefix,start,end) : ","123453578931".startswith("3",5,10))


# returns the index of first occurrence of the substring (if found),otherwise it returns -1.
a="h e l l o  w o r l d "
print("find(substring) : ",a.find("e"))
print("find(substring,start,end) : ",a.find("l",2,4))

# returns the index of last occurrence of the substring (if found),otherwise it returns -1.
print("rfind(substring) : ",a.rfind("l"))
print("rfind(substring,start,end) : ",a.rfind("l",2,4))

# returns the index of first occurrence of the substring (if found),otherwise it raises ValueError.
print("index(substring) : ",a.index("e"))
print("index(substring,start,end) : ",a.index("l",2,4))

# returns the index of last occurrence of the substring (if found),otherwise it raises ValueError.
print("rindex(substring) : ",a.rindex("l"))
print("rindex(substring,start,end) : ",a.rindex("l",2,4))

# isalnum() : It returns True if all characters in the string are alphanumeric (letters and numbers),otherwise it returns False.
print("isalnum(): ","12345a".isalnum())

print("isalpha() : ","12345a".isalpha())

#isdecimal() : Most strict; only decimal digits, no superscripts, fractions, or Roman numerals.
print("isdecimal() : ","12345a".isdecimal())

# isdigit(): includes decimal digits plus digits like superscript ² (²), and some Unicode digits.
print("isdigit() : ","12345².".isdigit())


#isnumeric(): includes decimal characters, digits, and fractions
print("isnumeric() : ","12345².".isnumeric())

#isidentifier(): returns True if the string is a valid Python identifier (variable name),otherwise it returns False.
print("isidentifier : ", a.isidentifier())
print("isidentifier : ", "12abc".isidentifier())

print("islower(): ",a.islower())
print("isupper(): ",a.isupper())
print("istitle(): ",a.istitle())
print("isspace(): ",a.isspace())

# isprintable() :returns True if all characters in the string are printable,otherwise False.
print("isprintable(): ",a.isprintable())

#replace(): replaces each matching occurrence of a substring with another string.
print("replace(old, new) : ",a.replace("l","L"))
print("replace(old, new, count) : ",a.replace("l","@@",2))

a="Hello World"
# split(separator, maxsplit):breaks down a string into a list of substrings using a chosen separator.
print("split(separator) : ",a.split())
print("split(separator, maxsplit) : ",a.split("l"))
print("split(separator, maxsplit) : ",a.split("l",2))

# rsplit(separator, maxsplit):breaks down a string into a list of substrings using a chosen separator,starting from the right.
print("rsplit(separator) : ",a.rsplit())
print("rsplit(separator, maxsplit) : ",a.rsplit("l"))

# partition(separator): splits a string into three parts: the part before the separator, the separator itself, and the part
print(a.partition("l"))
print("abc@gmail@.com".partition("@"))

# rpartition(separator): splits a string into three parts,starting from the right.
print("abc@gmail@.com".rpartition("@"))


# join(iterable): joins elements of an iterable (like a list or tuple) into a single string,using the string as a separator.
print("_python_".join("Python"))
print("$_".join("Python"))

# strip(chars): removes leading and trailing characters (default is whitespace) from a string.
print("      Python       ")
print("           Python       ".strip())
print("sPythonsss".strip('s'))

# lstrip(chars): removes leading characters (default is whitespace) from a string.
print("    Pythonsss".lstrip())
print("Pythonsss".lstrip("S"))

# rstrip(chars): removes trailing characters (default is whitespace) from a string.
print("Pythonsss      ".rstrip())
print("Pythonsss".rstrip("S"))

# rjust(width, fillchar): right-justifies a string within a specified width,using a fill character (default is space).
print("Python".rjust(20))
print("Python".rjust(20,'*'))
# ljust(width, fillchar): left-justifies a string within a specified width,using a fill character (default is space).
print("Python".ljust(20))
print("Python".ljust(20,'*'))

# zfill(width): pads a numeric string with zeros on the left,up to a specified width.
print("zfill(width):","python".zfill(20))

# translate(table): replaces characters in a string based on a translation table created by str.maketrans().
a="python"
b=str.maketrans('y','@')
print(b)
print(a.translate(b))
print(a)
b=a.maketrans('y','@','o')
print(b)
print(a.translate(b))
print(a.isprintable())

# expandtabs(tabsize): replaces tab characters with spaces,using a specified tab size.

a= "H\te\tl\tl\to"
print(a)
print("expandtabs(): ",a.expandtabs())
print("expandtabs(tabsize): ",a.expandtabs(2))
print("expandtabs(tabsize): ",a.expandtabs(4))
print("expandtabs(tabsize): ",a.expandtabs(10))



#encode(encoding, errors): encodes a string into bytes using a specified encoding and error handling scheme.
text = "pythón"
print(text.encode('utf-8'))  # Output: b'pyth\xc3\xb3'

print(text.encode('ascii'))  # Raises UnicodeEncodeError       


# Ignore non-ASCII
print(text.encode('ascii', errors='ignore'))  # b'pythn'

# Replace non-ASCII
print(text.encode('ascii', errors='replace'))  # b'pyth?n'

# 'xmlcharrefreplace' (replaces with XML character reference)
print(text.encode('ascii', errors='xmlcharrefreplace')) # b'pyth&#243;

# 'backslashreplace' (replaces with Python-style Unicode escape)
print(text.encode('ascii', errors='backslashreplace')) # Output: b'pyth\\xf3'

# 'namereplace' (Python 3.5+ — replaces with \N{...} names)
print(text.encode('ascii', errors='namereplace'))  # Output: b'pyth\\N{LATIN SMALL LETTER O WITH ACUTE}'