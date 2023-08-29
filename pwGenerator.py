import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def generate_password():
    password_length = int(input("How long would you like your password to be: "))
    random.shuffle(characters)
    password = []
    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    print('Password before join', password)
    password = "-".join(password)
    print(password)

option = input('Do u want to generate a password? (yes/no): ')
if option.lower() == 'yes':
    generate_password()
elif option.lower() == 'no':
    print('Program ended')
    quit()
else: 
    print('Invalid option, please try again')
    quit()