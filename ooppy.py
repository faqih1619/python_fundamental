######### CONSTRUCTOR INIT #########
# => dijalankan ketika objek dibuat
class Hero0:

    def __init__(self, inputNama, inputNyawa, inputKekuatan, inputArmor):
        # instance variable (nempel di objek)
        self.nama = inputNama
        self.nyawa = inputNyawa
        self.kekuatan = inputKekuatan
        self.armor = inputArmor
# init dijalankan ketika objek dibuat seperti ini (contoh)
hero1 = Hero0("johnson", 1000, 200, 900)
hero2 = Hero0("lancelot", 500, 1000, 200)
hero3 = Hero0("cyclops", 600, 200, 300)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)






######### CLASS AND INSTANCE VARIABEL #########
######### CONSTRUCTOR INIT #########
# => dijalankan ketika objek dibuat
class Hero1:
    # class variabel (nempel di class)
    jumlah = 0

    def __init__(self, inputNama, inputNyawa, inputKekuatan, inputArmor):
        # instance variable (nempel di objek)
        self.nama = inputNama
        self.nyawa = inputNyawa
        self.kekuatan = inputKekuatan
        self.armor = inputArmor
        Hero1.jumlah += 1
        print("Membuat hero dengan nama",inputNama)
        
# init dijalankan ketika objek dibuat seperti ini (contoh)
hero1 = Hero1("johnson", 1000, 200, 900)
print("Jumlah hero yang dibuat sekarang =",Hero1.jumlah)
hero2 = Hero1("lancelot", 500, 1000, 200)
print("Jumlah hero yang dibuat sekarang =",Hero1.jumlah)
hero3 = Hero1("cyclops", 600, 200, 300)
print("Jumlah hero yang dibuat sekarang =",Hero1.jumlah)






######### METHODS (HAMPIR SAMA DG FUNCTION) #########
class Hero2:
    def __init__(self, inputNama, inputNyawa, inputPower):
        self.nama = inputNama
        self.nyawa = inputNyawa
        self.power = inputPower
    # method ( ada 3 macam )
    # tanpa return dan argumen
    def siapa(self):
        print("Nama heronya =",self.nama)
    # tanpa return dengan argumen
    def getHealth(self, up):
        self.nyawa += up
    # dengan return tanpa argumen
    def healthUp(self):
        return self.nyawa

hero1 = Hero2("johnson", 1000, 200)
hero2 = Hero2("lancelot", 500, 1000)

hero1.siapa()
hero1.getHealth(30)
# karena sudah ditambahkan nyawanya di method getHealth maka nyawa akan nambah
print(hero1.healthUp())






######### LATIHAN OOP SEDERHANA #########
# 1 = mendeklarasikan class
class Hero3:
    # menginisialisasi (__init__)
    def __init__(self,nama,nyawa,power,armor):
        self.nama = nama
        self.nyawa = nyawa
        self.power = power
        self.armor = armor

    # method serang (menyerang)
    def serang(self, lawan):
        print(self.nama,'menyerang',lawan.nama)
        lawan.diserang(self, self.power)

    # method diserang
    def diserang(self, lawan, power_lawan):
        print(self.nama,'diserang',lawan.nama)
        damage_diterima = power_lawan/self.armor
        print('Serangan diterima :',damage_diterima)
        self.nyawa -= damage_diterima
        print('Darah',self.nama,'tersisa :',self.nyawa)

# membuat objek 
tank = Hero3("Tank",1000,200,500)
assasin = Hero3("Assasin",500,800,200)

# menjalankan program
tank.serang(assasin)
print('\n')
assasin.serang(tank)






######### LATIHAN OOP TKINTER #########
import tkinter
# membuat layar / seperti instance
main_window = tkinter.Tk()
# membuat objek
label1 = tkinter.Label(main_window, text = "label 1")
label2 = tkinter.Label(main_window, text = "label 2")
tombol1 = tkinter.Button(main_window, text = "tombol 1")
tombol2 = tkinter.Button(main_window, text = "tombol 2")
# positioning 
label1.pack()
tombol1.pack()
label2.pack()
tombol2.pack()
# menampilkan GUI ke layar
main_window.mainloop()






