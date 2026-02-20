def ft_count_harvest_helper(n: int) -> None:
    if n > 1:
        ft_count_harvest_helper(n - 1)
    print("Day", n)


def ft_count_harvest_recursive() -> None:
    n = int(input("Days until harvest: "))
    ft_count_harvest_helper(n)
    print("Harvest time!")
