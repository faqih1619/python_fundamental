import numpy as np
import matplotlib.pyplot as plt

######### MATPLOTLIB(INTRO) #########






######### MATPLOTLIB INSTALASI #########
# => di terminal ketik pip install matplotlib
# panggil di code editor dengan = import matplotlib.pyplot as plt
# contoh sederhana:
"""
    x = [1,2,3,4,5]
    y = [6,7,8,9,10]

    # menginisialisasi 
    plt.plot(x,y)
    # menampilkan output
    plt.show()

    # contoh membuat lingkaran
    pi = np.pi
    sudut = np.linspace(0,2*pi,100)
    jari_jari = 7

    x1 = jari_jari * np.cos(sudut)
    y1 = jari_jari * np.sin(sudut)

    plt.plot(x1,y1)
    plt.show()
"""






######### PENDAHULUAN PYPLOT #########
# step-stepnya:
"""
    1. Membuat data
    2. Membuat / menginisialisasi plot
    3. Menampilkan data
"""
# contoh:
# 1. Membuat data
a = np.array([1,2,3,4,5])
b = np.array([1,4,9,16,25])
c = np.array([1,16,81,256,625])

# 2. Membuat plot / menginisialisasinya
plt.plot(a,b)
plt.plot(a,c)

# 3. Menampilkan data
plt.show()






######### SET WARNA DAN MARKER #########
# membuat sinusgenerator
# 1. Membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t,y

# 2. Membuat plot
t1,y1 = sinusGenerator(1,1,4,0)
plt.plot(t1,y1)

t2,y2 = sinusGenerator(1,1,4,30)
plt.plot(t2,y2, "y")
# "y" = warna yellow

t3,y3 = sinusGenerator(1,1,4,60)
plt.plot(t3,y3, "b--")
# "b--" warna biru dengan marker -

t4,y4 = sinusGenerator(1,1,4,90)
plt.plot(t4,y4, "g-o")
# "g-o" warna hijau dengan marker o

# 3. Menampilkan plot
plt.show()






######### SET PROPERTIES #########
# => untuk mengedit plot dengan cara lebih efisien
# Membuat data
def sinusGenerator2(amplitudo,frekuensi,tAkhir,theta):
    a2 = np.arange(0,tAkhir,0.1)
    b2 = amplitudo * np.sin(2*frekuensi*a2 + np.deg2rad(theta))
    return a2,b2

k,l = sinusGenerator(1,1,4,0)
k1,l1 = sinusGenerator(1,1,4,60)
k2,l2 = sinusGenerator(1,1,4,90)

# Membuat plot
dPlot = plt.plot(k,l)
dPlot1 = plt.plot(k1,l1)
dPlot2 = plt.plot(k2,l2)

# Set properties
plt.setp(dPlot,color="r", linestyle="-", linewidth="0.75")
plt.setp(dPlot1,color="y", linestyle="--", linewidth="3.25")
plt.setp(dPlot2,color="g", linestyle="-.", linewidth="5")

# Menampilkan plot
plt.show()






######### SET AXIS #########
# => untuk mengatur batas max min garis x dan y
# Membuat data
def sinusGenerator3(amplitudo,frekuensi,tAkhir,theta):
    a3 = np.arange(0,tAkhir,0.1)
    b3 = amplitudo * np.sin(2*frekuensi*a3 + np.deg2rad(theta))
    return a3,b3

o,p = sinusGenerator(1,1,4,30)

# Membuat plot
dPlt = plt.plot(o,p)

# set axis format = plt.axis([x-min,x-max,y-min,y-max])
plt.axis([-1,5,-5,5])

# Menampilkan plot
plt.show()






######### SET LABEL DAN TITLE #########
# Membuat data
def sinusGenerator4(amplitudo,frekuensi,tAkhir,theta):
    a4 = np.arange(0,tAkhir,0.1)
    b4 = amplitudo * np.sin(2*frekuensi*a4 + np.deg2rad(theta))
    return a4,b4

amplitudo = 1
frekuensi = 1
theta = 0
tAkhir = 4

m,n = sinusGenerator4(amplitudo,frekuensi,tAkhir,theta)

# Membuat plot
judul = "Grafik Sinusoidal\n"
# r'' => regular expression
rumus = r"$ \mathcal{y} = A.sin() \omega t + \theta $" + '\n'
param1 = r"$ A = $" + str(amplitudo) + "cm, "
param2 = r"$ \omega = $" + str(frekuensi) + r"$ \mathit{Hz} $" + ", "
param3 = r"$ \theta = $" + str(theta) + r"$ ^{o} $"
# untuk menampilkan simbol2 maka formatnya harus r"$\simbol$
plt.plot(m,n)

