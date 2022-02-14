from pokemon_urls import PokemonUrlsCreator
from pokemon_stats_parser import PokemonStatsParser
from pokemon_compare import PokemonCompare
from google_spreadsheet import sheet_creator

# ------------------------------RUN FUNCTION FOR ALL CLASSES-------------------------------------- #


def main():
    urls = PokemonUrlsCreator()
    stats_parser = PokemonStatsParser()
    compare = PokemonCompare()
    upload = sheet_creator(compare.sorted_score_board)


if __name__ == '__main__':
    main()
