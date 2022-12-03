a = int(input("enter a number"))
b = int(input("enter another number"))
c = input ("enter an operator")
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='**':
    print(a**b)
elif c=='/':
    print(a/b)
while input ("do you want to continue"):
    if ("no"):
        break
else:
    return
