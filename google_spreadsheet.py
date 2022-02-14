import time
from pokemon_compare import PokemonCompare
import gspread

service_account = gspread.service_account(filename="creds.json")
sheet = service_account.open("Best Pokemons Listed")
worksheet = sheet.worksheet("Sheet1")

COUNTER = 2
request_counter = 0

# ------------------------------WRITING DATAS ON GOOGLE SHEET-------------------------------------- #


def sheet_creator(pokemon_sorted_list):
    global COUNTER, request_counter
    for key, value in pokemon_sorted_list.items():
        worksheet.update(f"A{COUNTER}:B{COUNTER}", [[key, value]])
        COUNTER += 1
        request_counter += 1
        if request_counter == 50:
            request_counter = 0
            time.sleep(60)
    return print("SUCCESSFULLY ENDED")

