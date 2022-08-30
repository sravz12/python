class Bank:
    def getdata(self):
        self.name=input("Enter the name")
        self.accno=int(input("enter the accno"))
        self.type=input("enter the type of acc")
        self.balance=0
    def printdata(self):
        print("name:",self.name)
        print("accno",self.accno)
        print("type",self.type)
        print("balance:",self.balance)
    def deposit(self):
        d=int(input("enter the deposit"))
        self.balance=self.balance+d
    def withdraw(self):
        w=int(input('enter the amount to be withdraw'))
        if self.balance>=w:
            self.balance=self.balance-w
            print("new balance:",self.balance)
        else:
            print("Insufficient balance")
    def display(self):



res=Bank()
res.getdata()
res.printdata()
res.methods()
res.printmethods()
