def ft_count_harvest_helper(n):
    if n > 1:
        ft_count_harvest_helper(n - 1)
    print("Day", n)


def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))
    ft_count_harvest_helper(n)
    print("Harvest time!")
