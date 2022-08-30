class Circle:
    def read(self):
        self.radius=int(input("enter the radius"))
    def display(self):
        print("radius",self.radius)
    def area(self):
        a=3.14*self.radius*self.radius
        print("area is:",a)
C1=Circle()
C1.read()
C1.display()
C1.area()