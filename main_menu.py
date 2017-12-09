from inventory import *
from ascii_art import ascii_art
import os

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
        print("============= Register Main Menu ===============  ")
        print("------------------------------------------------\n")
        print("Option 1: Instructions ")
        print("Option 2: Sales ")
        print("Option 3: Refunds ")
        print("Option 4: Reports ")
        print("Option 5: Inventory ")
        print("Option 6: Exit Program\n ")

        option = int(input("Please enter the corresponding option number: "))

        if option == 1:
            instructions()
        elif option == 2:
            sales()
        elif option == 3:
            refunds()
        elif option == 4:
            reports()
        elif option == 5:
            inventory()    
        elif option == 6:
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
    print("=========== Refund Processing Center ===========\n")
    print("------------------------------------------------\n")

    refund = int(input(" Refunds - Item Number: "))

    quantity = int(input("Enter item quantity to remove: "))
    try:
        
        (items[refund][3]) -= quantity 
        (items[refund][2]) += quantity
        print ("The newly updated record is: \n")
        print (items[refund])

        input("Press ENTER to Continue...")

    except KeyError:
        print ("\nInvalid item number, please re-enter 'refunds' module and try again\n")


def sales():
    
    print("--------------------------------------------")
    print("============= Checkout Screen ==============")
    print("--------------------------------------------")
    
    fp = open('receipt.txt', 'a')
    
    deleteContent(fp)

    fp.close()
    
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
            
            fp = open('receipt.txt', 'a')

            fp.write((str(items[item][0]))+ ", " +(str(items[item][1])) + ", " + str(quantity)+", "
                     + str((items[item][1])*(quantity)) +"\n")
            
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
    
def deleteContent(fp):
    fp.seek(0)
    fp.truncate()  

    
    
def inventory():
    
    print("------------------------------------------------")
    print("========= Display of current Inventory =========\n ")
    print("------------------------------------------------\n")
    print ("===== Items =====")
    print (" Item number - item - price - rem. stock ")

    for i in items:
        print ("\t", i, "   ", items[i][0],"   ", items[i][1], "    ", items[i][2] )

    input("Press ENTER to Continue...")



def reports():

    print("------------------------------------------------")
    print("================= Sales Report =================\n ")
    print("------------------------------------------------\n")

    print("Item Name        Sales ($)")
    grand_total = 0
    for i in items:

        tom = ((items[i][1])* (items[i][3]))
        grand_total = grand_total + tom 
        print ((items[i][0]), "            ", tom, "\n")


    print ("The Grand total of all Sales:",  grand_total)

    input("Press ENTER to Continue...")
        
          

def instructions():

    print("""
    Thank you for using the Grocery Shopping Calculator. To login, use one of
    the following username/password combinations.
    1. Username: nouman21 / Password: 4567
    2. Username: khawaja26 / Password: 1234
    
    The program allows users to operate a simulated Point of Sale (POS) system
    to conduct transactions. The options available in this application include:
    Sales, Refunds, Reports, Inventory, and the option to Exit the application.
    
    Sales: Input any item number between 0-34. User can enter the quantity of
    items being purchased. Continue entering items until you are done. Enter -1
    to finish and display a receipt.
    
    Refunds: Input the corresponding item number between 0-34 that you would
    like a refund for. Enter the quantity of items being returned.
    
    Reports: Input option 4 to use the reports function. Main purpose of
    this function is to display reports of the total sales figures.
    
    Inventory: Inputting option 5 displays the total inventory list and the
    corresponding item number, price, and quantity available.
    
    Exit: Input 6 on main menu screen to exit the application. 
    """
)


    



        
              


main()
            
