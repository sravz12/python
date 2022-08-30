#Polymorphism
#Function Overloading ->not support in python
#Operator overloading

class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        newa=self+aother.a
        newb=self.b+other.b
        return Point(newa,newb)
    def __str__(self):
        return "({0},{1})".format(self.a,self.b)
P1=Point(1,2)
P2=Point(2,3)
print(P1+P2)
