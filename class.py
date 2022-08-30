class Student:
    def read(self):
        self.rollno=int(input("enter the rollno"))
        self.name=input("enter the name")
    def display(self):
        print("rollno:",self.rollno)
        print("name:",self.name)
#object=classname()
s1=Student()
s1.read()
s1.display()
s2=Student()
s2.read()
s2.display()
