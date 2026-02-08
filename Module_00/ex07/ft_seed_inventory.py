def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit != "packets" and unit != "grams" and unit != "area":
        print("Unknow unit type")
    else:
        if unit == "packets":
            res = "packets availabe"
        elif unit == "grams":
            res = "grams total"
        else:
            res = "square meters"
        print(seed_type.capitalize() + " seeds: ", quantity, " " + res)
