pat=int(input('enter the num:'))
print("pattern")
for i in range(1,pat):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
