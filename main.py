from waktu import menu_waktu
from berat import menu_berat
from suhu import menu_suhu
from jarak import menu_jarak
from frekuensi import menu_frekuensi

def main():
    while True:
        print("\nMenu Konversi")
        print("1. Waktu")
        print("2. Berat")
        print("3. Suhu")
        print("4. Jarak")
        print("5. Frekuensi Suara")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_waktu()
        elif pilihan == "2":
            menu_berat()
        elif pilihan == "3":
            menu_suhu()
        elif pilihan == "4":
            menu_jarak()
        elif pilihan == "5":
            menu_frekuensi()
        elif pilihan == "0":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()