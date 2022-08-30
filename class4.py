class Rectangle:
    def read(self,l,b):
        self.length=l                 #public data member
        self.__breadth=b              #__variable name private data member
    def dis(self):
        print("length:",self.length)
        print("breadth:",self.breadth)
R1=Rectangle()
R1.read(10,5)
R1.dis()
R1.length
R1.__breadth
