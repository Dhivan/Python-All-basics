import time
a=int(input('enter value :'))
for i in range(1,(a+1)):
    print("\n")
    time.sleep(3)
    for j in range(1,11):
        print(i,'x',j,'=',i*j)