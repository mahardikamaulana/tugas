#Nomor 1a
print (""">>>* ANGKA GANJIL *<<<
    --------------""")

angka = int(input("Inputkan angka anda = "))
if angka %2 == 1:
    print (("Angka"),angka,("adalah angka ganjil"))

#Nomer 1b
print (""">>>* ANGKA GENAP *<<<
    --------------""")
angka = int(input("Inputkan Angka anda = "))
if angka %2 == 0:
    print (("Angka"),angka,("adalah angka genap"))

#nomer 2
print (""">>>* SPEED LIMIT *<<<
    ===============""")

kecepatan = int(input("Speed : "))
if kecepatan > 70:
    print("License Supended")
else:
    print("Ok")

#Nomer 3
print ("---- CEK BIlANGAN ----")

x = int(input("Masukkan bilangan : "))
if x > 47:
    print ("bilangan lebih dari 47")
elif x < 47:
    print ("bilangan kurang dari 47")
else:
    print ("bilangan sama dengan 47")

#Nomer 4
print ("---- Cek Kelulusan Mata kuliah Kalkulus ----")

nilai = int(input("input nilai : "))
kehadiran = int(input("input persentasi kehadiran : "))
if kehadiran >= 75:
    if 81 <= nilai <= 100:
        print ("""Selamat Anda lulus
        Indeks A""")
    elif 71 <= nilai <= 80:
        print ("""Selamat Anda lulus
        Indeks B""")
    elif 61 <= nilai <= 70:
        print ("""Selamat Anda lulus
        Indeks C""")
    elif 51 <= nilai <= 60:
        print ("""Selamat Anda lulus
        Indeks D""")
    elif 41 <= nilai <= 50:
        print ("""Selamat Anda lulus
        Indeks E""")
    else:
        print ("Tidak lulus")
else:
    print ("Maaf Anda mengulang")