from bs4 import BeautifulSoup
import requests

URL = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pokémon_by_National_Pokédex_number"


# ------------------------------CREATING URLS WITH POKEMON NAMES TO GET DATA-------------------------------------- #
class PokemonUrlsCreator:
    def __init__(self):
        self.pokemon_names = []
        self.response = requests.get(URL).text
        self.soup = BeautifulSoup(self.response, "html.parser")
        self.poke_name_search = self.soup.select(selector="div div table tbody tr th a img ")
        self.url_creator()

    def url_creator(self):
        with open("pokemon_urls.txt", "r+") as txt_file:
            txt_file.seek(0)
            txt_file.truncate()

        with open("pokemon_urls.txt", "a", encoding="utf-8") as data:
            for pokemon in self.poke_name_search:
                pokemon_name = pokemon['alt']
                if pokemon_name not in self.pokemon_names:
                    self.pokemon_names.append(pokemon_name)
                    data.write(f"https://bulbapedia.bulbagarden.net/wiki/{pokemon_name}_(Pokémon)\n")
