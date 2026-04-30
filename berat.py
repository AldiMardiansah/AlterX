def konversi_berat(nilai, dari, ke):
    relasi_ke_gram = {
        "kg": 1000,
        "hg": 100,
        "dag": 10,
        "g": 1,
        "dg": 0.1,
        "cg": 0.01,
        "mg": 0.001
    }

    if dari not in relasi_ke_gram or ke not in relasi_ke_gram:
        return None

    nilai_gram = nilai * relasi_ke_gram[dari]
    hasil = nilai_gram / relasi_ke_gram[ke]

    return hasil


def menu_berat():
    while True:
        print("\n-- Konversi Berat --")
        print("Pilihan satuan: kg | hg | dag | g | dg | cg | mg")

        try:
            nilai = float(input("Masukkan nilai: "))
            dari = input("Dari satuan: ").strip().lower()
            ke = input("Ke satuan: ").strip().lower()

            hasil = konversi_berat(nilai, dari, ke)

            if hasil is None:
                print("Satuan tidak valid!")
            else:
                print(f"Hasil: {nilai} {dari} = {round(hasil, 4)} {ke}")

        except ValueError:
            print("Input harus berupa angka!")

        print("\n1. Konversi lagi")
        print("0. Kembali ke menu utama")

        pilihan = input("Pilih: ").strip()

        if pilihan == "0":
            break