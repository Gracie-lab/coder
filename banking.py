import random   
import sys
    
    
credentials = open("Staff.txt", "r")

try:       
    action = int(input(''' For staff log in, press 1
    to logout, press 2: '''))
    c = open('staff.txt')
    txt = c.read()
    if action == 1:
        username = input("Please enter username: ")
        password = input("Enter password: ")
        user_session = open("user_session.txt", "w")
        if username and password in txt:
            login = True
        else:
            print("Incorrect username or password. Try again")
            username = input("Please enter username: ")
            password = input("Enter password: ")
    else:
        print("Thank you for banking with us")
        sys.exit()

    choice = int(input(''' To create new account, press 3
    To check account details, press 4
    To log out, press 5'''))
    
    if choice == 3:
        acc_name = input("Enter account name: ")
        opening_balance = input("Enter opening balance: ")
        acc_type = input("Enter account type: ")
        email = input("Enter account email: ")
        account_number = "%0.10d" % random.randint(0, 9999999999)
        file = open("customer.txt", "w")        
        file.write("Account Name: ")
        file.write(acc_name)
        file.write(" ")
        file.write("Opening Balance: ")
        file.write(opening_balance)
        file.write(" ")
        file.write("Account Type: ")
        file.write(acc_type)
        file.write(" ")
        file.write("email: ")
        file.write(email)
        file.write(" ")
        file.write("Account Number: ")
        file.write(" ")
        file.write(account_number)
        file.write("\n")
        file.close()
        

    print(f'''New account details:
    Account name: {acc_name}
    Balance: {opening_balance}
    Account type: {acc_type}
    Email: {email}
    Account Number: {account_number}''')

    choice = int(input(''' To create new account, press 3
    To check account details, press 4
    To log out, press 5'''))
    if choice == 4:
        acc_num = input("Enter account number: ")
        details = open("customer.txt", "r")
        customer = details.read()
        
        if acc_num in customer : 
            print(customer)
        else:
            print("Account number not registered")

    choice = int(input(''' To create new account, press 3
    To check account details, press 4
    To log out, press 5'''))
    if choice == 5:
        print("Thank you for banking with us")
        sys.exit()
            
except ValueError:
    print("Invalid input")
