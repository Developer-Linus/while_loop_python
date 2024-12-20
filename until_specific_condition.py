shopping_items = ['apples', 'bread', 'milk', 'cheese']
item_found = False

while not item_found:
    item = input("Search for item in the shopping list or enter 'q' to quit")
    if item.lower() == 'q':
        break
    if item in shopping_items:
        item_found = True
        print(f"{item} is in your shopping list.")
    else:
        print(f"{item} is not in your shopping list")