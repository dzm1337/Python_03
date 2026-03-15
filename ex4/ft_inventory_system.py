import sys

def ft_inventory_system() -> None:
   
    argv = sys.argv[1:]
    argc: int = len(argv)

    inventory = {}
    i = 0

    if argc < 1:
        raise Exception(f"Error: Not enough arguments!")

    for arg in argv:
        if not ":" in arg:
            raise Exception(f"Error: no ':' in argument")
    try:
        for arg in argv:
            data = arg.split(":")
            inventory.update({str(data[0]): int(data[1])})
    except ValueError:
        print(f"Error: either ({data[0]}) or ({data[1]}) is not a valid argument")
        return

    print("=== Inventory System Analysis ===") 
      
    total_values: int = 0 
    for items, values in inventory.items():
        total_values += values
    print(f"Total items: {total_values}")
    print(f"Unique item types: {argc}")

    print("\n=== Current Inventory ===")

    itens:list[tuple(str, int)] = list(inventory.items())
    
    i: int = 0
    while i < argc:
        j = 0
        while j < argc - i - 1:
            if itens[j][1] < itens[j + 1][1]:
                temp = itens[j]
                itens[j] = itens[j + 1]
                itens[j + 1] = temp
            j += 1
        i += 1

    i: int = 0
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
    least:tuple(str, int) = itens[0]
    most:tuple(str, int) = itens[0]
    for item in itens:
        if item[1] > most[1]:
            most = item
        if item[1] < least[1]:
            least = item
    if most[1] > 1:
        print(f"Most abundant: {most[0]} ({most[1]} units)")
    else:
        print(f"Most abundant: {most[0]} ({most[1]} unit)")
    if least[1] > 1:
        print(f"Least abundant: {least[0]} ({least[1]} units)")
    else:
        print(f"Least abundant: {least[0]} ({least[1]} unit)")

    print(f"=== Item Categories ===")
    categories:dict[dict[str, int]] = {"Moderate": {},
                                        "Scarce": {},}
    restock_needed:list[str] = []
    for items, values in inventory.items():
        if values >= 4:
            categories["Moderate"].update({items: values})
        else:
            categories["Scarce"].update({items: values})
        if values <= 1:
            restock_needed.append(items)
       
    moderate_items:dict[str, int] = categories["Moderate"]
    scarce_items:dict[str, int] = categories["Scarce"]
    print(f"Moderate: {moderate_items}")
    print(f"Scarce: {scarce_items}")
    
    print("\n=== Management Suggestions ===")
    
    print(f"Restock needed: {', '.join(restock_needed)}")
    
    print("\n=== Dictionary Properties Demo ===")

    keys_list:list[str] = list(inventory.keys())

    print(f"Dictionary keys: {', '.join(keys_list)}")

    values_list:list[str] = []
    for values in inventory.values():
        values_list.append(str(values))

    print(f"Dictionary values: {', '.join(values_list)}")
    print(f"Sample lookup - 'sword' in inventory: {inventory.get('sword') is not None}")

if __name__ == "__main__":
    try:
        ft_inventory_system()
    except (Exception, ValueError) as e:
        print(e)
