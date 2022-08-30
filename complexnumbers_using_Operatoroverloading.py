class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __sub__(self, other):
        newa=self.a-other.a
        newb=self.b-other.b
        return complex(newa,newb)
    def __str__(self):
        return "({0}+{1}j)".format(self.a,self.b)

p1=complex(6,7)
p2=complex(2,3)
print(p1-p2)
