print ("""
==== HITUNG LUAS TANAH ====""")

panjang = int(input("Masukkan Panjang Tanah: "))
lebar = int(input("Masukkan Lebar Tanah: "))
luas = panjang * lebar
harga = 895000 * luas
totalsetelahdiskon = harga * 0.15
print("Luas Tanah =",luas, "/m2")
print ("Harga Tanah = Rp",totalsetelahdiskon)