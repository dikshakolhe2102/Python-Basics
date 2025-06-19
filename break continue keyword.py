#  #break
for i in range(1,101):
     if i == 50:
         break
     print(i,end=" ")

# continue
for i in range(1,101):
     if i == 50:
         continue
     print(i,end=" ")

#for with else
for i in range(10):
     print(i)
else:
    print("Else part")
print("End of loop")


#break with else
for i in range(1,31):
     if i == 20:
         break
     print(i,end=" ")
else:
    print("Else part")
print("End of loop")


# #continue with else
for i in range(1,31):
     if i == 20:
        continue
     print(i,end=" ")
else:
    print("done")
print("after loop")


# Pass :The pass statement is used as a placeholder for future code. 
# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
# Empty code is not allowed in loops, function definitions, class definitions, or in if statements
for i in range(10):
    pass


