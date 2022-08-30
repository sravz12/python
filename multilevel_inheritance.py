# class Student:
#     def getdata(self):
#         self.roll=int(input("Enter the roll number"))
#         self.name=input("enter the name")
#     def printdata(self):
#         print("Rollno:",self.roll)
#         print("name:",self.name)
# class Mark(Student):
#     def getmark(self):
#         self.mark=int(input("enter the mark out of 500:"))
#     def printmark(self):
#         print("Mark:",self.mark)
# class Grade(Mark):
#     def claculategrade(self):
#         p=self.mark/500*100
#         if p>=80:
#             print("A Grade")
#         elif p>=70:
#             print("B Grade")
#         elif p>=60:
#             print("C Grade")
#         else:
#             print("Failed")
# result=Grade()
# result.getdata()
# result.printdata()
# result.getmark()
# result.printmark()
# result.claculategrade()

#using init

# class Student:
#     def __init__(self):
#         self.roll=int(input("Enter the roll number"))
#         self.name=input("enter the name")
#     def printdata(self):
#         print("Rollno:",self.roll)
#         print("name:",self.name)
# class Mark(Student):
#     def __init__(self):
#         Student.__init__(self)
#         self.mark=int(input("enter the mark out of 500:"))
#     def printmark(self):
#         print("Mark:",self.mark)
# class Grade(Mark):
#     def __init__(self):
#         Mark.__init__(self)
#     def calculategrade(self):
#         p=self.mark/500*100
#         if p>=80:
#             print("A Grade")
#         elif p>=70:
#             print("B Grade")
#         elif p>=60:
#             print("C Grade")
#         else:
#             print("Failed")
# R1=Grade()
# R1.printdata()
# R1.printmark()
# R1.calculategrade()

#init with parameters

class Student:
    def __init__(self,r,n):
        self.roll=r
        self.name=n
    def printdata(self):
        print("Rollno:",self.roll)
        print("name:",self.name)
class Mark(Student):
    def __init__(self,r,n,m):
        Student.__init__(self,r,n)
        self.mark=m
    def printmark(self):
        print("Mark:",self.mark)
class Grade(Mark):
    def __init__(self,r,n,m):
        Mark.__init__(self,r,n,m)
    def calculategrade(self):
        p=self.mark/500*100
        if p>=80:
            print("A Grade")
        elif p>=70:
            print("B Grade")
        elif p>=60:
            print("C Grade")
        else:
            print("Failed")
R1=Grade(1,'anu',455)
R1.printdata()
R1.printmark()
