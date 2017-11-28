# login function - final project 



def login():

    exit_code = False
    while exit_code == False:
        

        user = input("Username: ")

        password = input("Password: ")

        file = open("login_info.txt", "r")

        for line in file.readlines():

            us, pw = line.strip().split("|", 1)

            if (user in us) and (password in pw):

                print("Login correct")
                
                return True
                exit_code = True

        print("Login incorrect\n")

        #return False

        file.close()
