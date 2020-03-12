# # #Nomor 1
# # hari = ("Senin", 'selasa', 'rabu', 'kamis', "Jum'at", 'sabtu', 'minggu')
# # harike = int(input('Hari ke? :'))
# # print('hari ke-', harike, 'adalah hari :', hari[harike - 1])

# # #Nomor 2
# # stok = []

# # for i in range(1, 6):
# #     buah = input('Masukkan Buah ke-'+str(i)+':')
# #     stok.append(buah)
# # print ('Stock buah:',stok)

# # #Nomor 3
# # stok = ['jeruk', 'apel', 'naga', 'mangga', 'pisang']
# # print ("Stok Buah: ", end="")
# # for buah in stok:
# #     print(buah, end=" ")
# # cari = (input('\nCari buah apa? :'))
# # if cari in stok:
# #     print ('Buah', cari, 'TERSEDIA')
# #     beli = (input('Mau Beli(y/n) :'))
# #     if beli == "y":
# #         stok.remove(cari)
# #         print('Buah', cari, 'terbeli')
# #         print('Stok Buah: ', end="")
# #         for setelahstok in stok:
# #             print (setelahstok, end=" ")
# #     else:
# #         print('Stok Buah: ', end="")
# #         for buah in stok:
# #             print(buah, end=" ")
# # else:
# #     print ('Buah', cari, 'TIDAK TERSEDIA')

#nomor 4
daftar_lab = {
    "DASPRO" : {
        'Praktikum' : 'Algoritma dan Pemrograman',
        'Semester' : 2
    },
    'ERP' : {
        'Praktikum' : 'SAP 01 Fundamental',
        'Semester' : 1
    }
}
for key, value in daftar_lab.items():
    print ("nama lab: ", key)
    for key2 in value:
        print (key2, ':', value[key2])

