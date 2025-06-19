# escape sequences

#\n=new line 
a="abc\npqr"
print(a)

#\t tab
print("abc12344\tpqr")

#\r= carriage return
print("abc\rpqr")
print("abc\rpq")

a="abcpqr\rxy"
print (a)

#\b=backspace
print("abc\bpqr")
print("ABC12344\bPQR")

#\v  = vertical tab
print("abc12344\vpqr")

#\0=null 
print("abc12344\0pqr")

#\U=unicode 8 digits
print("abc12344\U00000022 pqr")
print("\U0000002A")

#\u
print("abc123\u0100pqr")

#prevent escape sequencce

print(r"C:\Users\yashr\OneDrive\Desktop\pythonclass3")

print("C:\\Users\\yashr\\OneDrive\\Desktop\\pythonclass3")