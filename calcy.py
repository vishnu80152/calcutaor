#calculator created by vishnu 
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def pow(a,b):
    return a**b
print("choose opreatin you need")
print("1 is for add")
print("2 is for subtract\n")
print("3 is for multiply\n")
print("4 is for division\n")
while True: 
    n1,n2=float(input("Enter the first number: ")),float(input("Enter the second number: "))
    ch=input("Enter your option: ")
    if ch in ('1','2','3','4','5'):
        if ch=='1':
            print(add(n1,n2))
        elif ch=='2':
           print(sub(n1,n2))
        elif ch==3:
            print(mult(n1,n2))
        elif ch==4:
            print(div(n1,n2))
        loop=input("calculation needed again: ")
        if loop=="no":
            break
    else:
        print("Invalid input")
