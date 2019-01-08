password = input('Enter new password')
for i in range(3):
    pw = input("Enter passwor to login")
    j=3
    if(pw == password):
        print("welcome")
        break
    else:
        print("wrong passwor, Attempt left",j-i)
        continue
print("Try again later")