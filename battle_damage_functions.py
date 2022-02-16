import json
import random

ATTACKER_LEVEL = 30
ATTACK_POWER = 100
TYPE_BONUS = 1

with open("pokemons_type_chart.json", "r") as chart_data:
    chart_data = json.load(chart_data)

# ------------------------------CALCULATING EXTRA DAMAGE ACCORDING TO POKEMON TABLE-------------------------------------- #


def type_modifiers_calculator(attack_type1, attack_type2, defend_type1, defend_type2):
    if attack_type2 != "Unknown":
        if defend_type2 != "Unknown":
            attack_1_with_type_1 = chart_data[f"{attack_type1.lower()}"][f"{defend_type1.lower()}"]
            attack_2_with_type_1 = chart_data[f"{attack_type1.lower()}"][f"{defend_type2.lower()}"]
            total_type_1 = attack_1_with_type_1 * attack_2_with_type_1

            attack_1_with_type_2 = chart_data[f"{attack_type2.lower()}"][f"{defend_type1.lower()}"]
            attack_2_with_type_2 = chart_data[f"{attack_type2.lower()}"][f"{defend_type2.lower()}"]
            total_type_2 = attack_1_with_type_2 * attack_2_with_type_2

            if total_type_1 >= total_type_2:
                total = total_type_1
            else:
                total = total_type_2
        else:
            attack_1_with_type_1 = chart_data[f"{attack_type1.lower()}"][f"{defend_type1.lower()}"]
            total_type_1 = attack_1_with_type_1

            attack_1_with_type_2 = chart_data[f"{attack_type2.lower()}"][f"{defend_type1.lower()}"]
            total_type_2 = attack_1_with_type_2

            if total_type_1 >= total_type_2:
                total = total_type_1
            else:
                total = total_type_2

    else:
        if defend_type2 != "Unknown":
            attack_1_with_type_1 = chart_data[f"{attack_type1.lower()}"][f"{defend_type1.lower()}"]
            attack_2_with_type_1 = chart_data[f"{attack_type1.lower()}"][f"{defend_type2.lower()}"]
            total = attack_1_with_type_1 * attack_2_with_type_1
        else:
            attack_1_with_type_1 = chart_data[f"{attack_type1.lower()}"][f"{defend_type1.lower()}"]
            total = attack_1_with_type_1
    if total == 10 or total == 20 or total == 5:
        total = total * 10
    return float(total / 10).__round__(1)

# ------------------------CALCULATING ALL DAMAGE ACCORDING TO ATTACKER AND DEFENDER POKEMON----------------------- #


def battle_damage_calculator(attacker_type1, attacker_type2, defender_type1, defender_type2, attacker_attack,
                             defender_defence):
    battle_damage = (((((2 * ATTACKER_LEVEL / 5) + 2) * attacker_attack * ATTACK_POWER) / defender_defence / 50) + 2) \
                    * TYPE_BONUS * type_modifiers_calculator(attacker_type1, attacker_type2, defender_type1,
                                                             defender_type2) \
                    / 10 * random.randint(217, 255) / 255
    return battle_damage.__round__(2)
