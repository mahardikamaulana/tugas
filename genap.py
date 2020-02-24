# x = int(input("masukkan angka: "))

# #genap
# if x % 2 == 0:
#     print ("bilangan genap")
# else:
#     print ("bukan bilangan genap")

# #ganjil
# if x % 2 >= 0:
#     print ("bilangan ganjil")
# else:
#     print ("bukan bilangan ganjil")

#cek panjang kata ganjil genap
# kata = (input("masukkan kata"))
# panjangkata = len(kata)
# if panjangkata % 2 == 0:
#     print ("panjang kata adalah genap")
# else:
#     print ("panjang kata adalah ganjil")

# a = int(input("input: "))

# if a % 2 == 0:
#     a //= 2
#     print (a)
# else:
#     a += 3
#     print(a)

a = int(input("a:")) #BACOT
b = int(input("b:"))
c = int(input("c:"))

# if a>b>c:
#     print(a)
# elif a>=c>b:
#     print (a)
# elif b>=a>c:
#     print(b)
# elif b>=c>a:
#     print (b)
# else:
#     print(c)

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > c:
    print(b)
else:
    print(c)