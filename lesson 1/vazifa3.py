import json


tovar_nomi = input("Tovar nomini kiriting: ")
narxi = float(input("Tovar narxini kiriting: "))
rangi = input("Tovar rangini kiriting: ")
soni = int(input("Tovar sonini kiriting: "))

tovar = {
    "nomi": tovar_nomi,
    "narxi": narxi,
    "rangi": rangi,
    "soni": soni
}


with open("tovarlar.json", "w") as json_file:
    json.dump(tovar, json_file)

print("json fayliga saqlandi")

