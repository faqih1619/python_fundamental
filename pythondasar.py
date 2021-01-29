######### PRINT #########
# => untuk menampilkan suatu program / output ke layar 
# Boleh memakai (" ") / (' ') dan tidak diakhiri dengan ";" seperti pada bahasa pemrograman yang lain
print("Hello World!")






######### KOMENTAR ########
# => digunakan untuk memberikan informasi terkait sebuah code
# tidak akan dijalankan,ditampilkan ke layar, dan tidak terpengaruh dengan apapun
# caranya dengan menggunakan tanda (#) atau ("""" isi komentar """")






######### VARIABEL #########
# => untuk menyimpan suatu data, baik berupa string / integer
# Tata nama yang baik : 
"""
  1) Tidak boleh pakai spasi  2) diawali dengan huruf kecil 
  3) boleh mengandung angka/simbol 4) dihubungkan dengan tanda _
  contoh :
  - A ; - a ; - namaSaya ; - nama_saya ; - abc123
"""
nama = "Muhammad faqih Khawarizmi"
kelas = "XI IPA 2 MA"

print("Nama saya",nama,"dan saya kelas",kelas)
# Boleh memakai '+' / ',' dalam menghubungkan suatu variable, tetapi lebih baik menggunakan ','






######### OPERATOR MATEMATIKA #########
# => digunakan dalam operasi matematika dan dalam kebutuhan lain
# Tambah (+)
print(10 + 20)
# Kurang (-)
print(50 - 30)
# Kali (*)
print(10*10)
# Bagi (/)
print(50/5)
# Modulo (%)
print(20 % 6)
# Pangkat (**)
print(2 ** 3)
# Pembagian bulat (//)
print(10//3) # harusnya hasilnya 3.xxxxx tetapi dibulatkan menjadi 3






######### MATH FUNCTIONS #########
# Referensi: overiq-numbers in python
# max => nilai maximum
print(max(1,2,3,4,5,6,7,8,9))
# min => nilai minimum
print(min(1,2,3,4,5,6,7,8,9))
# round => membulatkan angka (jika > 5 desimale,maka dibulatkan ke angka atase.begitu juga sebaliknya)
print(round(6.67))
# menggunakan modul math, pertama import modul math dahulu
# pilihannya ada banyak, ada math.sin,cos,tan,log,e,dll. CEK REFERENSI DIATAS
import math

luasLingkaran = math.pi*7*7

print(luasLingkaran)






######### TIPE DATA #########
# Numbers = int,float,complex; String; Tuple; List; Dictionary; Boolean
# String
stringg = "ini sebuah string"

print(type(stringg),stringg)
# Numbers (int)
intt = 50

print(type(intt),intt)
# Numbers (float)
floatt = 50.10

print(type(floatt),floatt)
# Numbers (complex)
complexx = 50.j

print(type(complexx),complexx)
# Tuple
tuplee = ('faqih','daffa','ilham')

print(type(tuplee),tuplee)
# List
listt = ['faqih','daffa','ilham']

print(type(listt),listt)
# Dictionary
dictionaryy = {'nama':'faqih', 'umur':30}

print(type(dictionaryy),dictionaryy)
# Boolean (True)
boolTrue = True

print(type(boolTrue),boolTrue)
# Boolean (False)
boolFalse = False

print(type(boolFalse),boolFalse)
a = 10
b = 20
c = "abc"

print(a > b)
print(a < b)
print(c.isalnum())






######### CONCATINATE(PENGGABUNGAN) #########
# => menggabungkan data data 
# pertama
a = 'faqih'
b = 'khawarizmi'

print(a,b) # atau # print(a + ' ' + b)
# kedua
c = 'saya'

print(c + ' faqih') # atau bisa juga
print(c,'faqih')
# ketiga
d = 10
e = 20

print(d + 10)
print(d + e)
# keempat
f = 17
g = 'faqih'
""" print(f + g) """ # ini akan error karena tidak bisa digabung int dg str, shg harus diubah formatnya 

print(str(f) +' ' + g) # tetapi tidak bisa mengubah str ke int, oleh karena itu lebih baik gunakan cara :
print(f,g) # dengan mengganti tanda tambah menjadi koma






######### ESCAPING #########
# mengatasi masalah seperti ketika butuh enter / tanda tertentu,dll
# enter
print("Nama saya adalah \nFaqih")
# ketika butuh tanda (' atau ")
print("ini butuh tanda (\") alias petik dua atas")
print("ini butuh tanda (\') alias petik satu atas")
# ketika butuh indentasi / tab
print("saat ini saya butuh \tindentasi")






######## STRING METHODS #########
# => terdiri dari banyak sekali syntax dan digunakan dalam mengolah, mengedit kata / kalimat
# referensi ada di w3school, nama subbab: string-methods
# capitalize() => untuk mengubah huruf di awal kalimat pembuka menjadi huruf besar
a = "assalaam surakarta"

print(a.capitalize())
print("assalaam maju".capitalize())
# lower() => mengubah semua huruf menjadi huruf kecil
print("ASSALAAM".lower())
# upper() => mengubah semua huruf menjadi huruf besar
print("assalaam".upper())
# title() => mengubah kalimat menjadi sesuai dengan tata nama judul
print("ledakan terjadi di kota beirut".title())
# replace() => mengubah suatu kata/kalimat/huruf
x = "Assalaam pondokku"

print(x.replace("pondokku","pondokmu"))






# Aplikasi sederhana dengan input
nama = input("Siapa nama anda? ")

print("siap",nama,"salam kenal.")

umur = input("oh iya,berapa umurmu? ")

print("oooo...umurmu",umur,"tahun, sama dong hihihi")






######### Conditional statement / Percabangan (if, else, elif) $ logical operator (and(&) or(|) not(!=)) #########
# untuk menentukan kondisi, jika true lakukan sesuatu, jika salah lakukan sesuatu
# contoh pertama
a = 10
b = 20

if a > b:
    print(a,"lebih besar dari",b)
else:
    print(a,"lebih kecil dari",b)

# contoh kedua
uang = int(input("kamu sekarang punya uang berapa? "))
hutang = 500000
kembalian = uang - hutang
kekurangan = hutang - uang

if uang == hutang:
    print("Terima kasih sudah membayar,uangnya pas yaa..")
elif uang > hutang:
    print("wah uangmu banyak,bisa bayar hutang dong, saya ada kembaliannya kok,ini kembaliannya",kembalian,)
else:
    print("waduh uangmu nggak cukup bro, kurang ",kekurangan)

# contoh ketiga dengan (logical operator)
syarat1 = True
syarat2 = False
# and (harus sama keduanya jika ingin True,begitupula dengan False)
if syarat1 & syarat2:
    print("ini True")
else:
    print("ini False")
# or (tidak harus sama keduanya jika ingin True,begitupula dengan False,cukup salah satu saja)
if syarat1 | syarat2:
    print("ini True")
else:
    print("ini False")
# Not (tidak ==)
if syarat1 != syarat2:
    print("ini True")
else:
    print("ini False")

# contoh keempat (mencari jodoh) dengan menerapkan conditional statement dan logical operator
tamu = "pria"
shalihah = True
rajin = True

if tamu == "wanita":
    if shalihah & rajin:
        print("saya siap menjadikanmu istri")
    else:
        print("maaf ya kamu bukan tipeku")
else:
    print("anda laki-laki, sedangkan saya sedang mencari perempuan,pergi sana")






######### LOOPING ########
# While loop
x = 0

while x < 5:
    print("ini angka ke:",x)
    x = x + 1
else:
    print("program berhenti di angka:",x)

# For loop
nama = ['faqih','galang','daffa','rizaldi','riduan']
kata = "faqih"

for i in nama:
    print("nama anda",i)

for a in kata:
    print("huruf",a)

# Loop Bercabang
a = 1

while a < 6:
    b = 0
    while b < a:
        print("*", end='')
        b = b + 1
    print()
    a = a + 1

# perkalian bercabang (1*1, 1*2 - 1*4 terus 2*1, 2*2 dst)
for a in range(1,5):
    for b in range(1,5):
        c = a*b
        print(c, end=' ')
    print()






######### BERMAIN DENGAN LIST #########
orang = ['faqih','fadhil','daffa','fauzan']
umur = [10,5,50,60]
campur = [10,'makan','ayam',2.5]
# index dimulai dengan 0 dan diakses dengan [no.index]
print(orang[1])
# menambahkan data ke list
orang.append('galang')
print(orang)
# mengedit data didalam list
orang[0] = 'rifqi'
print(orang)
# menghapus data dalam list
print(umur)
del umur[2]
print(umur)






######### BERMAIN DENGAN TUPLES #########
# merupakan list yang sifatnya imutable (tidak bisa diganti) dan ditulis dengan ()
# imutable = tidak bisa di edit, hapus, tambah
nama = ('faqih','daffa','nugraha','daffa')
angka = (20,75,35,98,120)
nama2 = ['fuad','haikal','dimas']

print(nama[3])
print(len(nama))
print(angka)
print(max(angka))
# mengkonversi tuples > list atau list > tuple
print(list(nama))
print(tuple(nama2))






######### BERMAIN DENGAN DICTIONARY #########
# terdiri dari key:value dan dibuka ditutup dengan {}
# indexnya = keynya
data = {'nama':'faqih',
        'age': '20',
        'hobby':'coding'
        }
# memanggil data
print('Namanya adalah',data['nama'])
# mengeloop data
# for key,value in data_yang_mau_diloop
for key,value in data.items():
    print(key + ' = ' + value)
# menambahkan data
data['dream'] = 'programmer'

print(data)
# mengedit data
data['nama'] = 'fauzan'
# menghapus data
del data['age']

print(data)






######### NESTED DICTIONARY #########
# merupakan dictionary bercabang
data = {1:{'nama':'faqih', 'age':'17', 'hobby':'coding'},
        2:{'nama':'fadhil', 'age':'18', 'hobby':'olahraga'},
        3:{'nama':'daffa', 'age':'16', 'hobby':'game'}
        }

print(data)
# mengakses data secara general
print(data[2])
# mengakses data lebih spesifik
print(data[2]['nama'])
# mengeloop data
for key,value in data.items():
    print('\nkeynya: ', key)
    for key2 in value:
        print(key2 + '-', value[key2])






######### BERKENALAN DENGAN SET #########
# => item yang tidak punya urutan, dan tidak boleh duplikat
orang = {'faqih', 'fauzan', 'fadil', 'faqih'}

print(orang)
# menambahkan data
orang.add('sojan')
# menghapus data
orang.remove('fadil')
print(orang)
# tidak bisa diakses = print(orang[0]) maka akan error

angka1 = {1,2,3,4,5}
angka2 = {4,5,6,7,8}

print(angka1 | angka2) # => Tanda | merupakan union, bukan atau
print(angka1 & angka2) # => Tanda & merupakan irisan
print(angka1 - angka2) # => Tanda - merupakan perbedaan
print(angka2 - angka1) # => Tanda - merupakan perbedaan
print(angka1 ^ angka2) # => Tanda ^ tidak menampilkan data yang sama






######### FUNGSI & PARAMETER ########
# adalah beberapa baris kode yang yang berada di dalam sebuah fungsi
# penulisan :
"""
    def namaFungsi:
        program (argumen / parameter)
"""
# contoh 1 sederhana
def fungsiA():
    print('=========')
    print('fqhkhwrzm')
    print('=========')
# pemanggilan
fungsiA()

# contoh 2 dengan argumen
# pemasangan nilai default dengan menambah parameter
def fungsiB(tulisan = 'tidak ada'):
    print('=========')
    print(tulisan)
    print('=========')
# pemanggilan
fungsiB('faqih123')
fungsiB() # ini tanpa parameter

# contoh 3 dengan 2 parameter
def penambahan1(a,b):
    c = a + b
    print('hasil pertambahan dari',a,'+',b,'adalah',c) # atau
    print('hasil dari a + b adalah',a + b)
# pemanggilan
penambahan1(10,50)






######### RETURN PADA FUNGSI #########
# return digunakan untuk mengembalikan nilai
# contoh 1
def penambahan2(a,b):
    return a + b

hasil1 = penambahan2(10,100)

penambahan2(10,20) # maka tidak akan menampilkan output, kecuali dengan 
print(penambahan2(10,20)) # maka ini akan jalan
print(penambahan2(hasil1,50))

# contoh 2
def perkalian1(a,b):
    c = a * b
    return c

hasil1 = perkalian1(10,100)

perkalian1(10,20) # maka tidak akan menampilkan output, kecuali dengan 
print(perkalian1(10,20)) # maka ini akan jalan
print(perkalian1(hasil1,50))






######### KEYWORD ARGUMENT #########
def keyarg(namee,hobbyy):
    print("Name: " + namee + " - hobby: " + hobbyy)

# keyarg('faqih','coding') => ini akan berjalan normal, tetapi jika:
# keyarg('coding','faqih') => maka ini akan terbalik, cara mengatasinya:
keyarg(hobbyy = 'masak', namee = 'fadhil')
# maka cara diatas ini normal walaupun terbalik, krn sudah diberi key






######### ARGS & KWARGS #########
# ARGS(*) = mengatasi jika inputan ternyata melebihi program
# KWARGS(**)  = mengatasi jika inputan memasukkan key and value
def argkwarg(name):
    print(name)

# argkwarg0('faqih') => maka ini akan normal, tapi bagaimana jika:
# argkwarg0('faqih','hilman') => maka ini akan error, cara mengatasinya:
# contoh args 
def argkwarg0(*args):
    for name in args:
        print(name)
    
argkwarg0('faqih','daffa','hasbi') # maka akan berjalan normal

# contoh kwargs
def argkwarg1(**kwargs):
    for key, value in kwargs.items():
        print(key + ' = ' + value)

argkwarg1(name = 'faqih', age = '20', hobby = 'coding')
# kode akan berjalan dengan normal






######### MODULE #########
# dengan menggunakan import, bagian ini berada di file bahanjar1.py
biodata = {'nama': 'faqih',
           'umur': '20',
           'kelas': 'sebelas'
           }

def latmodul(nama):
    print("Namamu adalah:",nama)






######### BUILT IN MODULE #########
# => modul yang bisa dipakai secara langsung
# reference : library python
# contoh : datetime = untuk melihat waktu sekarang di tempat kira berada
import datetime

now = datetime.datetime.now()

print(now)
# bisa juga menampilkan waktu dengan beberapa pilihan
print(now.strftime('%Y, %B, %d'))






######### LOCAL & GLOBAL VARIABEL #########
# 1 Global var = bisa dipangil dimana saja,asalkan deklarasi var spt ini
globalvar  = "Faqih"

def printNama():
    print('akses dari dalam:',globalvar)

printNama()
print("akses dari luar",globalvar)

# 2 Local var = hanya bisa dipangil di wilayah tempat pendeklarasian var
globalvar  = "Faqih"

def printNama0():
    localvar = "khawarizmi"
    print('akses dari dalam:',globalvar)
    print('akses dari dalam:',localvar)

printNama0()
# print("akses dari luar",localvar) 
# maka variabel tidak akan dipanggil diatas ini dan error 
# jika ingin mengedit var di dalam local var, maka harus diubah ke:
# syntax = global nama_variabel

# 3 contoh global & local
globalvar  = "Faqih"

def printNama1():
    localvar = "khawarizmi"
    print('akses dari dalam:',globalvar)
    print('akses dari dalam:',localvar)

printNama1()
print("akses dari luar",globalvar)

# 4 contoh mengedit local var
name = 'FAQIH'

def printName():
    global name
    name = name + 'KHAWARIZMI'
    print(name)

printName()
print(name)






######### EXCEPTIONS #########
# => menangani error
# reference: tutorialspoint
# fungsi raise = untuk menghentikan program dimanapun kita mau jika eror
# contoh 1
"""
    bug = 'faqih'

    raise Expection("ada eror")

    bugi = i + bug
    print(bugi)
    print("finish")
    # maka print finish tidak akan berjalan, karena terdapat raise
"""

# contoh 2
# menggunakan try except (konsepnya hampir == conditional statement)
bug0 = 'makan'

try:
    print(bugg + bug0)
except NameError:
    print("ada error di bugg + bug0 di penamaan var")
# untuk except NamaError ada banyak : 
# NameError, ValueError, IndexError, SyntaxError
# kalau ingin secara general, gunakan except saja

# contoh 3
"""
    import sys
    def is_it_macbook():
        assert("Macbook" in sys.platform), "kalimat ditaruh disini"

    is_it_macbook()
    print('finish')
"""
# maka finish tidak dijalankan, dan yang dijalankan di dlm fungsi






######### __main__ #########
# => berfungsi jika ingin memakai modul
# => sebagai titik utama file / main file, dijalankan dengan syntax __name__
# contoh ada di sini dan file mainname.py
import main_name as m 

m.tambah(10,20)
m.kurang(20,10)

# Maka di file ini fungsi main tidak dijalankan karena menganngap bahwa:
# - file ini adalah file matematika dan bukan __main__ file






######### PENGENALAN CLASS #########
# => Atau bisa juga disebut template yang terdiri dari beberapa objek/instance yang bisa dipakai berkali-kali
class santri():
    nama = "nama"
    kelas = "kelas"
    absen = "absen"
# Nama,Kelas,Absen disebut attribut / objek / instance

faqih = santri()

faqih.nama = "Muhammad Faqih Khawarizmi"
faqih.kelas = "11 IPA 2 MA"
faqih.absen = "23"

print(faqih.nama)
print(faqih.kelas)
print(faqih.absen)






######### MEMBUAT METHOD (FUNGSI DI DLM CLASS) #########
# jangan lupa menggunakan param self pada fungsinya agar mereturnkan ke classnya
class future():
    nama = "Nama"

    def serius(self,namaPelajaran):
        print(self.nama,"Sedang serius belajar",namaPelajaran)

    def tidur(self,namaPelajaran):
        print(self.nama,"Sedang tidur nyenyak saat pelajaran",namaPelajaran)
# Fungsi self tersebut bisa dibilang mereturn ke class future() dg objek nama
# main program
faqih = future()
daffa = future()

faqih.nama = "faqih khawarizmi"
daffa.nama = "daffa nugraha"

faqih.serius("Matematika")
daffa.tidur("Matematika")






######### __init__() #########
# => init = akan otomatis berjalan saat menginisialisasi program class
# akan otomatis berjalan walaupun tidak dipanggil 
# Berbentuk seperti def
# contoh 1
class separoo():
    nama = "nama"

    def __init__(self):
        print("ini initialize")

    def seriuss(self,namaPelajaran):
        print(self.nama,"Sedang serius belajar",namaPelajaran)

    def tidurr(self,namaPelajaran):
        print(self.nama,"Sedang tidur nyenyak saat pelajaran",namaPelajaran)

# Main program

faqih = separoo()
faqih.nama = "faqih"
# Maka saat faqih diinisialisasi maka init akan otomatis berjalan 
faqih.seriuss("Pemrograman")

# contoh 2
class separo():
    def __init__(self, input_nama, input_nilai):
        self.nama = input_nama
        self.nilai = input_nilai

    def seriuss(self,namaPelajaran):
        print(self.nama,"Sedang serius belajar",namaPelajaran)

    def tidurr(self,namaPelajaran):
        print(self.nama,"Sedang tidur nyenyak saat pelajaran",namaPelajaran)

# Main program

faqih = separo("Muhammad Faqih", 100)

print("Namanya =",faqih.nama,"\nNilainya =",faqih.nilai)

faqih.seriuss("Pemrograman")






######### PRIVATE ATTRIBUTE #########
# => Agar tidak bisa diakses oleh orang lain maupun hacker (diproteksi)
# dengan menambah simbol __namaVar "_ 2 kali"
class privasi():
    jurusan = "MIPA" # public
    __nilai = 0 # private

    def __init__(self,input_nama,input_nik):
        self.nama = input_nama
        self.nik = input_nik

    def uts(self,input_nilai):
        self.__nilai += input_nilai

    def uas(self,input_nilai):
        self.__nilai += input_nilai

    def cek(self):
        if self.__nilai <= 50:
            print(self.nama,'Anda Tidak Lulus')
        else:
            print(self.nama,'Anda Lulus')

# main program

faqih = privasi("faqih",1223448)
daffa = privasi("daffa",1244556)

faqih.uts(10)
faqih.uas(50)
faqih.cek()
daffa.uts(5)
daffa.uas(10)
daffa.cek()
# print(faqih.__nilai) maka tidak bisa diakses karena private dan terproteksi






######### CLASS VARIABLE #########
# => untuk memanage variable di class apakah mau dioverride(timpa) / tidak
# contoh 1
class kelas_ma():
    # saat awal semua jurusan = data science
    jurusan = "Data science"

    def __init__(self, input_nama, input_nik):
        self.nama = input_nama
        self.nik = input_nik

# main program

faqih = kelas_ma("faqih",12345)
daffa = kelas_ma("daffa",67890)

faqih.jurusan = "Bioinformatics"
# maka faqih mjd bionformatics krn class variable nya tertimpa variable instance
print(kelas_ma.jurusan)
print(faqih.jurusan)
print(daffa.jurusan)

# contoh 2
class kelasku():
    # saat awal murid = 0
    murid = 0

    def __init__(self, input_nama, input_nik):
        self.nama = input_nama
        self.nik = input_nik
        kelasku.murid += 1

# main program
# saat diinisialisasi maka jmlh murid bertambah tiap inisialisasi
faqih = kelasku("faqih",12345)
daffa = kelasku("daffa",67890)
fauzan = kelasku("fauzan",98765)
# maka skrng jumlah murid mejadi 3
print(kelasku.murid)






######### CLASS INHERITANCE (keturunan) #########
# => Mendapatkan warisan / turunan dari program yang kita mau ambil
# dan sesuai kaidah programming yaitu jangan sampai melakukan DRY
# Don't Repeat Yourself, mksdnya kalau ada hal yang sama jangan diulang lagi
# tetapi bisa mengoverride (menimpa) apa yg ada di parent dan bisa menambah code
# contoh:
class Ojek():
    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id(self):
        print('nama:',self.nama,'\nmotor:',self.transmisi,'\ndaerah:',self.daerah)

class Gojek(Ojek):
# Maka class Gojek mewarisi semua program class Ojek, tetapi dapat diedit juga 
    def cek_id(self):
        print("Silahkan cek di dalam aplikasi-nya")

ojek1 = Ojek("Mamang","Matic","Jakarta")
ojek2 = Gojek("babang","Automatic","Banfung")

ojek1.cek_id()  # maka akan sesuai dengan program di class Ojek
ojek2.cek_id()  # maka akan sesuai dengan program di class Gojek






######### INPUT OUTPUT FILE.TXT #########
# => untuk membackup program ke dalam text
# harus diawali dengan kode = namaVar = open("nama_file","mode").dan diakhiri dengan file.close()
# isi perintahnya :
""" 
w = menulis file (akan menimpa file yang lama), jika file belum dibuat maka akan otomatis dibuatkan
r = membaca file (hanya bisa membaca)
a = menambahkan data di akhir baris (tidak menimpa)
r+ = membaca dan menulis file
dll , referensi : w3school, tutorialspoint
"""
# menulis file
file1 = open("data.txt","w")

file1.write("INFO LOGIN")
file1.write("\nini buat nama")
file1.write("\nini buat email")
file1.write("\nini buat password")

file1.close()

# membaca file
file2 = open("data.txt","r")

#print(file2.read()) # maka file akan ditampilkan ke terminal
print(file2.readline()) # maka file akan ditampilkan perbaris)

file2.close()

# menambahkan data ke dalam file
file3 = open("data.txt","a")

file3.write("\nini adalah baris baru dan yang terakhir")

file3.close()






######## MEMBUAT GUI (Graphical User Interface) DG TKINTER ########
# => untuk menampilkan sebuah layar yang berisi output dari codenya
# => referensi built-in ada di web python.org (web resmi python)
import tkinter

main_window = tkinter.Tk() # untuk menampilkan layar GUI

def selama_ditekan():
    label2 = tkinter.Label(main_window, text="Aku ditekan '_'")
    label2.pack() # fungsi pack = untuk meekspor codenya ke layar GUI

label = tkinter.Label(main_window, text ="Halo selamat datang di \n GUI sederhana")
# label = untuk membuat tulisan dg format label(varLayar, text="", command,dll)
tombol = tkinter.Button(main_window, text = "Tekan Saya", command = selama_ditekan)

label.pack() # fungsi pack = untuk meekspor codenya ke layar GUI secara berurutan
tombol.pack() # untuk meekspor codenya ke layar GUI shg tombol ada di bwh label
main_window.mainloop() # agar kode tidak berhenti dan hanya berhenti ketika di close






######### EKSTERNAL PACKAGE dg PIP #########
# referensi package ada di: pypi python package
"""
    cara memasang: (pastikan terkoneksi internet)
    1) pip install nama_package
"""
# contoh (package numpy)
import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
# maka akan menambahkan perkomponen
print(a+b)

# contoh (package pillow)
from PIL import Image

im = Image.open("foto.png")

print("format file:",im.format)
print("size file:",im.size)
print("mode file:",im.mode)

# im.show() => untuk menampilkan file

#============================ END ============================#
