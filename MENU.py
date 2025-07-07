#Using functions to come up with simple  menu
def menu():
    print("1. Breakfast")
    print("2. Lunch")

def handle_selection(selected_value):
    if selected_value == 1:
        print("You have selected breakfast")
        print("________BREAKFAST MENU________")
        menu = {"Black_Tea":5.000, "Milk":10.000,"Hot_Choclate":7.000}
        #create a loop
        for items,Price in menu.items():
           print(f"{items:<15}shs{Price:>10.4f}")

    elif selected_value == 2:
        print("You have selected lunch")
        print("__________LUNCH_MENU___________")
        menu ={"Burger":12.000, "Fries":6.000,"Chicken":20.000}
        for items,Price in menu.items():
         print(f"{items:<15}shs{Price:>10.4f}")
menu()
choice = int(input("Enter your choice (1 or 2):"))
handle_selection(choice)

