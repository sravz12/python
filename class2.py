#Rectangle
#length
#breadth
#getdata
#displaydata()
#area()
class Rectangle:
    def getdata(self):
        self.length=int(input("enter the length"))
        self.breadth=int(input("enter the breadth"))
    def display(self):
        print("length:",self.length)
        print("breadth:",self.breadth)
    def area(self):
        a=self.length*self.breadth
        print("area:",a)
rec1=Rectangle()
rec1.getdata()
rec1.display()
rec1.area()