######### PRIVATE VARIABEL ########
# untuk membatasi akses
class Hero4:
    # class variabel
    jumlah = 0
    # private variabel
    __privateJumlah = 10

    def __init__(self,name,health):
        self.name = name
        self.health = health
        # variabel instance private
        self.__private = "private"
        # variavel instance protected
        # var protected sama dengan public variabel
        # hanya berlaku di dalam class, dan jangan dirubah (seperti tanda)
        self._protected = "protected"

alok = Hero4("Alok",1000)

print(alok.__dict__)
# print(alok.__private) => akan error karena private variabel
print(alok._protected)
alok._protected = "terproteksi"
print(alok._protected)
print(alok.__dict__)
alok.__private = "terprivasi"
# maka ini tidak mengoverride var private tetapi membikin var baru dg nama __private
print(alok.__dict__)






######### ENCAPSULASI ########
# => Merubah variabel private,Memudahkan maintain bug
# Mengefisiensi kode program
# getter = mengambil variabel, setter = mensetting (mengubah) variabel private
class Hero5:
    def __init__(self,name,health,power):
        self.__name = name
        self.__health  = health
        self.__power = power

    # getter = mengambil variabel private
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter = mengubah/menyetting variabel
    def diserang(self,seranganPower):
        self.__health -= seranganPower # maka var private health bisa berubah

# awal program
muaythai = Hero5("muay thai",500,100)

# game berjalan
print(muaythai.getName()) # var private bisa diakses
print(muaythai.getHealth()) # var private bisa diakses
muaythai.diserang(30) 
print(muaythai.getHealth()) # var private bisa diakses






######### STATIC AND CLASS METHOD #########
class Hero6:
    # private class variabel
    __jumlah = 0

    def __init__(self,name):
        self.__name = name
        Hero6.__jumlah += 1

    # method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero6.__jumlah

    # method ini hanya berlaku untuk class 
    def getJumlah1(self):
        return Hero6.__jumlah

    # method static(decorator) nempel ke objek dan class
    # tetapi kurang efisien saat mengganti nama class
    @staticmethod
    def getJumlah2():
        return Hero6.__jumlah

    @classmethod # sangat efisien karena tidak dipengaruhi perubahan nama class
    def getJumlah3(cls): # nama argumen bebas
        return cls.__jumlah

faqih = Hero6("faqih")
print(Hero6.getJumlah2())
daffa = Hero6("daffa")
print(daffa.getJumlah2())
fauzan = Hero6("fauzan")
print(Hero6.getJumlah3())





######### GETTER AND SETTER #########
class Hero7:
    def __init__(self,name,health,armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    @property # constructor @property = merubah sebuah method menjadi seperti variabel
    def info(self):
        return "name {} : \n\thealth: {}".format(self.name,self.__health)

    @property
    def armor(self):
        pass # pass karena nanti ini untuk mengubah method menjadi variabel

    @armor.getter # getter = mendapatkan variabel private
    def armor(self):
        return self.__armor

    @armor.setter # setter = mengubah variabel private
    def armor(self,input):
        self.__armor = input # nantinya armor akan berubah sesuai input

rizaldi = Hero7("Rizaldi",1000,200)

print("Merubah Info")
print(rizaldi.info)
rizaldi.name = "Ruzuldun" # disini berlaku seperti variabel karena property
print(rizaldi.info)

print("Getter dan Setter untuk __armor")
print(rizaldi.armor)
rizaldi.armor = 50 # disini berlaku seperti variabel karena property dan 
# tidak usah mengedit seperti method namaVar(edit) karena pemberlakuan sifat variabel
print(rizaldi.armor)






######### LATIHAN ENCAPSULASI #########
class Hero8:
    __jumlah = 0
    
    def __init__(self,name,health,power,armor):
        self.__name = name
        self.__healthAwal = health
        self.__powerAwal = power
        self.__armorAwal = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthAwal * self.__level
        self.__power = self.__powerAwal * self.__level
        self.__armor = self.__armorAwal * self.__level
        self.__health = self.__healthMax

        Hero8.__jumlah = 0

    @property
    def info(self):
        return "{} level : {} \n\thealth : {}/{} \n\tpower : {} \n\tarmor : {}".format(
            self.__name,self.__level,self.__health,self.__healthMax,self.__power,
            self.__armor
        )

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name,"Level Naik")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthAwal * self.__level
            self.power = self.__powerAwal * self.__level
            self.__armor = self.__armorAwal * self.__level
            self.health = self.__healthMax

    def attack(self,gainExp):
        self.gainExp = 50

