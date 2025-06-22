def cek_ganjil_genap():
    try:
        angka = int(input("Masukkan angka yang ingin Anda cek: "))
        if angka % 2 == 0:
            print(f"{angka} adalah bilangan genap!")
        else:
            print(f"{angka} adalah bilangan ganjil!")
    except ValueError:
        print("Input yang Anda berikan salah")

cek_ganjil_genap()
