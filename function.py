def add():
    n1=int(input('enter num'))
    n2=int(input('enter num'))
    print(n1+n2)
def sub():
    n1=int(input('enter num'))
    n2=int(input('enter num'))
    print(n1-n2)
a=int(input("Enter the otions \n 1.add \n2.sub\n"))
if (a==1):
    add()
elif (a==2):
    sub()
