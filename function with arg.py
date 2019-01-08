def add(n1,n2):
  n3=n1+n2
  print("The value is ",n3)
def sub(n1,n2):
    n4=n1-n2
    print("the value is ",n4)
n1=int(input('enter num'))
n2=int(input('enter num'))
a=int(input("Enter the otions \n 1.add \n2.sub\n"))
if (a==1):
    add(n1,n2)
elif (a==2):
    sub(n1,n2)
