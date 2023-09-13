student = {
    "name" : "Timo",
    "age" : 20,
    "grade" : "A",
    "courses" : ["Math", "Physics", "Programming"]
}

# Accessing dictionary values:
print("Name: ", student["name"])
print("courses: ", student["courses"])

student["age"] = 25
student["courses"].append("language")
student["city"] = "Espoo"

# Iterating through the dictionary
for key, value in student.items():
    print(key + " :", value)

del student["grade"]
# checking if a key exists in the dictionary

if "age" in student:
    print("Age: ", student["age"])
else:
    print("Age not found in the dictionary")


shopping = {
    "milk" : 2,
    "rice" : 3,
    "oats" : 4,
}

def addshopping(item, quantity):
    shopping.append(item, quantity)

def removeshopping(item, quantity):
    shopping.remove(item, quantity)

def displayshopping():
    for item, quantity in shopping.items():
        print(item + ": " + quantity)

print("What would you like to do with your shopping list?")
print("1. Add an item")
print("2. Remove an item")
print("3. Display the shopping list")
print("4. Quit")
shoppinglist = input("Enter your choice 1/2/3/4 : ")

if shoppinglist == 1:
    addshopping(input("What would you like to add to your list?: "))
    print(f"You have added {addshopping} to your list")

