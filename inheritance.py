#inheritance
#single inheritance


# class Person:
#     def getdata(self):
#         self.name=input("enter the name")
#         self.voterid=int(input("enter the id"))
#     def dis(self):
#         print("Name:",self.name)
#         print("Voter id:",self.voterid)
# class Employee(Person):
#     def salary(self):
#         self.salary=int(input("enter the salary"))
#     def printsalary(self):
#         print("salary:",self.salary)
# Emp1=Employee()
# Emp1.getdata()
# Emp1.salary()
# Emp1.printsalary()
# Emp1.dis()


#overriding   (the same function name occure both parent class and child class)
#
# class Person:
#     def getdata(self):
#         self.name=input("enter the name")
#         self.voterid=int(input("enter the id"))
#     def dis(self):
#         print("Name:",self.name)
#         print("Voter id:",self.voterid)
# class Employee(Person):
#     def getdata(self):
#         super().getdata()                            #avoid overriding(super.function name)
#         self.salary=int(input("enter the salary"))
#     def dis(self):
#         super().dis()
#         print("salary:",self.salary)
# Emp1=Employee()
# Emp1.getdata()
# Emp1.dis()

#using constructor


class Person:
    def __init__(self):
        self.name=input("enter the name")
        self.voterid=int(input("enter the id"))
    def dis(self):
        print("Name:",self.name)
        print("Voter id:",self.voterid)
class Employee(Person):
    def __init__(self):
        super().__init__()
        self.salary=int(input("enter the salary"))
    def dis(self):
        super().dis()
        print("salary:",self.salary)
Emp1=Employee()
Emp1.dis()


