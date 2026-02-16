
import sys


def parser(stri: str) -> dict[str, int]:
    """ parse input in a discionary """

    if stri is None:
        return
    name = ""
    i = 0
    while i < len(stri) and stri[i] != ':':
        name += stri[i]
        i += 1
    if name is None or name == "":
        print("invalid name")
        return {}
    try:
        try:
            num = int(stri[i + 1:])
        except Exception:
            raise ValueError("invalid number")
        if num < 0:
            raise ValueError("value can´t be negative")
        if num == 0:
            print(f"\"{name}\" count: {num} -not created-")
            return {}
        print(f"\"{name}\" count: {num} -created-")
    except Exception as e:
        print(name, f": {e}")
        return {}
    return dict([(name, num)])


def see(inv: dict) -> None:
    """ show the inventory in lines """

    print("\nINVENTORY:")
    for item in inv.items():
        print(item)


def stats(inv: dict) -> None:
    """ see stats of the inventory """

    print("\nSTATS:")
    (big_name, big), *oth = inv.items()
    (less_name, less), *oth = inv.items()
    total = 0
    for item, value in inv.items():
        if value > big:
            big = value
            big_name = item
        if value < less:
            less = value
            less_name = item
        total += value

    print("Inventory repartition:")
    for item, value in inv.items():
        print(f"{item} {value}, ({value / total * 100} %)")
    print("\ntotal items:", total, end=", ")
    print("composed by:", inv.values())
    print("most possess item : ", big_name, ". count: ", big, sep="")
    print("least possess item : ", less_name, ". count: ", less, sep="")
    print("item collection:", inv.keys())


def nester_stats(inv: dict) -> dict[str, dict[str, int]]:
    """ create a nested dictionary and display stats infos """

    nested_inv = {"abundant": {}, "moderate": {}, "scarce": {}}
    for item in inv.items():
        name, value = item
        if value < 5:
            nested_inv.get("scarce").update({item})
        elif value < 10:
            nested_inv.get("moderate").update({item})
        else:
            nested_inv.get("abundant").update({item})

    print("\nNESTED STATS:")
    print("Rares items:", nested_inv.get("scarce"))
    print("Uncommon items:", nested_inv.get("moderate"))
    print("Common items:", nested_inv.get("abundant"))

    print("\nSUGGESTION:")
    gold = nested_inv.get("abundant").get("gold")
    if len(nested_inv.get("scarce")) < 3:
        print("get more \"Rares\" items")
    elif gold and gold < 1000:
        print("get more \"Golds\"")
    else:
        print("you are fine to go in dungeons")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")
    inventory = dict()
    for elem in sys.argv[1:]:
        inventory.update(parser(elem))
    if len(inventory) < 1:
        print("no inventory created")
        sys.exit()
    see(inventory)
    stats(inventory)
    nested_inv = nester_stats(inventory)
