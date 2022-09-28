n=int(input("enter the values:"))
list=[]
even=0
odd=0
for i in range(0,n):
    b=int(input("enter the elements in list:"))
    list.append(b)
print(list)
for i in list:
    if i%2==0:
       even=even+(i**2)
    else:
        odd=odd+(i**2)
print("even sum squares",even)
print("odd sum squares",odd)
                
