import sys

def small_parser(argv):
    if (len(argv) < 1):
        raise Exception("Error: Not enough arguments")
    for arg in argv:
        data = arg.split(":")
        if len(data) != 2:
            raise ValueError("Error: This is not a valid argument")
        try:
            int(data[1])
        except ValueError:
            raise ValueError("Error: This is not a valid argument")

def ft_inventory_system():
   
    argv = sys.argv[1:]
    argc = len(argv)

    small_parser(argv)
    inventory = {}
    i = 0
    for arg in argv:
        arg = arg.split(":")
        inventory.update({str(arg[0]): int(arg[1])})
    print("=== Inventory System Analysis ===") 
      
    total_values = 0 
    for items, values in inventory.items():
        total_values += values
    print(f"Total items: {total_values}")
    print(f"Unique item types: {argc}")

    print("=== Current Inventory ===")

    itens:list[tuple(str, int)] = list(inventory.items())
    
    i = 0
    while i < argc:
        j = 0
        while j < argc - i - 1:
            if itens[j][1] < itens[j + 1][1]:
                temp = itens[j]
                itens[j] = itens[j + 1]
                itens[j + 1] = temp
            j += 1
        i += 1

    i = 0
    while i < argc:
        name = itens[i][0]
        value = itens[i][1]
        porcentage = (value / total_values) * 100
        if value <= 1:
            print(f"{name}: {value} unit ({porcentage:.1f}%)")
        else:
            print(f"{name}: {value} units ({porcentage:.1f}%)")
        i += 1

    print("\n=== Inventory Statistics ===")
    least = itens[0]
    most = itens[0]
    for item in itens:
        if item[1] > most[1]:
            mais = item
        if item[1] < least[1]:
            least = item
    print(f"Most abundant: {most[0]} {most[1]} units")
    print(f"Least abundant: {least[0]} {least[1]} unit")
    
    print(f"=== Item Categories ===")
    categories = {"Moderate": {},
                  "Scarce": {},}
    restock_needed = []
    for items, values in inventory.items():
        if values >= 4:
            categories["Moderate"].update({items: values})
        else:
            categories["Scarce"].update({items: values})
        if values <= 1:
            restock_needed.append(items)
       
    moderate_items = categories["Moderate"]
    scarce_items = categories["Scarce"]
    print(f"Moderate: {moderate_items}")
    print(f"Scarce: {scarce_items}")
    
    print("\n=== Management Suggestions ===")
    
    print(f"Restock needed: {', '.join(restock_needed)}")
    
    print("\n=== Dictionary Properties Demo ===")
    keys_list = list(inventory.keys())
    print(f"Dictionary keys: {', '.join(keys_list)}")
    values_list = []
    for values in inventory.values():
        values_list.append(str(values))
    print(f"Dictionary values: {', '.join(values_list)}")
    print(f"Sample lookup - 'sword' in inventory: {inventory.get('sword') is not None}")

try:
    ft_inventory_system()
except (ValueError, Exception) as e:
    print(e)

