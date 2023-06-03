import math
x = int(input("Press enter a number:"))
y = int(input("Press enter a number:"))
print("x to the power of y is", x**y)
if x > 0:
    print("x to the log of 2 is", math.log(x,2))
elif x == 0:
    print("x to the log of 2 is undefined")
else:
    print("The number stored in x can't be processed")