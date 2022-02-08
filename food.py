food_stock = {1: ["Tandoori Chicken", 16, 240], 2: ["Vegan Burger", 10, 320], 3: ["Truffle Cake", 2000, 900]}
order_history = {}


def add_food(food_id):
    name = input("Enter food name: ")
    quantity = int(input('Enter quantity: '))
    price = int(input('Enter price: '))
    food_stock.update({food_id: [name, quantity, price]})


def display():
    for k, v in food_stock.items():
        print(f"FOOD_ID:{k}.{v[0]} Available:{v[1]} For Price {v[2]} per Pieces")


def remove_food(food_id):
    flag = False
    if bool(food_stock):
        for i in food_stock.keys():
            if i == food_id:
                flag = True
        if flag:
            print("ITEM DELETED SUCCESSFULLY")
            del food_stock[food_id]
    else:
        print(f"FOOD ITEM WITH ID:{food_id} IS NOT AVAILABLE")


def edit_food(food_id):
    flag = False
    sh = ''
    while sh != 4:
        print("\tFOOD EDIT MENU")
        print("\t1. CHANGE NAME")
        print("\t2. RESTOCK")
        print("\t3. CHANGE PRICE")
        print("\t4. EXIT")
        print("\tSelect Your Option (1-4)\n=> ")
        sh = input()

        if sh == '1':
            name = input("GIVE NEW NAME : ")
            for k in food_stock.keys():
                if k == food_id:
                    flag = True
            if flag:
                food_stock[food_id][0] = name
        elif sh == '2':
            stock = int(input("\tQUANTITY : "))
            for k in food_stock.keys():
                if k == food_id:
                    flag = True
            if flag:
                food_stock[food_id][1] = stock
        elif sh == '3':
            price = int(input("\tGIVE NEW PRICE : "))
            for k in food_stock.keys():
                if k == food_id:
                    flag = True
            if flag:
                food_stock[food_id][2] = price
        else:
            print("INVALID ID")
            break


def order(userid):
    emp_lst = []
    food_id_list = []
    count = 0
    total = 0
    food_id = input("ENTER FOOD ID [ Please Give Space After Every Food ID]: ")
    new_lst = list(food_id.replace(' ', ''))
    for i in new_lst:
        food_id_list.append(int(i))
    for i in food_id_list:
        if i in food_stock and food_stock[i][1] != 0:
            food_stock[i][1] -= 1
            emp_lst.append(food_stock[i][0])
            print(f"YOUR ORDER FOR {food_stock[i][0]} IS SUCCESSFULL")
            total = total + food_stock[i][2]
        else:
            print(f"{food_stock[i][0]} IS OUT-OF-STOCK ")
    print(f" YOUR GRAND TOTAL IS : {total} \n ITEMS\n")
    for i in emp_lst:
        count += 1
        print(f"{count}.{i} ORDERED")
    order__history(userid, emp_lst)


def order__history(userid, food_lst):
    if userid in order_history:
        order_history[userid] = order_history[userid] + food_lst
    else:
        order_history.update({userid: [food_lst]})


def display_order_history(user_id):
    if user_id in order_history:
        print(f" All ORDERS FOR USER_ID : {user_id} \n ")
        for i in order_history[user_id]:
            print(i, '\n')
    else:
        print("INVALID USER_ID")
