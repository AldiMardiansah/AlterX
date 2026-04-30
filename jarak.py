def konverter_jarak(satuan_awal, nilai_awal, satuan_hasil):
    data_konversi = {
        "m" : 1,
        "km" : 1000,
        "cm" : 0.01,
        "mm" : 0.001,
        "mil" : 1609.34,
        "yard" : 0.9144,
        "inci" : 0.0254,
        "kaki" : 0.3048,
        "satuan astronomi" : 149597870700, #149.597.870.700
        "sa" : 149597870700,
        "light year" :  9460730472580800, #9.460.730.472.580.800
        "ly" : 9460730472580800
    }

    if satuan_awal not in data_konversi or satuan_hasil not in data_konversi:
        return None

    meter = nilai_awal * data_konversi[satuan_awal]
    nilai_hasil = meter / data_konversi[satuan_hasil]

    return nilai_hasil
def menu_jarak():
    while True:
        print("\n-- Konversi Jarak --")
        print("Pilihan Satuan")
        print("Umum      : Mm   | Cm   |  M     | Km")
        print("Imperial  : Inci | Kaki |  Yard  | Mil")
        print("Astronomi : Satuan Astronomi (SA)| Light Year (ly)")
        try:
            satuan_awal = input("Masukkan Satuan Asal: ").lower()
            nilai_awal = float(input("Masukkan Nilai: "))
            satuan_hasil = input("Masukkan Satuan Hasil: ").lower()
            nilai_hasil = konverter_jarak(satuan_awal, nilai_awal, satuan_hasil)
            if nilai_hasil == None:
                print("Satuan tidak valid!")
            else:
                print(f"Hasil: {round(nilai_awal, 4)} {satuan_awal} = {round(nilai_hasil, 4)} {satuan_hasil}")

        except ValueError: 
            print("Input harus berupa angka!")

        print("\n1. Konversi lagi")
        print("0. Kembali ke menu utama")

        pilihan = input("Pilih: ")

        if pilihan == "0":
            break
    
    
