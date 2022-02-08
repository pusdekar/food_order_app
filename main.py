import login
import food


def call_admin():
    sh = ''
    while sh != 5:
        print("\tADMIN MENU")
        print("\t1. VIEW FOOD LIST")
        print("\t2. ADD FOOD ITEM'S")
        print("\t3. REMOVE FOOD ITEM'S")
        print("\t4. EDIT FOOD ITEM")
        print("\t5. EXIT")
        print("\tSelect Your Option (1-5)\n=> ")
        sh = input()

        if sh == '1':
            food.display()
        elif sh == '2':
            food_id = int(input('ENTER FOOD ID: '))
            food.add_food(food_id)
        elif sh == '3':
            food_id = int(input('ENTER FOOD ID: '))
            food.remove_food(food_id)
        elif sh == '4':
            food_id = str(input('ENTER FOOD ID: '))
            food.edit_food(food_id)
        elif sh == '5':
            print("\tBACK TO PREVIOUS MENU")
            break
        else:
            print("INVALID OPTION")


def call_user(userid):
    print("AVAILABLE FOOD : ")
    food.display()
    sh = ''
    while sh != 4:
        print("\tMENU")
        print("\t1. Place New Order")
        print("\t2. Order History")
        print("\t3. Update Profile")
        print("\t4. EXIT")
        print("\tSelect Your Option (1-4)\n=> ")
        sh = input()

        if sh == '1':
            food.order(userid)
        elif sh == '2':
            food.display_order_history(userid)
        elif sh == '3':
            login.update(userid)
        elif sh == '4':
            print("\tBACK TO PREVIOUS MENU")
            break
        else:
            print("INVALID OPTION")


ch = ''
while ch != 5:
    print("\tUSER MENU")
    print("\t1. NEW USER")
    print("\t2. Admin Login")
    print("\t3. USER LOGIN")
    print("\t4. EXIT")
    print("\tSelect Your Option (1-2)\n=> ")
    ch = input()
    if ch == '1':
        login.add_user()
    elif ch == '2':
        if login.admin():
            call_admin()
        else:
            print("PLEASE TRY AGAIN :-( !!")
    elif ch == '3':
        user_id = login.user_login()
        if bool(user_id):
            call_user(user_id)
        else:
            print("ID NOT FOUND!!")
    elif ch == '4':
        print("\tThank-You FOR USING FOOD ORDERING APPLICATION")
        exit(0)
    else:
        print("INVALID OPTION")
