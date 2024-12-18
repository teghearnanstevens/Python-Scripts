items = int(input("Number of Manufactored items: "))
items_in_box = int(input("Number of items to pack per box: "))

boxes_required = (items + items_in_box - 1) // items_in_box

print(f"You will need {boxes_required} boxes.")

