import sys


def split_arg(arg: str) -> tuple[str, int]:
    valid = False
    i = 0
    for c in arg:
        if c == ':':
            valid = True
            break
        i += 1
    item = arg[:i]
    quantity = arg[i + 1:]
    if not valid or len(item) == 0 or len(quantity) == 0:
        raise ValueError(f"Invalid format: '{arg}'")
    for c in quantity:
        if c == ':':
            raise ValueError(f"Invalid format: '{arg}'")

    try:
        quantity = int(quantity)
    except ValueError:
        raise ValueError(f"Invalid quantity: '{arg}'")
    if quantity < 0:
        raise ValueError(f"Invalid quantity: '{arg}'")
    return (item, quantity)


def process_inventory(args: list[str]) -> list[dict]:
    if len(args) == 0:
        raise ValueError(
            'No items provided. Usage: python3 '
            'ft_inventory_system.py <item:quantity> <item:quantity> ...')
    inventory = {}
    for arg in args:
        try:
            item, quantity = split_arg(arg)
            inventory.update({item: quantity})
        except ValueError as e:
            print(e)
    return inventory


def get_total_items(inventory: dict) -> int:
    total_items = 0
    for item in inventory.values():
        total_items += item
    return total_items


def inventory_items(inventory: dict):
    total_items = get_total_items(inventory)
    if total_items == 0:
        raise ValueError('No valid inventory items.')

    print(f'Total items in inventory: {total_items}')
    print(f'Unique item types: {len(inventory.keys())}')


def display_inventory_items(inventory: dict) -> None:
    total_items = get_total_items(inventory)
    for key, value in inventory.items():
        print(
            f'{key}: {value} units ({value / total_items * 100:.1f}%)')


def inventory_stats(inventory: dict) -> None:
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


def item_categories(inventory: dict) -> None:
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


def suggestions_management(inventory: dict) -> None:
    restock = []
    for item, value in inventory.items():
        if value < 2:
            restock += [item]
    print('Restock needed: ', end='')
    print(*restock, sep=', ')


def dictionary_demo(inventory: dict) -> None:
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


if __name__ == "__main__":
    print('=== Inventory System Analysis ===')
    try:
        inventory = process_inventory(sys.argv[1:])

        inventory_items(inventory)

        print('\n=== Current Inventory ===')
        display_inventory_items(inventory)

        print('\n=== Inventory Statistics ===')
        inventory_stats(inventory)

        print('\n=== Item Categories ===')
        item_categories(inventory)

        print('\n=== Management Suggestions ===')
        suggestions_management(inventory)

        print('\n=== Dictionary Properties Demo ===')
        dictionary_demo(inventory)
    except Exception as e:
        print(e)
