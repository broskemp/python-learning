
shopping = {
    "MILK": 2,
    "RICE": 3,
    "OATS": 4,
}


def addshopping(item, quantity):
    shopping[item] = quantity


def removeshopping(item):
    del shopping[item]


def displayshopping():
    for item, quantity in shopping.items():
        print(item, ": ", quantity)


while True:
    print("What would you like to do with your shopping list?")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Display the shopping list")
    print("4. Quit")
    shoppinglist = int(input("Enter your choice 1/2/3/4 : "))
    if shoppinglist == 1:
        addshopitem = input("What would you like to add to your list?: ").upper()
        addshopquantity = int(input("How much of this item would you like to add? : "))
        print(f"You have added {addshopitem} (amount = {addshopquantity}) to your list")
        addshopping(addshopitem, addshopquantity)
        if addshopitem == "":
            break
    elif shoppinglist == 2:
        removeshopitem = input("What would you like to remove from your list? : ").upper()
        if removeshopitem in shopping:
            print(f"You have removed {removeshopitem} from your list.")
            removeshopping(removeshopitem)
        else:
            print("This item is not in the shopping list.")
    elif shoppinglist == 3:
        displayshopping()
    elif shoppinglist == 4:
        break
    else:
        print("Please enter 1, 2, 3 or 4.")
print("Enjoy shopping! Ending sequence.")