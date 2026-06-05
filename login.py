username = "cyrus"
password = 12345
count = 3


while count > 0:
    userName = input("Enter Username :")
    userPass = int(input("Enter Password :"))

    if username  == userName and password == userPass:
     print("Login Successful")
     break
    else:
        count -= 1
        print("Invalid Credentials")
        print("Remaining Attempts:", count)
    
    if count == 0:
        print("Account locked") 