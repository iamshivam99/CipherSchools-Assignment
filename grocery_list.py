#Here we're importing tabulate module for prettier representation of grocery list at the end...
#if you don't have tabulate installed in your system. Just run {pip install tabulate}...
from tabulate import tabulate

budget = int(input("Please Enter your budget: "))
budget_left = budget

item_names = []
item_quantity = []
item_price = []

index = -1

while True:
    if budget_left == 0:
        print('No items could be bought. Please Proceed to Transaction...\n')
        break
    print("\nPress (1) to add an item \n")
    print("Press (2) to Exit \n")
    status = input()

    if status == '2':
        print('Amount left is Rs',budget_left)
        print("\nThere's still some items left under your budget...")
        break
    elif status != '1':
        print('Invalid Input. Please try again...')
        continue
    else:

        curr_item_name = input('Enter product: ')
        curr_item_quantity = input('Enter quantity: ')
        curr_item_price = int(input('Enter Price: '))

        if curr_item_name in item_names:
                index = item_names.index(curr_item_name) 
                if curr_item_price > item_price[index]:
                    budget_left -= curr_item_price - item_price[index]
                    if budget_left < 0:
                        print("Can't make this change due to insufficient budget...")
                        print('\nAmount Left: ', budget_left)
                        continue
                elif curr_item_price < item_price[index]:
                    budget_left += item_price[index] - curr_item_price
                item_price[index] = curr_item_price
                item_quantity[index] = curr_item_quantity
                print('\nAmount Left: ', budget_left)
                continue
        
        if curr_item_price > budget_left:
            print("Can't Buy this product. Budget Left is Rs", budget_left)
            print('\nAmount Left: ', budget_left)
            continue

        elif curr_item_price <= budget_left:
            budget_left -= curr_item_price
            item_names.append(curr_item_name)
            item_price.append(curr_item_price)
            item_quantity.append(curr_item_quantity)

        print('\nAmount Left: ', budget_left)
                      
print("Here's Your Grocery List: \n")

grocery_list = [(item_names[i],item_quantity[i],item_price[i]) for i in range(len(item_names))]
print(tabulate(grocery_list, headers=["Product Name", "Quantity", "Price"]))