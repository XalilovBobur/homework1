import json


try:
    with open("tovarlar.json", "r") as json_file:
        tovarlar = json.load(json_file)
except FileNotFoundError:
    print("Tovarlar JSON fayli topilmadi")
    exit()


if isinstance(tovarlar, list):  
    for idx, tovar in enumerate(tovarlar, start=1):
        print(f"Tovar {idx}:")
        print(f"\tNomi: {tovar.get('nomi')}")
        print(f"\tNarxi: {tovar.get('narxi')}")
        print(f"\tRangi: {tovar.get('rangi')}")
        print(f"\tSoni: {tovar.get('soni')}")
        print("-" * 20)
else:  
    print("royxat bosh")