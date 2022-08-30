class Person:
    def getdata(self):
        self.name=input("enter the name")
        self.code=int(input('enter the code'))
    def printdata(self):
        print("name:",self.name)
        print("code",self.code)
class Account(Person):
    def pay(self):
        self.pay = int(input("member pay"))
    def printpay(self):
        print("pay:", self.pay)
class Admin(Account):
    def member(self):
        self.exp=int(input("enter the experience"))
    def printmember(self):
        print("Experience:",self.exp)
class Employee(Admin):
    pass
    # def EployeeDtails(self):
    #     self.getdata()
    #     self.pay()
    #     self.member()
    # def printemployee(self):
    #     print("name:",self.name)
    #     print("code:",self.code)
    #     print("pay:",self.pay)
    #     print("Experience:",self.exp)
res=Employee()
res.getdata()
res.pay()
res.member()
res.printdata()
res.printpay()
res.printmember()



