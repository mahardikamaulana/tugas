# LATIHAN
# saldo = 50000
# tagihan = 10000

# if saldo >= tagihan :
#     print ((saldo - tagihan))
# else: 
#     print ("saldo Anda tidak mencukupi")

# LATIHAN 2
# a = (input("a = "))
# b = (input("b = "))
# c = (input("c = "))

# if a > b:
#     if a > c:
#         print (a)
#     else:
#         print (c)
# elif b > c:
#     print (b)
# else :
#     print (c)

# #LATIHAN 3
import getpass
USER = (input("Masukkan Username = "))
username = (getpass.getuser(USER))
password = (getpass.getpass())

if username == ("admin"):
    if password == ("admin"):
        print ("Login Berhasil")
    else:
        print ("login tidak berhasil")
else:
    print ("login tidak berhasil")