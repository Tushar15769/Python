a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

if ( a >= b and a >= c ):
  print("First number is the greatest", a)
elif ( b >= c ):
  print("Second number is greatest", b)  
else:
  print("Third number is the greatest", c)  