try:
    a = input("Kiruvchi ma'lumotni kiriting: ")
    k = int(a)
    print("Kiruvchi ma'lumot int ga aylantirildi: ", k)

except ValueError:
    print("Xatolik! Ma'lumotni int ga aylantirishda xato yuz berdi")