Manuk = Hero8("Manuk",1000,200,300)
Dadali = Hero8("Dadali",800,350,400)

print(Manuk.info)
Manuk.attack(Dadali)
Manuk.attack(Dadali)
Manuk.attack(Dadali)
Manuk.attack(Dadali)
print(Manuk.info)






######### INTRO INHERITANCE #########
# => pewarisan sifat dari superclass (parent) ke subclass (children)
class Hero9:
    def __init__(self,name,health):
        self.name = name
        self.health = health

class Hero99(Hero9):
    pass

class Hero999(Hero9):
    pass

nunuk = Hero9("Nunuk",1000)
ninik = Hero99("Ninik",500)
nanak = Hero999("Nanak",800)

print(nunuk.name)
# print(help(ninik)) => untuk mengecek ini warisan darimana
print(ninik.name)
print(nanak.name)






######### SUPER (INHERITANCE) #########
# dengan menggunakan syntax = super(). 
class Hero10:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} mempunyai health : {}".format(self.name,self.health))

class Hero100(Hero10):
    def __init__(self,name): # membuat init 
        super().__init__(name,100) # health langsung ditulis karena sudah mengambil dari parent
        super().showInfo()

class Hero1000(Hero10):
    def __init__(self,name):
        super().__init__(name,200) # health langsung ditulis karena sudah mengambil dari parent
        super().showInfo()

mamang = Hero100("Mamang") # Health tidak ditulis karena sudah terdefinisi di class Hero100
babang = Hero1000("Babang") # Health tidak ditulis karena sudah terdefinisi di class Hero1000






######### OVERRIDE METHOD #########
# => Menimpa class / method yang sama
class Hero11:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfoo(self):
        print("showInfo di class Hero11 (parent)")
        print("{} health : {}".format(self.name,self.health))

class Hero111(Hero11):
    def __init__(self,name):
        super().__init__(name,100)

    # OVERRIDING IN HERE ^-^
    def showInfoo(self):
        print("showInfo di subclass Hero111 (child)")
        print("{} \n\ttipe : intelligent \n\thealth : {}".format(
            self.name,
            self.health)
        )

class Hero1111(Hero11):
    def __init__(self,name):
        super().__init__(name,300)

lala = Hero111("Lala")
lulu = Hero1111("Lulu")

lala.showInfoo()
lulu.showInfoo()






######### LATIHAN INHERITANCE #########
class Hero:
    def __init__(self,name):
        self.health_pool = [0,100,200,300,400,500]
        self.power_pool = [0,10,20,30,40,50]
        self.armor_pool = [0,1,2,3,4,5]
        self.__name = name
        self.__exp = 0
        self.__level = 0

    def show_info(self):
        print("{} \n\tlevel: {}\n\thealth: {}\n\tpower: {}\n\tarmor: {}".format(
                self.__name,
                self.__level,
                self.__health,
                self.__power,
                self.__armor
            )
        )

    @property
    def health_pool(self):
        pass

    @property
    def power_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def levelUp(self):
        pass

    @property
    def gainExp(self):
        pass

    @health_pool.setter
    def health_pool(self,input):
        self.__health_pool = input

    @power_pool.setter
    def power_pool(self,input):
        self.__power_pool = input

    @armor_pool.setter
    def armor_pool(self,input):
        self.__armor_pool = input

    @gainExp.setter
    def gainExp(self,input):
        self.__exp += input
        if(self.__exp >= 100):
            self.levelUp = self.__exp//100
            self.__exp %= 100

    @levelUp.setter
    def levelUp(self,input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__power = self.__power_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]

class HeroIntelligent(Hero):
    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,50,100,150,200,250]
        self.power_pool = [0,20,40,60,80,100]
        self.armor_pool = [0,0.5,1,1.5,2,2.5]
        self.levelUp = 1

class HeroStrength(Hero):
    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,200,300,400,500,600]
        self.power_pool = [0,20,40,60,80,100]
        self.armor_pool = [0,2,4,6,8,10]
        self.levelUp = 1

