def konverter_suhu(satuan_awal, nilai_awal, satuan_hasil):
    
    if satuan_awal in "Celcius":
        suhu = nilai_awal
    elif satuan_awal in "Kelvin":
        suhu = nilai_awal - 273.15
    elif satuan_awal in "Fahrenheit":
        suhu = (nilai_awal - 32) * 5/9
    elif satuan_awal in "Reamur":
        suhu = nilai_awal * 5/4
    else:
        return None

    if satuan_hasil in "Celcius":
        nilai_hasil = suhu
    elif satuan_hasil in "Kelvin":
        nilai_hasil = suhu + 273.15
    elif satuan_hasil in "Fahrenheit":
        nilai_hasil = (suhu * 9/5) + 32
    elif satuan_hasil in "Reamur":
        nilai_hasil = suhu * 4/5
    else:
        return None

    return nilai_hasil
def menu_suhu():
    while True:
        print("\n-- Konversi Suhu --")
        print("Pilihan Satuan: Kelvin(K) | Celcius(C) | Fahrenheit(F) | Reamur(R)")
        
        try:
            satuan_awal = input("Masukkan Satuan Asal: ").capitalize()
            nilai_awal = float(input("Masukkan Nilai: "))
            satuan_hasil = input("Masukkan Satuan Hasil: ").capitalize()
            nilai_hasil = konverter_suhu(satuan_awal, nilai_awal, satuan_hasil)
            if nilai_hasil == None:
                print("Satuan tidak valid!")
            else:
                print(f"Hasil: {nilai_awal} {satuan_awal[0]} = {nilai_hasil} {satuan_hasil[0]}")

        except ValueError: 
            print("Input harus berupa angka!")

        print("\n1. Konversi lagi")
        print("0. Kembali ke menu utama")

        pilihan = input("Pilih: ")

        if pilihan == "0":
            break    