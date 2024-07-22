def check_link(link):
    if link.startswith("http://") or link.startswith("https://"):
        print("Link tekshiruv muvaffaqiyatli boldi")
    else:
        raise ValueError("Link http yoki https bilan boshlanishi kerak")

user_input = input("Linkni kiriting: ")

try:
    check_link(user_input)
except ValueError as error:
    print(f"Xatolik: {error}")
    exit(1)
