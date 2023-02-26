import library


def set_deposit(summa):
    txt = library.gryvni_kopiyki(summa)
    print(f"надана вами сума: {txt[0]} {txt[1]}")


set_deposit(input("Введіть сумму: "))