# Membuat judul (harus ada dibawah plt.plot() pas)
plt.title(judul + rumus + param1 + param2 + param3)
# Membuat label sumbu x dan y
plt.xlabel("waktu(detik")
plt.ylabel("magnituda(cm")

# Menampilkan plot
plt.show()






import numpy as np
import matplotlib.pyplot as plt

######### MEMBUAT LEGEND #########
# Membuat data
def sinusGenerator5(amplitudo,frekuensi,tAkhir,theta):
    a5 = np.arange(0,tAkhir,0.1)
    b5 = amplitudo * np.sin(2*frekuensi*a5 + np.deg2rad(theta))
    return a5,b5

r,s = sinusGenerator5(1,1,4,0)
r1,s1 = sinusGenerator5(1,1,4,90)

# Membuat plot
# tipe pertama
#plt.plot(r,s, label="sin(0)")
#plt.plot(r1,s1, label="sin(90)")

#plt.legend()
# plt.legend() berfungsi untuk menamapilkan legenda seperti pada peta

# tipe kedua
#plt.plot(r,s, label="sin(0)")
#plt.plot(r1,s1, label="sin(90)")

#plt.legend(loc="upper center ")
#loc="" berfungsi untuk menaruh posisi legenda ( atas tengah,kiri bawah,dll)

# tipe ketiga
#plt.plot(r,s, label="sin(0)")
#plt.plot(r1,s1, label="sin(90)")

#plt.legend(loc="upper center ", bbox_to_anchor(0.5,-0.05))
#bbox_to_anchor(x,y) berfungsi untuk menggeser/mengubah field wilayah grafik 

# tipe keempat
plt.figure(1) # figure = container
ax = plt.subplot(111) 
# subplot = berfungsi untuk mengatur plot fieldnya
plt.plot(r,s, label="sin(0)")
plt.plot(r1,s1, label="sin(90)")
box = ax.get_position() # untuk mengambil posisinya biar bisa dirubah
# pertama get kedua set
ax.set_position([box.x0, box.y0, box.width*0.7, box.height])
plt.legend(loc='upper center', bbox_to_anchor=(1.2,1))

# Menampilkan plot
plt.show()






######### MENAMBAH TEXT #########
# Membuat Data
def sinusGenerator6(amplitudo,frekuensi,tAkhir,theta):
    a6 = np.arange(0,tAkhir,0.1)
    b6 = amplitudo * np.sin(2*frekuensi*a6 + np.deg2rad(theta))
    return a6,b6

q,w = sinusGenerator6(1,1,4,0)

# Membuat Plot
plt.plot(q,w)

# Menambah Text
# format = plt.text(sbX,sbY, "text")
plt.text(2,0.5, r'$ y = \mathcal{A}.sin(2 \omega t) $')
plt.text(2,0.4, r'$ \mathcal{A} = 1 cm, \omega = 1 Hz $')

# Menampilkan plot
plt.show()






######### SET TICKS (MERUBAH RENTANG) #########
# Membuat data
sudutt = np.arange(0,360,1)
yy = np.sin(np.deg2rad(sudutt))

# Membuat plot
plt.plot(sudutt,yy)
plt.ylabel("magnituda")
plt.xlabel("sudut")

plt.yticks([-1,0,1])
# yticks berfungsi untuk mengatur nilai di sb Y yang ingin ditampilkan saja
plt.xticks([0,90,180,270,360],
           [r"${0}^o$",r"${90}^o$",r"${180}^o$",r"${270}^o$",r"${360}^o$"])
# di yticks ada 2 parameter karena param-2 berfungsi untuk mengganti nilai param-1

# Menampilkan plot
plt.show()






######### SET SPINES(MENGGESER AXIS) #########
# Membuat data
sudutt2 = np.arange(0,360,1)
yy2 = np.sin(np.deg2rad(sudutt2))

# Membuat plot
plt.plot(sudutt2,yy2)
plt.title("Grafik Sinosidal")
plt.text(190,1,"magnituda")
plt.text(360,0.1,"sudut")
plt.yticks([-1,0.5,0,0.5,1])
plt.xticks([0,90,180,270,360],
           [r"${0}^o$",r"${90}^o$",r"${180}^o$",r"${270}^o$",r"${360}^o$"])

# set spines
# pertama deklarasikan var berfungsi gca()
ax = plt.gca() # gca() => getCureentAxis

# lalu set spines dengan format:
# varDeklar.spines['posisi'].fungsi_yang_dipilih
# jika pilih fungsi .set_position maka format wajib seperti dibawah ini
# nama "data" wajib karena sudah aturan dari fungsinya
ax.spines['left'].set_position(('data',180))
ax.spines['bottom'].set_position(('data',0))
# set_color('none') agar tidak ditampilkan batas plot kanan dan atas
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Menampilkan plot
plt.show()
