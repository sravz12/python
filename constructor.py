# it is a member function help to assign value to data members in a class . it will call automatically when a object were assigned
#the default name of constructor is __init__

class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def dis(self):
        print("length:",self.length)
        print("breadth:",self.breadth)
R1=Rectangle(4,5)
R1.dis()