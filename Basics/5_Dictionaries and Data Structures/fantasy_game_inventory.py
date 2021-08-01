'''Function that can take a library representing the inventory and print it'''

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

'''Function that can add a list of loot to an existing inventory'''

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'rope']

def add_to_inventory(inventory, loot):
    for item in loot:
        item_count = loot.count(item)
        if item in inventory.keys():
            inventory[item] += item_count
        else:
            inventory.setdefault(item, item_count)
        loot = [value for value in loot if value != item]

add_to_inventory(inv, dragonLoot)
display_inventory(inv)

