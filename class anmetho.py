  class student:
    def __init__(self,name):
        self.name = name
        self.attend=0
        self.marks=[]
        print('Welcom to school {}'.format(name))
    def addmark(self,ma):
        self.marks.append(ma)
    def attenddays(self):
        self.attend +=1
    def getavg(self):
        return sum(self.marks)/len(self.marks)
name = input('enter the name')
s1 = student(name)
c = int(input('enter the action to perform\n 1; add mark\n 2; add attenance\n 3; Find Avg\n'))
if (c==1):
    ma=int(input('Maths = '))
    s1.addmark(ma)
    ma = int(input('science = '))
    s1.addmark(ma)
    ma = int(input('bio = '))
    s1.addmark(ma)
    print('mark added {}'.format(ma))
elif (c==2):
    print('press enter to give attnd')
    s1.attenddays()
elif(c==3):
    print("avg {}".format(s1.getavg()))