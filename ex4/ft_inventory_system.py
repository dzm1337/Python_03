def ft_inventory_system():

    print("=== Inventory System Analysis ===")
    inventory = {
    "potion": 5,
    "armor": 3,
    "shield": 2,
    "sword": 1,
    "helmet": 1
    }
    total_value = 0
    len_inventory = (len(inventory))
    for value in inventory.values():
        total_value += value
    print(f"Total items in inventory: {total_value}")
    print(f"Unique items types: {len_inventory}")
    
    print("\n=== Current Inventory ===")
    for names, values in inventory.items():
        porcentage = (values / total_value) * 100
        if (values == 1):
            print(f"{names}: {values} unit ({porcentage:.1f})")
        else:
            print(f"{names}: {values} units ({porcentage:.1f})")
    
ft_inventory_system()
