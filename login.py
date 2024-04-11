import getpass
#_FUNCTION FOR LOGIN_
def login():
    print("                        LOGIN")
    user =input("Username: ")
    while True:
        try:
            passw=getpass.getpass("User Id::6 LETTERS")
        except:
            pass
        if len(passw)==6:
            break
        else:
            print("ENTER 6 LETTER USER ID:-)")
            pass
    f = open("user.txt", "r")
    for line in f.readlines():
        try:
            us, pw = line.strip().split(",")
        except:
            print("USER NAME OR USER ID DOES NOT EXIST!!")
        if (user in us) and (passw in pw):
            return 1
    print("Wrong username/password")
    return 2
    f.close()
#_FUNCTION FOR SIGNUP_
def pas():
    print("                        SIGN UP")
    user =input("Username: ")
    while True:
        passw=getpass.getpass("User Id::6 LETTERS!!")
        if len(passw)==6:
            break
        else:
            print("ENTER 6 LETTER USER ID:-)")
            pass
    f = open("user.txt", "r")
    for line in f.readlines():
        pw = line.strip().split(",")
        if (passw in pw):
            print("USER ID EXISTS::TRY A DIFFERENT ONE:-)")
            return pas()
        else:
            pass
    else:
        pass
    print("Done!")
    return user,passw
