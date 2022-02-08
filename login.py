import random

user_list = {}


def update(user_id):
    name = input("Enter Your Full Name =>")
    phone = input("Enter Your Phone Number =>")
    address = input("Enter Your Address =>")
    passwd = input("Enter Your Password =>")
    user_list.update({user_id: {'name': name, 'phone': phone, 'address': address, 'passwd': passwd}})


def admin():
    print('Welcome Administrator Please Enter Credential')
    count = 0
    # user_id
    while count < 3:
        username = input('Enter username: ')
        password = input('Enter password: ')
        if password == '123' and username == 'kunal':
            print('Access granted')
            return True
        else:
            print('Access denied. Try again.')
            count += 1


def add_user():
    user_id = random.randint(1, 100)
    update(user_id)
    print("You have successfully created an account with id:", user_id, "and password:", user_list[user_id]['passwd'])


def user_login():
    user_id = input('Enter user_id: ')
    password = input('Enter password: ')
    for k, v in user_list.items():
        if int(user_id) == k and v['passwd'] == password:
            print("successfully login")
            return user_id
        else:
            return False
