def write_list(lst):
    with open("index.txt", "w") as file:
        for line in lst:
            file.write(line + "\n")
    print("Ma'lumotlar faylga muvaffaqiyatli saqlandi")

lines = ["Bu yolbars", "Bu tulki", "Bu quyon"]
write_list(lines)
