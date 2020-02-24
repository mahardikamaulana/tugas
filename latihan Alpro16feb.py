# Latihan 1
# x = int(input("input: "))  #Deklarasi variabel dan input

# if x % 3 == 0 and x % 4 == 0: #Pengkondisian kelipatan 3 dan 4
#     print ("Kelipatan 4 dan 3")
# elif x % 4 == 0: #pengkondisian kelipatan 4
#     print("Kelipatan 4")
# elif x % 3 == 0: #pengkondisian kelipatan 3
#     print ("Kelipatan 3")
# else: #pengkondisian selain kelipatan diatas
#     print("Bukan kelipatan 4 & 3 atau 4 atau 3")

# Latihan 2
nama = (input("Siapa Nama Anda: "))
umur = int(input("Berapa Umur anda: "))
tinggicm= int(input("Berapa Tinggi Badan Anda: ")) #Input Tinggi badan
tinggi = tinggicm / 100 #Konversi Centimeter ke Meter
berat= float(input("Berapa Berat Anda: ")) #Input Berat badan
gender = ""
BMI = berat / (tinggi * tinggi) #perhitungan berat badan ideal berdasarkan Body Mass Indeks (BMI)
beratidealW = (tinggicm - 100) - ((tinggicm - 100) * 0.15)
beratidealP = (tinggicm - 100) - ((tinggicm - 100) * 0.1)
ideal=''
while True: #Untuk menggunakan perulangan
    gender = int(input("""\
Apakah Anda
1. Pria
2. Wanita
Masukkan Angka: """)) #Input Gender untuk menentukan rumus yang digunakan
    if gender == 1: #Jika gender Pria (1)
        if 18.5 < BMI < 24.9: #Range Berat badan ideal dalam BMI
            # print ("Selamat Berat Badan kamu ideal!")
            ideal = 0
        elif berat > beratidealP: #Jika berat saat ini lebih dari berat ideal
            print("Berat badan kamu tidak ideal, Coba diet ya!")
            print ("ayo semangat kurangi makanan berlebih!")
            ideal = berat - beratidealP
        elif berat < beratidealP: #Jika berat saat ini kurang dari berat ideal
            print ("Berat kamu kurang ideal, ayo naikkan berat badan kamu ya!")
            ideal = beratidealP - berat
        break #Menghentikan Perulangan
    elif gender == 2: #Jika gender Wanita (2)
        if 18.5 < BMI < 24.9: #Range Berat badan ideal dalam BMI
            print ("Selamat Berat Badan kamu ideal!")
            ideal = 0
        elif berat > beratidealW: #Jika berat saat ini lebih dari berat ideal
            print("Berat badan kamu tidak ideal, Coba diet ya!")
            print ("ayo semangat kurangi makanan berlebih!")
            ideal = berat - beratidealW
        elif berat < beratidealW: #Jika berat saat ini kurang dari berat ideal
            print ("ayo naikkan berat badan kamu ya!")
            ideal = beratidealW - berat
        break
    else:
        print("Input anda Salah!")

print("""\
----- BIODATA -----""")
print("Nama        : ", nama)
print("Umur        : ", umur)
print("gender      : ", gender)
print("Tinggi      : ", tinggicm, "cm")
print("Berat       : ", berat, "kg")
if gender == 1:
    print("Berat Ideal : ", beratidealP, "kg")
elif gender == 2:
    print("Berat Ideal : ", beratidealW, "kg")
print("BMI         : ", BMI)