a = (input("enter a value of a:"))
b = (input("enter a value of b:"))
def check(a,b):
    if(sorted(a)==sorted(b)):
        print("string is anagram")
    else:
        print("string is not a anagram")
check(a,b)
