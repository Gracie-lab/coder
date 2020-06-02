import string
import random
firstName = input('Enter first name: ')
lastName = input('Enter last name: ')
email = input('Enter email address: ')

password = firstName[:2] + lastName[:2] + ''.join(random.choice(string.ascii_letters) for i in range(5))
print (password)

changePassword = input('If you would like to change your password, type yes: ')

while changePassword == 'yes':
    print('password must not be less than 7 characters')
    password = str(input('Enter new password: '))
    if len(password) < 7:
        print('Password should have at least 7 characters')
    else:
        break
    
container = [firstName, lastName, email, password]
print(container)
