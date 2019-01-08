password = input('Enter new password')
for i in range(3):
    pw = input("Enter passwor to login")
    if(pw == password):
        print("welcome")
    else:
        print("wrong passwor, Attempt left",j-i)
        continue
print("Try again later")