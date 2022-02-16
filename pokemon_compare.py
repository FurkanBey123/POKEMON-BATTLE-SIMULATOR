import pandas as pd
from functions import *

# ------------------------------MAIN POKEMON BATTLER CLASS-------------------------------------- #


class PokemonCompare:
    def __init__(self):
        self.data_frame = pd.read_csv("pokemon_stats.csv")
        self.score_board = {}
        self.score_board_creator()
        self.pokemon_compare()
        self.sorted_score_board = dict(sorted(self.score_board.items(), key=lambda item: item[1]))
        self.sorted_score_board = dict(reversed(list(self.sorted_score_board.items())))

    def score_board_creator(self):
        for pokemon in self.data_frame.itertuples():
            self.score_board[f"{pokemon[2]}"] = 0

    # ------------------------------MAIN POKEMON COMPARE FUNCTION------------------------------------- #
    def pokemon_compare(self):
        for attacker in self.data_frame.itertuples():
            for defender in self.data_frame.itertuples():
                attacker_type1 = attacker[3]
                attacker_type2 = attacker[4]
                defender_type1 = defender[3]
                defender_type2 = defender[4]
                attacker_name = attacker[2]
                defender_name = defender[2]
                attacker_atk = int(attacker[9])
                defender_atk = int(defender[9])
                attacker_special_atk = int(attacker[11])
                defender_special_atk = int(defender[11])
                attacker_hp = int(attacker[8])
                defender_hp = int(defender[8])
                attacker_def = int(attacker[10])
                defender_def = int(defender[10])
                attacker_special_def = int(attacker[12])
                defender_special_def = int(defender[12])

                if attacker_name != defender_name:
                    if attacker_atk > attacker_special_atk:
                        if defender_atk > defender_special_atk:
                            attacker_damage = battle_damage_calculator(attacker_type1, attacker_type2, defender_type1,
                                                                       defender_type2, attacker_atk, defender_def)
                            defender_damage = battle_damage_calculator(defender_type1, defender_type2, attacker_type1,
                                                                       attacker_type2, defender_atk, attacker_def)
                            while attacker_hp > 0 or defender_hp > 0:
                                if attacker_damage == 0:
                                    self.score_board[f"{defender_name}"] = self.score_board[f"{defender_name}"] + 1
                                    break
                                elif defender_damage == 0:
                                    self.score_board[f"{attacker_name}"] = self.score_board[f"{attacker_name}"] + 1
                                    break
                                defender_hp = (defender_hp - attacker_damage).__round__(2)
                                attacker_hp = (attacker_hp - defender_damage).__round__(2)
                                if defender_hp <= 0:
                                    self.score_board[f"{attacker_name}"] = self.score_board[f"{attacker_name}"] + 1
                                    attacker_hp = defender_hp = -1
                                elif attacker_hp <= 0:
                                    self.score_board[f"{defender_name}"] = self.score_board[f"{defender_name}"] + 1
                                    attacker_hp = defender_hp = -1

                        elif defender_atk <= defender_special_atk:
                            attacker_damage = battle_damage_calculator(attacker_type1, attacker_type2, defender_type1,
                                                                       defender_type2, attacker_atk, defender_def)
                            defender_damage = battle_damage_calculator(defender_type1, defender_type2, attacker_type1,
                                                                       attacker_type2, defender_special_atk,
                                                                       attacker_special_def)
                            while attacker_hp > 0 or defender_hp > 0:
                                if attacker_damage == 0:
                                    self.score_board[f"{defender_name}"] = self.score_board[f"{defender_name}"] + 1
                                    break
                                elif defender_damage == 0:
                                    self.score_board[f"{attacker_name}"] = self.score_board[f"{attacker_name}"] + 1
                                    break
                                defender_hp = (defender_hp - attacker_damage).__round__(2)
                                attacker_hp = (attacker_hp - defender_damage).__round__(2)
                                if defender_hp <= 0:
                                    self.score_board[f"{attacker_name}"] = self.score_board[f"{attacker_name}"] + 1
                                    attacker_hp = defender_hp = -1
                                elif attacker_hp <= 0:
                                    self.score_board[f"{defender_name}"] = self.score_board[f"{defender_name}"] + 1
                                    attacker_hp = defender_hp = -1

                    elif attacker_atk <= attacker_special_atk:
                        if defender_atk > defender_special_atk:
                            attacker_damage = battle_damage_calculator(attacker_type1, attacker_type2, defender_type1,
                                                                       defender_type2, attacker_special_atk,
                                                                       defender_special_def)
                            defender_damage = battle_damage_calculator(defender_type1, defender_type2, attacker_type1,
                                                                       attacker_type2, defender_atk, attacker_def)
                            while attacker_hp > 0 or defender_hp > 0:
                                if attacker_damage == 0:
                                    self.score_board[f"{defender_name}"] = self.score_board[f"{defender_name}"] + 1
                                    break
                                elif defender_damage == 0:
                                    self.score_board[f"{attacker_name}"] = self.score_board[f"{attacker_name}"] + 1
                                    break
                                defender_hp = (defender_hp - attacker_damage).__round__(2)
                                attacker_hp = (attacker_hp - defender_damage).__round__(2)
                                if defender_hp <= 0:
                                    self.score_board[f"{attacker_name}"] = self.score_board[f"{attacker_name}"] + 1
                                    attacker_hp = defender_hp = -1
                                elif attacker_hp <= 0:
                                    self.score_board[f"{defender_name}"] = self.score_board[f"{defender_name}"] + 1
                                    attacker_hp = defender_hp = -1

                        elif defender_atk <= defender_special_atk:
                            attacker_damage = battle_damage_calculator(attacker_type1, attacker_type2, defender_type1,
                                                                       defender_type2, attacker_special_atk,
                                                                       defender_special_def)
                            defender_damage = battle_damage_calculator(defender_type1, defender_type2, attacker_type1,
                                                                       attacker_type2, defender_special_atk,
                                                                       attacker_special_def)
                            while attacker_hp > 0 or defender_hp > 0:
                                if attacker_damage == 0:
                                    self.score_board[f"{defender_name}"] = self.score_board[f"{defender_name}"] + 1
                                    break
                                elif defender_damage == 0:
                                    self.score_board[f"{attacker_name}"] = self.score_board[f"{attacker_name}"] + 1
                                    break
                                defender_hp = (defender_hp - attacker_damage).__round__(2)
                                attacker_hp = (attacker_hp - defender_damage).__round__(2)
                                if defender_hp <= 0:
                                    self.score_board[f"{attacker_name}"] = self.score_board[f"{attacker_name}"] + 1
                                    attacker_hp = defender_hp = -1
                                elif attacker_hp <= 0:
                                    self.score_board[f"{defender_name}"] = self.score_board[f"{defender_name}"] + 1
                                    attacker_hp = defender_hp = -1
