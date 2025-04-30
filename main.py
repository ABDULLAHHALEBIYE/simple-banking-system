users = {"abdullah":500,
         "ali":600,
         "saad":300,
         "omer":100}
is_running = True

while is_running:
    print(f"{'Menu':^25}")
    print("*************************")
    print("1. Display all Users")
    print("2. Add new User")
    print("3. Delete User")
    print("4. Withdraw Money")
    print("5. Exit")
    print("*************************")
    selection = input("Select What Do you want to do: ")
    match selection:
        case "1":
            print("*************************")
            for key, value in users.items():
                print(f"{key:15} -> {value}")
        case "2":
            a_user = input("Enter the user you want to add: ")
            if a_user in users.keys():
                print("the user is already in the table.")
                continue
            a_money = input("Enter the balance of the user: ")
            if a_money.isdigit() == False:
                print("please enter a number.")
                continue
            if a_user not in users.keys():
                users[a_user] = int(a_money)
                print(f"{a_user} was added successfully.")            
        case "3":
            d_user = input("Enter which user you want to delete: ")
            if d_user in users.keys():
                users.pop(d_user)
            else:
                print(f"there is no {d_user} in users table.")
        case "4":
            from_user = input("from: ")
            if from_user not in users.keys():
                print(f"{from_user} is not found.")
                continue
            to_user = input("to: ")
            if to_user not in users.keys():
                print(f"{to_user} is not found.")
                continue
            else:
                how_much = int(input("how much do you want to withdraw: "))
                if how_much <= 0:
                    print("the number must be greater than 0")
                    continue
                if how_much > users[from_user]:
                    print("you dont have enough money to withdraw")
                else:
                    users[from_user] -= how_much
                    users[to_user] += how_much
                    print("the withdraw completed successfully")
        case "5":
            is_running = False
        case _:
            print("invalid value.")
    print("*************************")
