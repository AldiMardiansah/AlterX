def konversi_frekuensi(nilai, dari, ke):
    relasi_ke_hz = {
        "hz": 1,
        "khz": 1000,
        "mhz": 1_000_000
    }

    if dari not in relasi_ke_hz or ke not in relasi_ke_hz:
        return None

    nilai_hz = nilai * relasi_ke_hz[dari]
    hasil = nilai_hz / relasi_ke_hz[ke]

    return hasil


def menu_frekuensi():
    while True:
        print("\n-- Konversi Frekuensi --")
        print("Pilihan satuan: hz | khz | mhz")

        try:
            nilai = float(input("Masukkan nilai: "))
            dari = input("Dari satuan: ").lower()
            ke = input("Ke satuan: ").lower()

            hasil = konversi_frekuensi(nilai, dari, ke)

            if hasil is None:
                print("Satuan tidak valid!")
            else:
                print(f"Hasil: {nilai} {dari} = {hasil} {ke}")

        except ValueError:
            print("Input harus berupa angka!")

        print("\n1. Konversi lagi")
        print("0. Kembali ke menu utama")

        pilihan = input("Pilih: ")

        if pilihan == "0":
            break