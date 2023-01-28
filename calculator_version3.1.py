class calculator:
    def __init__(self):
        self.val1=None
        self.val2=None
        self.operation=None
        while True:
            self.operator()
            if self.operation in ("+","-","*","/"):
                self.getvalues()
                if self.operation=="+":
                    self.add()
                elif self.operation=="-":
                    self.sub()
                elif self.operation=="*":
                    self.mul()
                elif self.operation=="/":
                    self.div()
                loop=input("you need to continue calculation: ")
                if loop=="no":
                    break
            else:
                print("Invalid operation")
        
    def getvalues(self):
            self.val1 = float(input("enter first number: "))
            self.val2 = float(input("enter second number: "))
        
    def operator(self):
            self.operation=input("operation:")
        
    def add(self):
        print(self.val1+self.val2)
        
    def sub(self):
        print(self.val1-self.val2)
        
    def mul(self):
        print(self.val1*self.val2)
        
    def divide(self):
        print(self.val1/self.val2)
        
if __name__ == "__main__":
    obj=calculator()