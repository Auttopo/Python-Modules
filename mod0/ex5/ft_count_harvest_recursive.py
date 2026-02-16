
def ft_count_harvest_recursive(days=int(input("Days until harvest: "))):

    test = 0
    if days >= 0:
        test = 1
        days = days * -1
    if days < 0:
        if days + 1 != 0:
            ft_count_harvest_recursive(days + 1)
        print("Day", days * -1)
    if test == 1 or (test == 1 and days == 0):
        print("Harvest time!")

# ft_count_harvest_recursive()
