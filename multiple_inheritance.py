#a-> c <-b

class Mark:
    def getdata(self):
        self.m=int(input("enter the mark"))
    def printdata(self):
        print("mark:",self.m)
class Gracemark:
    def getmark(self):
        self.gm=int(input("enter the gracemark"))
    def printgm(self):
        print("Gracemark:",self.gm)
class Grade(Mark,Gracemark):
    def calculate(self):
        Total=self.m+self.gm
        p=Total/500*100
        if p>=80:
            print("A grade")
        elif p>=70:
            print("B grade")
        elif p>=60:
            print("C grade")
        else:
            print("failed")
Result=Grade()
Result.getdata()
Result.getmark()
Result.printdata()
Result.printgm()
Result.calculate()