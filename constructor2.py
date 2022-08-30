class Person:
    def __init__(self,n,v):
        self.name=n
        self.voterid=v
    def dis(self):
        print("name:",self.name)
        print("voterid:",self.voterid)
class Employee(Person):                 #child class
    def __init__(self,n,v,s):           #anu,1,20000
        super().__init__(n,v)           #anu,1
        self.salary=s
    def print(self):
        super().dis()
        print("salary:",self.salary)
R1=Employee('anu',1,20000)
R1.print()
