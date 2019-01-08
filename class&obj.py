class student:
    def details(self,name,age):
        self.name=name
        self.age=age
        print('the name is {} age is {}'.format(name,age))
s=student()
name=input('Enter name ')
age=int(input('enter the age'))
s.details(name,age)