from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda arti: arti["power"])


def power_filter(
        mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    return [
        elem for elem in filter(
            lambda pow: pow["power"] >= min_power, mages
        )
    ]


def spell_transformer(spells: list[str]) -> list[str]:
    return [elem for elem in map(lambda elem: '*' + elem + '*', spells)]


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "max_power": max(mages, key=lambda datas: datas["power"]),
        "min_power": min(mages, key=lambda datas: datas["power"]),
        "avg_power": (
            sum((lambda arg: [elem['power']
                for elem in arg])(mages)) / len(mages) * 100 + 0.5
        ).__int__() / 100
    }


if __name__ == "__main__":
    obj_list = [
        {"name": "stick", "power": 1, "type": "wood"},
        {"name": "cursed bow", "power": -10, "type": "wood"},
        {"name": "mega legendary AK47",
            "power": 999, "type": "automatic rifle"},
        {"name": "bow", "power": 16, "type": "wood"},
        {"name": "wooden sword", "power": 6, "type": "wood"},
        {"name": "thorny stick", "power": -1, "type": "wood"},
        {"name": "sword", "power": 26, "type": "steel"},
        {"name": "steel stick", "power": 4, "type": "steel"}
    ]

    sorted_obj_list = artifact_sorter(obj_list)
    print("SORTED OBJ LIST :")
    for item in sorted_obj_list:
        print(item)
    print("")

    mage_list = [
        {"name": "stick", "power": 1, "element": "wood"},
        {"name": "cursed bow", "power": -10, "element": "wood"},
        {"name": "mega legendary AK47",
            "power": 999, "element": "automatic rifle"},
        {"name": "bow", "power": 16, "element": "wood"},
        {"name": "wooden sword", "power": 6, "element": "wood"},
        {"name": "thorny stick", "power": -1, "element": "wood"},
        {"name": "sword", "power": 26, "element": "steel"},
        {"name": "steel stick", "power": 4, "element": "steel"}
    ]

    filtred_mage_list = power_filter(mage_list, 10)
    print("FILTRED WITH 10 OBJ LIST :")
    for item in filtred_mage_list:
        print(item)
    print("")

    spell_list = [
        "stick",
        "cursed bow",
        "mega legendary AK47",
        "bow",
        "wooden sword",
        "thorny stick",
        "sword",
        "steel stick"
    ]
    transformed_spell_list = spell_transformer(spell_list)
    print("TRANSFORMED STR LIST :")
    for simple_item in transformed_spell_list:
        print(simple_item)
    print("")

    stats = mage_stats(mage_list)
    print("CALCULATED OBJ LIST :")
    for unpacked_item in stats.items():
        print(unpacked_item)
    print("")
