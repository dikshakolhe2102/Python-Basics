# string declare in single,double and triple quotes
a="python programming"
print(a)
a='Python Programing'
print(a)
print(type(a))
a="""A python Programming 
python is a programming language
pyhon is a programming language """
print(a)
print(type(a))

#slicing
#syntax - stringname[start:end-1:step]
#         start :starting index (included)
#         end :ending index (excluded)
#         step :default value is 1

a="python programming"
print(a[0])
print(a[-1])
print(a[-2])
print(a[2:5])
print(a[2:])
print(a[:2])

print(a[:])
print(a[-5:-1])
print(a[2:-5])
print(a[2::2])
print(a[::2])
print(a[::-1])
print(a[::])
print(a[-1:-5])     

print(a[2:5:2])
print(a[1:10:3])

 # type: ignore