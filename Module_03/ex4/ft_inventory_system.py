import sys


def my_split(name: str) -> list[str]:
    valid = False
    i = 0
    for c in name:
        if c == ':':
            valid = True
            break
        i += 1
    key = name[:i]
    value = name[i + 1:]
    if len(key) == 0 or len(value) == 0:
        raise ValueError(f"Ivalid format: '{name}'")
    for c in value:
        if c == ':':
            raise ValueError(f"Ivalid format: '{name}'")
    if not valid:
        raise ValueError(f"Ivalid format: '{name}'")
    try:
        value = int(value)
    except ValueError:
        raise ValueError(f"Invalid quantity: '{name}'")
    if value < 0:
        raise ValueError(f"Invalid quantity: '{name}'")
    return [key, value]


if __name__ == "__main__":
    print('=== Inventory System Analysis ===')
    if len(sys.argv) == 1:
        print('No data provided')
    else:
        inventory = {}
        args = sys.argv[1:]
        for arg in args:
            try:
                lst = my_split(arg)
                if len(lst) == 2:
                    inventory.update({lst[0]: lst[1]})
            except ValueError as e:
                print(e)
        total_items = 0
        for item in inventory.values():
            total_items += item
        if total_items != 0:
            print(f'Total items in inventory: {total_items}')
            print(f'Unique item types: {len(inventory.keys())}')

            print('\n=== Current Inventory ===')
            for key, value in inventory.items():
                print(
                    f'{key}: {value} units ({value * 100 / total_items:.1f}%)')

            print('\n=== Inventory Statistics ===')
            first_item = True
            for key, value in inventory.items():
                if first_item:
                    most_key = key
                    most_value = value
                    least_key = key
                    least_value = value
                    first_item = False
                else:
                    if value > most_value:
                        most_key = key
                        most_value = value
                    if value < least_value:
                        least_key = key
                        least_value = value
            print(f'Most abundant: {most_key} ({most_value} units)')
            print(f'Least abundant: {least_key} ({least_value} units)')

            print('\n=== Item Categories ===')
            categories = {
                "abundant": {},
                "moderate": {},
                "scarce": {}
                }
            names = {
                'abundant': 'Abundant',
                'moderate': 'Moderate',
                'scarce': 'Scarce'
                }
            for key, value in inventory.items():
                if value >= 10:
                    categories['abundant'].update({key: value})
                elif value >= 5:
                    categories['moderate'].update({key: value})
                else:
                    categories['scarce'].update({key: value})
            for category, items in categories.items():
                if len(items) == 0:
                    continue
                print(f"{names[category]}: {categories[category]}")

            print('\n=== Management Suggestions ===')
            restock = []
            for item, value in inventory.items():
                if value < 2:
                    restock.append(item)
            print('Restock needed: ', end='')
            print(*restock, sep=', ')

            print('\n=== Dictionary Properties Demo ===')
            print('Dictionary keys: ', end='')
            print(*inventory.keys(), sep=', ')
            print('Dictionary values: ', end='')
            print(*(inventory.values()), sep=', ')
            lookup = 'sword'
            print(f"Sample lookup - '{lookup}' in inventory: ", end='')
            if inventory.get(lookup) is None:
                print('False')
            else:
                print('True')
        else:
            print("No valid inventory data.")
