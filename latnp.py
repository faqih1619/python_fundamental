######### NUMPY (INTRO) #########
"""

"""






######### NUMPY (INSTALASI) #########
# => cara menginstall = pip install numpy (di terminal)
# contoh sederhana (perbedaan list dan array pada numpy)
import numpy as np

a0 = np.array([1,2,3,4,5])
b0 = [1,2,3,4,5]

print(a0) # output yang ditampilkan tidak menampilkan komanya
print(b0) # output yang ditampilkan menampilkan komanya

a0 = a0 + 1 # tidak usah menggunakan kurung untuk array numpy
b0 = b0 + [1] # menggunakan kurung karena tipe data list

print(a0) # maka 1 akan ditambahkan pada setiap komponen
print(b0) # maka 1 akan ditambahkan di akhir array






######### MEMBUAT NUMPY ARRAY #########
# membuat vektor
a1 = np.array([1,2,3,4,5]) 
# jika angka pertama berupa desimal maka semuanya jadi desimal
print(a1)
# format penulisan = np.array([masukkan angka])

# membuat vektor dengan range
b1 = np.arange(1,10,2) 
# 1 = batas bawah, 10 = batas atas, 2 = step/selisih
print(b1)
# format penulisan = np.arange(batasBawah,batasAtas,selish)

# membuat linspace
c1 = np.linspace(1,10,5) 
# 1 = batas bawah, 10 = batas atas, 5 = hanya menampilkan 5 angka dengan selisih yang sama
print(c1)
# format penulisan = np.linspace(batasBawah,batasAtas,jumlahAngka)

# array multidimensi (matriks)
d1 = np.array([ (1,2,3) , (4,5,6) , (7,8,9) ])
# 1,2,3 = baris pertama, 4,5,6 = baris kedua dst
print(d1)
# format penulisan = np.array([(input angka baris 1) , (input angka baris 2)])

# matriks dengan nilai 0
e1 = np.zeros((5,3))
# format = np.zeros((jumlahBaris,jumlahKolom))
print(e1)

# matriks dengan nilai 1
f1 = np.ones((5,3))
# format = np.ones((jumlahBaris,jumlahKolom))
print(f1)

# matriks identitas ( yang matriks 0 1 )
g1 = np.identity(5) 
# atau dengan format np.eye(inputBarisKolom)
print(g1)






######### OPERASI ARITMATIKA #########
# deklarasi array list
a2 = [1,2,3,4,5]
b2 = [6,7,8,9,10]
# deklarasi array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

### ELEMENTWISE OPERATION
## pertambahan
list_tambah = a2 + b2
numpy_tambah = anp + bnp

print(list_tambah)
print(numpy_tambah)

## pengurangan
# list_kurang = a2 - b2 akan error karena list tidak suport pengurangan
numpy_kurang = anp - bnp

# print(list_kurang)
print(numpy_kurang)

## perkalian
#list_kali = a2 * b2 akan error karena list tidak suport perkalian
numpy_kali = anp * bnp

#print(list_kali)
print(numpy_kali)

## pembagian
#list_bagi = a2 / b2 akan error karena list tidak suport pembagian
numpy_bagi = anp / bnp

#print(list_bagi)
print(numpy_bagi)

## perpangkatan
#list_pangkat = a2 ** 2 akan error karena list tidak suport pembagian
numpy_pangkat = anp ** 2

#print(list_pangkat)
print(numpy_pangkat)

## multidimensi array numpy
c2 = np.array([
             (1,2,3),
             (4,5,6)
             ])
d2 = np.array([
             (7,8,9),
             (10,11,12)
             ])
# atau formatnya boleh:
"""
    c2 = np.array(([1,2,3] , [4,5,6]))
    d2 = np.array(([7,8,9] , [10,11,12]))
"""
arnum = c2 + d2
print(arnum)






######### INDEXING, SLICING, ITERASI #########
a3 = np.arange(10)**2 
# mksdnya = bikinkan array - 10 tetapi tiap nilai dipangkat 2
print(a3)

# indexing dan slicing
print("Nilai awal sampai selesai adalah", a3[:])
print("Nilai awal sampai ke-5 adalah", a3[:5])
print("Nilai ke-3 sampai ke-6 adalah", a3[2:6])
print("Nilai ke-2 adalah", a3[1])
print("Nilai ke-5 adalah", a3[4])

