#friends= []
#name = None

#while name != "end":
    #name = input("Type the name of a friend: ")
    #if name!= "end":
        #friends.append(name)
#print()
#print("Your friends are:")

#for friend in friends: 
    #print(friend)

shopping_list = []
item = None

while item != "quit":
    item = input("Item: ")

    if item != "quit":
        shopping_list.append(item)

print("\nThe shopping list is:")
for item in shopping_list:
    print(item)

print("\nThe shoppping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

shopping_list[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")
