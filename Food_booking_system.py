Pasta = 7.50
burger = 9.50
soup = 6.00
drink = 4.50


def mainMenu():
    print("1.Food")
    print("2.Drinks")
    print("3.Exit")
    while True:
        try:
            selection=int(input("Enter choice 1 = Food, 2 = Drink, 3 = Exit"))
            if selection==1:
                food()
                break
            if selection==2:
                drinks()
                break
            elif selection==4:
                print("Thank you for using the food booking system")
                break
            else:
                print("Invalid choice, Enter 1-3")
                mainMenu()
        except ValueError:
                print("Please enter a choice between 1-3")

def food():
    foodselect=int(input("Enter choice 1 = Pasta, 2 = Burger, 3 = Soup"))
    if foodselect==1:
        print("You have selected Pasta")
        foodquantiy = int(input("Please quantity "))
        unit_price = str(Pasta * foodquantiy)
        print("Your total cost is £" + unit_price)
    elif foodselect==2:
        print("You have selected burger")
        foodquantiy = int(input("Please quantity "))
        unit_price = str(burger * foodquantiy)
        print("Your total cost is £" + unit_price)
    elif foodselect==3:
        print("You have selected Soup")
        foodquantiy = int(input("Please quantity "))
        unit_price = str(soup * foodquantiy)
        print("Your total cost is £" + unit_price)
    else:
        print("Invalid choice")
        drinkselect=int(input("Enter choice 1 = Coke, 2 = Fanta, 3 = Sprite"))
    if drinkselect==1:
        print("You have selected Coke")
        drinkquantiy = int(input("Please quantity "))
        drinkunit_price = str(drink + drinkquantiy)
        print("Your grand total is £" + drinkunit_price) 
        print(float(drinkunit_price))
    elif drinkselect==2:
        print("You have selected Fanta")
        drinkquantiy = int(input("Please quantity "))
        drinkunit_price = str(drink * drinkquantiy)
        total = str(unit_price * drinkunit_price)
        print("Your grand total is £" + drinkunit_price) 
        print("Your grand total is £" + float(unit_price)+float(drinkunit_price))
    elif drinkselect==3:
        print("You have selected Sprite")
        drinkquantiy = int(input("Please quantity "))
        drinkunit_price = str(drink * drinkquantiy)
        print("Your total cost is £" + drinkunit_price)
        print("Your grand total is £" + float(unit_price)+float(drinkunit_price))
    else:
        print("Invalid choice")
        
def drinks():
        drinkselect=int(input("Enter choice 1 = Coke, 2 = Fanta, 3 = Sprite"))
        if drinkselect==1:
            print("You have selected Coke")
            drinkquantiy = int(input("Please quantity "))
            drinkunit_price = str(drink + drinkquantiy)
            print("Your grand total is £" + drinkunit_price) 
            print(float(drinkunit_price))
        elif drinkselect==2:
            print("You have selected Fanta")
            drinkquantiy = int(input("Please quantity "))
            drinkunit_price = str(drink * drinkquantiy)
            total = str(drinkunit_price)
            print("Your grand total is £" + drinkunit_price) 
        elif drinkselect==3:
            print("You have selected Sprite")
            drinkquantiy = int(input("Please quantity "))
            drinkunit_price = str(drink * drinkquantiy)
            print("Your total cost is £" + drinkunit_price)
        else:
            print("Invalid choice")
mainMenu()