# iterasi
for i in a3:
    print("Nilainya =", i)






######### PERKALIAN MATRIX #########
# definisikan matriksnya
a4 = np.array(([1,2] , [3,4]))
b4 = np.ones([2,2])

print("Matriks A:")
print(a4)
print("Matriks B:")
print(b4)
# operasi perkalian matriks dengan format np.dot(matriks1,martriks2)
kali_matriks1 = np.dot(a4,b4)
kali_matriks2 = a4.dot(b4)
# hasil
print("Hasil perkalian matriks:")
print(kali_matriks1)






######### MANIPULASI MATRIKS #########
a5 = np.array((
             [1,2,3],
             [4,5,6]
             ))

# shape = mengetahui bentuk / ukuran matriksnya
print("Matrix a ukurannya:", a5.shape)
print(a5)

# transpose matrix = mengubah baris menjadi kolom
print("Transpose matrix a adalah:")
print(a5.transpose())
print(np.transpose(a5))
print(a5.T)
print("Matrix a ukurannya:", a5.shape)

# flatten array = vektor baris (mengubah bentuk vektor mjd baris semua)
print("Flatten matrix a adalah:")
print(a5.ravel())
print(np.ravel(a5))
print("Matrix a ukurannya:", a5.shape)

# reshape matrix = mengubah bentuk / ukuran matrix
print("Reshape matriks a adalah:")
print(a5.reshape(3,2)) # intinya jumlah / ukuran harus sama 
# misal ukuran 2 x 4 maka bisa diubah mjd 4 x 2 / 8 x 1 / 1 x 8
print("Matrix a ukurannya:", a5.shape)

# resize matrix = benar-benar mengubah ukuran matrix
print("Resize matriks a adalah:")
a5.resize(3,2)
print(a5)
print("Matrix a ukurannya:", a5.shape)

"""
    catatan: reshape,flatten,transpose itu hanya mereturn nilai sehingga 
    nilai asli tidak berubah, tetapi jika resize maka benar benar mengubah
    bentuk matriksnya
"""






######### STACKING MATRIX #########
# => Menumpuk matrix
a6 = np.array((1,2,3))
b6 = np.array((4,5,6))

aMat = np.zeros((3,3))
bMat = np.ones((3,3))

c6 = np.hstack((a6,b6)) # Horizontal Stack (kesamping )
d6 = np.vstack((a6,b6)) # Vertikal stack (Kebawah-atas)

cMat = np.hstack((aMat,bMat))
dMat = np.vstack((aMat,bMat))

print(c6)
print('=========')
print(d6)
print('=========')
print(cMat)
print('=========')
print(dMat)
# Untuk perkalian matrix maka jumlah (ukuran) baris dan kolom harus sama






######### CARA ADVANCE MEMBUAT ARRAY #########
# membuat array dengan tipedata tertentu
a7 = np.array(([1,2,3],[4,5,6]), dtype = int)
print(a7)

# membuat array dengan menggunakan function
# pertama bikin fungsinya dahulu
def kuadrat(baris, kolom):
    return (kolom**2)

def jumlah(baris, kolom):
    return (kolom + baris)
# kedua substitusikan fungsi dengan format:
# var = np.formfunction(namaFungsi, (jumlahBaris,jumlahKolom), dtype = tipe)
b7 = np.fromfunction(kuadrat, (1,10), dtype = int)
c7 = np.fromfunction(kuadrat, (4,4), dtype = float)

print(b7)
print(c7)

# membuat array atau matrix dengan menggunakan iterable
# deklarasikan iterasinya
iterable = (x*x for x in range(5))
# format penulisan : var = np.formiter(varIter, dtype = tipe)
d7 = np.fromiter(iterable, dtype = int)

# membuat multiple array
# list  biasa
e7 = ([
    ("faqih", 100),
    ("daffa", 150),
    ("fauzan", 170)
    ])

print(e7)
# array
# pertama deklarasikan isi var array
e7 = ([
    ("faqih", 100),
    ("daffa", 150),
    ("fauzan", 170)
    ])
