from inventory import *
from ascii_art import ascii_art


def main():

    print("********Welcome to the Grocery Shopping Calculator********")

    ascii_art()

    apple = login()

    exit_code = False

    while exit_code == False:   

        if apple == True:

            menu()
            break

        else:

            print(" The password provided was incorrect, please try again. ")

def menu():


    exit_code = True

    while exit_code == True:

        print("------------------------------------------------")    
        print("=== Register Main Menu ===  ")
        print("------------------------------------------------\n")
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


def refunds():

    print("------------------------------------------------")
    print ("===== Refund Processing Center =====\n")
    print("------------------------------------------------\n")

    refund = int(input(" Refunds - Item Number: "))

    quantity = int(input("Enter item quantity to remove: "))
    try:
        
        (items[refund][3]) -= quantity 
        (items[refund][2]) += quantity
        print ("The newly updated record is: \n")
        print (items[refund])

    except KeyError:
        print ("\nInvalid item number, please re-enter 'refunds' module and try again\n")


def sales():
    
    print("------------------------------------------------")
    print ("===== Sales Center =====")
    print("------------------------------------------------")
    
    while True:

        print("(Enter -1 to complete check out process)")
        
        item = int(input("Employee, Enter item number: "))

        if item == -1:
            break
            
        quantity = int(input("Item Quantity: "))
        try:
            
            (items[item][3]) += quantity 
            (items[item][2]) -= quantity
            print (items[item])
            
            fp = open('receipt.txt', 'w+')


            fp.write((str(items[item][0]))+ ", " +(str(items[item][1])) + ", " + str(quantity)+", " + str((items[item][1])*(quantity)) +"\n")
            
            fp.close()
      

        except KeyError:
            print ("\nInvalid item number, please re-enter 'refunds' module and try again\n")

    print("---------------------")
    print("Here is your Receipt:")
    print("---------------------")
    f = open('receipt.txt', 'r')

    message = f.read()

    print(message)

    f.close()
    

    
def inventory():
    
    print("------------------------------------------------")
    print (" ===== Display of current Inventory =====\n ")
    print("------------------------------------------------\n")
    print ("===== Items =====")
    print (" Item number - item - price - rem. stock ")

    for i in items:
        print ("\t", i, "   ", items[i][0],"   ", items[i][1], "    ", items[i][2] )

    input("Press ENTER to Continue...")

#def payment():


#def report():

    



        
              


main()
            
