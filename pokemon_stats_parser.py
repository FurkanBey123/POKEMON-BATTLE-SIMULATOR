from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
import requests

# ------------------------------PARSING THE HTML FILES TO GET DATAS-------------------------------------- #


class PokemonStatsParser:
    def __init__(self):
        self.pokemon_stats_csv = {
            "POKEDESK NUMBER": [],
            "NAME": [],
            "TYPE1": [],
            "TYPE2": [],
            "COLOR": [],
            "HEIGHT": [],
            "WEIGHT": [],
            "HP": [],
            "ATK": [],
            "DEF": [],
            "SP ATK": [],
            "SP DEF": [],
            "SPD": [],
            "TOTAL": []
        }
        self.data_parser()

    # ------------------------------DATA PARSER MAIN FUNCTION-------------------------------------- #
    def data_parser(self):
        with open("pokemon_urls.txt", "r", encoding="utf-8") as url_data:
            data_content = url_data.readlines()

            # ------------------------------PARSING THE FIRST TABLE TO GET BASIC INFO--------------------------------#
            for url in data_content:
                stripped_content = url.strip()
                response = requests.get(stripped_content)
                html_content = html.fromstring(response.content)
                poke_name_search = html_content.xpath(
                    '//*[@id="mw-content-text"]/div/table[2]/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[1]/big/big/b')[
                    0].text
                pokedesk_number = html_content.xpath(
                    '//*[@id="mw-content-text"]/div/table[2]/tbody/tr[1]/td/table/tbody/tr[1]/th/big/big/a/span')[
                    0].text
                type1 = html_content.xpath(
                    '//*[@id="mw-content-text"]/div/table[2]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[1]/a/span/b')[
                    0].text
                type2 = html_content.xpath(
                    '//*[@id="mw-content-text"]/div/table[2]/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/a/span/b')[
                    0].text
                color = html_content.xpath(
                    '/html/body/div[2]/div[1]/div[3]/div[5]/div[4]/div/table[2]/tbody/tr[11]/td[1]/table/tbody/tr/td/text()')[
                    0].strip()
                self.pokemon_stats_csv["POKEDESK NUMBER"].append(pokedesk_number)
                self.pokemon_stats_csv["NAME"].append(poke_name_search)
                self.pokemon_stats_csv["TYPE1"].append(type1)
                self.pokemon_stats_csv["TYPE2"].append(type2)
                self.pokemon_stats_csv["COLOR"].append(color)
                try:
                    height = html_content.xpath(
                        '//*[@id="mw-content-text"]/div/table[2]/tbody/tr[6]/td[1]/table/tbody/tr[1]/td[2]')[
                        0].text.strip()
                    weight = html_content.xpath(
                        '//*[@id="mw-content-text"]/div/table[2]/tbody/tr[6]/td[2]/table/tbody/tr[1]/td[2]')[
                        0].text.strip()
                    self.pokemon_stats_csv["HEIGHT"].append(height)
                    self.pokemon_stats_csv["WEIGHT"].append(weight)
                except IndexError:
                    height = html_content.xpath(
                        '//*[@id="mw-content-text"]/div/table[2]/tbody/tr[5]/td[1]/table/tbody/tr[1]/td[2]')[
                        0].text.strip()
                    weight = html_content.xpath(
                        '//*[@id="mw-content-text"]/div/table[2]/tbody/tr[5]/td[2]/table/tbody/tr[1]/td[2]')[
                        0].text.strip()
                    self.pokemon_stats_csv["HEIGHT"].append(height)
                    self.pokemon_stats_csv["WEIGHT"].append(weight)

                # ------------------------------STATS TABLE ANALYZER-------------------------------------- #
                soup = BeautifulSoup(response.text, "html.parser")
                table = soup.select_one(selector="#mw-content-text")
                hp = table.select(selector="div table tbody tr th div")[1].text
                attack = table.select(selector="div table tbody tr th div")[3].text
                defense = table.select(selector="div table tbody tr th div")[5].text
                sp_attack = table.select(selector="div table tbody tr th div")[7].text
                sp_defense = table.select(selector="div table tbody tr th div")[9].text
                speed = table.select(selector="div table tbody tr th div")[11].text
                total = table.select(selector="div table tbody tr th div")[13].text
                self.pokemon_stats_csv["HP"].append(hp)
                self.pokemon_stats_csv["ATK"].append(attack)
                self.pokemon_stats_csv["DEF"].append(defense)
                self.pokemon_stats_csv["SP ATK"].append(sp_attack)
                self.pokemon_stats_csv["SP DEF"].append(sp_defense)
                self.pokemon_stats_csv["SPD"].append(speed)
                self.pokemon_stats_csv["TOTAL"].append(total)
        return pd.DataFrame(self.pokemon_stats_csv).to_csv('pokemon_stats.csv', index=False)