# kedua deklarasikan 
# format = var = [("namaYgDmksd","stringMax") , ("namaYgDmksd, tipe")]
dtipe = [("Nama","S255") , ("Tinggi", int)]
# maksud S255 = string max yang diambil sebanyak 255 kata / huruf
# kalau diganti S2 maka hanya 2 huruf saja yang diambil
f7 = np.array(e7, dtype = dtipe)
print(f7)
# indexing 
print(f7[0])






######### SORTING NUMPY ARRAY #########
## 1 dimensi
# pertama kita randomkan saja matriksnya dengan format:
# var = np.floor(np.random.randn(baris,kolom))
a8 = np.floor(np.random.randn(1,10)*10)
# np.floor = untuk membulatkan
# *10 = tiap bilangan dikalikan dengan 10

print(a8)

# mengetahui nilai max min
print("Nilai max dari matriks =", a8.max())
print("Nilai min dari matriks =", a8.min())
# mengetahui posisi / index max min
print("posisi max dari matriks =", a8.argmax())
print("posisi min dari matriks =", a8.argmin())


## 2 dimensi
b8 = np.floor(np.random.randn(2,2)*10)

print(b8)

print("Nilai max dari matriks =", b8.max())
print("Nilai min dari matriks =", b8.min())
print("posisi max dari matriks =", b8.argmax())
print("posisi min dari matriks =", b8.argmin())


## multiple array
# PENTING disini harus diawali dengan [] untuk formatnya
dtipe2 = [("Nama","S10"),("Tinggi",int)]
c8 = [
    ("baka",100),
    ("naka",120),
    ("jaka",110),
    ("maka",90)
]

d8 = np.array(c8, dtype = dtipe2)
print(d8)

# mengurutkan nilai dari terkecil ke terbesar
# format = np.sort(namaVar, order="yangMauDiurutkan")
print(np.sort(d8, order="Tinggi"))
print(np.sort(d8, order="Nama"))






######### PERKALIAN VEKTOR (DOT DAN CROSS) #########
# Aljabar linear
# jika diputar keatas maka z + dan sebaliknya
# rumus dot = a . b atau |a|.|b|.cos 0
# contoh dot
a9 = np.array([2,4])
b9 = np.array([1,4])
# dot
c9 = np.dot(a9,b9)
print(c9)

# rumus cross = ||a||.||b||.sin 0.c(vektor)
# contoh cross
d9 = np.array([3,2,1])
e9 = np.array([2,2,4])
# dot
f9 = np.cross(d9,e9) # maka hasil + karena a di cross ke b
g9 = np.cross(e9,d9) # maka hasil - karena b di cross ke a
print(f9)
print(g9)






######### INVERS DAN DETERMINAN #########
# untuk menyelesaikan persamaan linear
a10 = np.array([(1,-1),(1,1)])

print(a10)

# invers matriks
a10_inv = np.linalg.inv(a10)
print(a10_inv)

# determinan matriks
a10_det = np.linalg.det(a10)
a10_detInv = np.linalg.det(a10_inv)
print(a10_det)
print(a10_detInv)






######### SOLUSI PERSAMAAN LINEAR #########
A = np.array([(2,3),(1,2)])
B = np.array([(23),(14)]) 
# untuk B bisa ditulis np.array([23,14])

print(A)
print(B)
A_inv = np.linalg.inv(A)
print(A_inv)

# menyelesaikan persamaan linear
X1 = np.dot(A_inv,B)
print(X1)

# atau cara lain
X2 = np.linalg.solve(A,B)
print(X2)






######### PLOT DATA DENGAN MATPLOTLIB #########
import matplotlib.pyplot as plt 

# persamaan garis
# y = 2x + 5

x = np.arange(0,11,1)
y = 2*x + 5

print(x)
print(y)

plt.figure(1)
# figure berfungsi utk urutan yg ingin ditampilkan shg tdk usah langsung di show
plt.plot(x,y)
# plot berfungsi untuk membuat grafiknya

# lingkaran
jari2 = 7
sudut = np.linspace(0,2*np.pi,100)
x2 = jari2*np.cos(sudut)
y2 = jari2*np.sin(sudut)

plt.figure(2)
plt.plot(x2,y2)
plt.show()
# show untuk menampilkan output
