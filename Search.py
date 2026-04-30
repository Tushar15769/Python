list_1=[1 ,4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ,100 ]
i = 0
x = int(input("Enter the number from the list : "))

while(i < len(list_1)):
    if(list_1[i] == x):
      print(f"{x} found at index {i}")
      break
    i=i+1

print("Exit the loop")  