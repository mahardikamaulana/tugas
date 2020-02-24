# #Latihan 0
# for i in range(0, 100):
#     print ("saya tidak akan menceontek "+str(i+1))
# #Latihan 1
# masukan = ("*")
# count = ""
# while (masukan != '**********'):
#     count += "*"
#     masukan =(count)
#     print (count)
# masukan = ("**********")
# count = len(masukan)
# while (masukan != '*'):
#     count -= 1
#     masukan =(count)
#     print (count)

    
# #Latihan 2
# for i in range(1, 11):
#     for j in range(i):
#         print(j+1, end="")
#     print()
# #Latihan 3
for i in (range(10, -1, -1)):
    for j in range(0, i+1):
        print(j, end="")
    print()

#Latihan 3
y = 10
while (y > 0):
    x = 0
    while x < y:
        print (x, end="")
        x += 1
    print ()
    y -= 1