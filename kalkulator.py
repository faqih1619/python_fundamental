##### PROJECT MEMBUAT KALKULATOR #####
"""
    1. Menampilkan pilihan operasi
    2. User memilih operasi (tambah/kurang/kali/bagi)
    3. User memasukkan angka pertama dan kedua
    4. Menampilkan output
    5. User memilih apakah mau melanjutkan operasi atau tidak
    6. Jika iya maka user akan memilih operasi kembali
    7. Jika tidak maka keluar dari program
"""

# 1. Membuat fungsi operasi

def Pertambahan(a,b):
    return a + b

def Pengurangan(a,b):
    return a - b

def Perkalian(a,b):
    return a * b

def Pembagian(a,b):
    return a / b

# 2. Membuat program
print("=======================")
print("Pilih operasi berikut")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("=======================")

while True:
    # Ambil data dari user
    choice = input("pilih (1/2/3/4) = ")
    # Lakukan conditional statement pertama
    if choice in ("1","2","3","4"):
        angka_pertama = float(input("Masukkan angka pertama = "))
        angka_kedua   = float(input("Masukkan angka kedua = "))

        # conditional statement kedua untuk menentukan pilihan
        if choice == "1":
            print("Anda memilih operasi pertambahan")
            print(angka_pertama, "+", angka_kedua, "=", Pertambahan(angka_pertama,angka_kedua))
        
        elif choice == "2":
            print("Anda memilih operasi pengurangan")
            print(angka_pertama, "-", angka_kedua, "=", Pengurangan(angka_pertama,angka_kedua))

        elif choice == "3":
            print("Anda memilih operasi perkalian")
            print(angka_pertama, "x", angka_kedua, "=", Perkalian(angka_pertama,angka_kedua))

        elif choice == "4":
            print("Anda memilih operasi pembagian")
            print(angka_pertama, ":", angka_kedua, "=", Pembagian(angka_pertama,angka_kedua))
        
        x = input("mau lanjut lagi? (y/n) ")

        if x in ("y","n"):
            if x == "y":
                print("Silahkan menggunakan kalkulator lagi ^_^")
                continue
            elif x == "n":
                print("Terimakasih sudah memakai kalkulator ^_^")
                break
        else:
            y = input("Masukkan pilihan yang benar (y/n) ")

            if y in ("y","n"):
                if y == "y":
                    continue
                elif y == "n":
                    print("Terimakasih sudah memakai kalkulator ^_^")
                    break
                else:
                    break
            else:
                print("Masukkan pilihan yang benar, ulangi program!")
                break
    else:
        print("Masukkan pilihan yang benar antara (1/2/3/4)")


