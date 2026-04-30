def konversi_waktu(nilai, dari, ke):
    relasi_ke_detik = {
        "detik": 1,
        "menit": 60,
        "jam": 3600
    }

    if dari not in relasi_ke_detik or ke not in relasi_ke_detik:
        return None

    nilai_detik = nilai * relasi_ke_detik[dari]
    hasil = nilai_detik / relasi_ke_detik[ke]

    return hasil


def menu_waktu():
    while True:
        print("\n-- Konversi Waktu --")
        print("Pilihan satuan: detik | menit | jam")

        try:
            nilai = float(input("Masukkan nilai: "))

            dari = input("Dari satuan: ").strip().lower()
            ke = input("Ke satuan: ").strip().lower()

            hasil = konversi_waktu(nilai, dari, ke)

            if hasil is None:
                print("Satuan tidak valid!")
            else:
                print(f"Hasil: {nilai} {dari} = {round(hasil, 2)} {ke}")

        except ValueError:
            print("Input harus berupa angka!")

        print("\n1. Konversi lagi")
        print("0. Kembali ke menu utama")

        pilihan = input("Pilih: ").strip()

        if pilihan == "0":
            break