print (">>> PENGHITUNG NILAI AKHIR <<<")
print("")
nama = (input("Masukkan Nama            = "))
nim = (input("Masukkan NIM             = "))
nilaikuis = int(input("Masukkan Nilai Kuis      = "))
nilaiuts = int(input("Masukkan Nilai UTS       = "))
nilaiuas = int(input("Masukkan Nilai UAS       = "))
nilaiprtkm = int(input("Masukkan Nilai Praktikum = "))
totalnilai = nilaikuis*0.15 + nilaiuts*0.30 + nilaiuas*0.30 + nilaiprtkm*0.25
if totalnilai > 80:
    indeks = ("A")
    status = ("LULUS")
elif 70 < totalnilai <= 80:
    indeks = ('AB')
    status = ("LULUS")
elif 65 < totalnilai <= 70:
    indeks = ('B')
    status = ("LULUS")
elif 60 < totalnilai <= 65:
    indeks = ('BC')
    status = ("LULUS")
elif 50 < totalnilai <= 60:
    indeks = ('C')
    status = ("LULUS")
elif 40 < totalnilai <= 50:
    indeks = ("D")
    status = ("LULUS")
else:
    indeks = ("E")
    status = ("TIDAK LULUS")

print("")
print("+++++* Nilai Kelulusan *+++++")
print ("Nama        :",nama)
print ("NIM         :",nim)
print ("Nilai Akhir :",totalnilai)
print ("Indeks      :",indeks)
print ("Status      :",status)