lesles = HeroIntelligent("Lesles")
luslus = HeroStrength("Luslus")
lesles.show_info()
luslus.show_info()






######### MULTIPLE INHERITANCE #########
# Suatu class yang bisa mendapatkan inheritance dari banyak class
# pewarisan banyak class
# contoh sederhana:
class A:

    def method_A(self):
        print("Ini method A")

class B:

    def method_B(self):
        print("Ini method B")

class C(A,B): # Multiple inheritance here
    pass

objek = C()

objek.method_A()
objek.method_B()
# contoh 2:
class Team:
    def setTeam(self,team):
        self.team = team
    
    def showTeam(self):
        print(self.team)

class Tipe:
    def setTipe(self,tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)

class Player(Team,Tipe):
    def  __init__(self,name,health):
        self.name = name
        self.health = health

Bagong = Player("Bagong",1000)

Bagong.setTeam("Juventus")
Bagong.setTipe("Kiper")

Bagong.showTeam()
Bagong.showTipe()






######### METHOD RESOUTION ORDER #########
class A1:
    def show(self):
        print("Now in A1")

class A2:
    def show(self):
        print("Now in A2")

class A3(A1,A2): # jika A2 pertama maka output menjadi Now in A2
    pass

ubun = A3()
ubun.show() 
# Maka akan menampilkan output Now in A, mengapa demikian?
# karena tergantung urutan class nya yang diwariskan
"""
    tetapi jika class A3 juga terdapat method show maka yang dijalankan yang 
    ada di class A3
"""






######### DIAMOND PROBLEM #########
class B1:
    def showPro(self):
        print("Sekarang ada di class pertama")

class B2(B1):
    def showPro(self):
        print("Sekarang ada di class kedua")

class B3(B1):
    def showPro(self):
        print("Sekarang ada di class ketiga")

class B4(B2,B3):
    pass

atul = B4()
atul.showPro() # maka output Sekarang ada di class kedua
# urutannya : B4,B2,B3,B1
# jika di B4 tidak ada maka akan ke B2(sesuai urutan inherit), dst






######### MAGIC METHOD #########
# => adalah keyword method yang sudah ada di pythonnya
class Buah:
    # magic method
    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah
    # __repr__ hampir sama seperti __init__ tetapi langsung diprint
    def __repr__(self):
        return "Mangga: {} berjumlah: {}".format(self.nama,self.jumlah)
    # __str__ hampir sama seperti __repr__ biasanya digunakan ketika program sdh jadi
    def __str__(self):
        return "Mangga: {} berjumlah: {}".format(self.nama,self.jumlah)
    # __add__ digunakan untuk operasi aritmatika
    def __add__(self,buah):
        return self.jumlah + buah.jumlah
    
    @property
    def __dict__(self):
        return "Objek ini mempunyai nama dan jumlah"

Buah1 = Buah("Mangga",10)
Buah2 = Buah("Apel",20)
print(Buah1)
print(Buah2)
print(Buah1 + Buah2)
print(Buah1.__dict__)






######### CLASS ABSTRACT #########
# Super super class ^_^
# untuk memaksa melakukan suatu program walaupun di super class di pass
# abc = abstract base class
from abc import ABC,abstractmethod

class Tombol(ABC):
    @abstractmethod
    def click(self):
        pass # maka akan tetap berjalan walaupun pass 

class PushButton(Tombol):
    def click(self):
        print("Push Button Click")

class RadioButton(Tombol):
    def click(self):
        print("Radio Button Click")

Tombol1 = PushButton()
Tombol2 = RadioButton()
 
Tombol1.click() # maka method pushbutton tetap berjalan walau class Tombol pass 
Tombol2.click() # maka method radiobutton tetap berjalan walau class Tombol pass 






######### CLASS ABSTRACT DAN DECORATOR #########
from abc import ABC,abstractmethod

class button(ABC):
    def __init__(self,set_link):
        self.link = set_link

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass

class Pushbutton(button):
    def click(self):
        print("Go To: {}".format(self.link))

    @button.link.setter
    def link(self,input):
        self.__link = input

    @link.getter
    def link(self):
        return self.__link

tombol = Pushbutton("www.google.com")
tombol.click()

#=================== E N D ===================#
