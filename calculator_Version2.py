class calculator:
    def __init__(self,x,y):
        self.val1=x
        self.val2=y
    def add(self):
        return (self.val1+self.val2)
    def sub(self):
        return(self.val1-self.val2)
    def mul(self):
        return(self.val1 * self.val2)
    def div(self):
        return(self.val1/self.val2)
    def pow(self):
        return(self.val1**self.val2)
    def AND(self):
        return(self.val1 & self.val2)
    def OR(self):
        return(self.val1 | self.val2)
    def NOT(self):
        return (~self.val1)
    def NAND(self):
        return(self.val1 & ~self.val2)

if __name__ == "__main__":
    print("choose opreatin you need")
    print("1 is for add")
    print("2 is for subtract")
    print("3 is for multiply")
    print("4 is for division")
    print("5 is for power")
    print("6 is for AND")    
    print("7 is for OR")
    print("8 is for NOT")
    print("9 is for NAND")    
    while True:
        x=int(input("Enter the first number: "))
        y=int(input("Enter the second number: "))
        obj=calculator(x,y)
        ch=input("Enter your option: ")
        if ch in ('1','2','3','4','5','6','7','8','9'):
            if ch=='1':
                print("sum of the numbers is: ",obj.add())
            elif ch=='2':
                print("Diffrence of the numbers is: ",obj.sub())
            elif ch=='3':
               print("Product of the number is",obj.mul())
            elif ch=='4':
               print("Division of the number is: ",obj.div())
            elif ch=='5':
                print("Power of the number is: ",obj.pow())
            elif ch=='6':
                print("AND of the numbers is: ",obj.AND())
            elif ch=='7':
                print("OR of the numbers is: ",obj.OR())
            elif ch=='8':
                print("NOT of the numbers is: ",obj.NOT())
            elif ch=='9':
                print("NAND of the numbers is: ",obj.NAND())
            loop=input("calculation needed again: ")
            if loop=="no":
                break
    else:
        print("Invalid input")

    
    
    
    
    

