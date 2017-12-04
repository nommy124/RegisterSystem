from inventory import *


def main():

    apple = login()

    exit_code = False

    while exit_code == False:   

        if apple == True:

            main_menu()
            break

        else:

            print(" The password provided was incorrect, please try again. ")

def main_menu():


    exit_code = True

    while exit_code == True:

        print (items[1][0])  # TESTING IF ITEM IMPORTS CORRECTLY. IT DOES :)      
        print("=== Register Main Menu === \n ")
        print("Option 1: Sales ")
        print("Option 2: Refunds ")
        print("Option 3: Reports ")
        print("Option 4: Inventory ")
        print("Option 5: Exit Program\n ")

        option = int(input("Please enter the corresponding option number: "))

        if option == 1:
            sales()
        elif option == 2:
            refunds()
        elif option == 3:
            reports()
        elif option == 4:
            inventory()
        elif option == 5:
            print("The Program will now exit.... Goodbye!")
            exit_code = False
            break
        else:
            print ("error, none of the inputs entered were valid. Please try again")
            

# login function - final project 



def login():

    exit_code = False
    while exit_code == False:

        print("------------------------------------------------")
        print("Hello, Please enter your login credentials below")
        print("------------------------------------------------\n")
        
        user = input("Username: ")

        password = input("Password: ")

        file = open("login_info.txt", "r")

        for line in file.readlines():

            us, pw = line.strip().split("|", 1)

            if (user in us) and (password in pw):

                print("Login correct\n")
                exit_code = True
                return True
              

        print("Login incorrect\n")


        file.close()


main()
            
