def indeksnilai(nilai):
    totalnilai = int(input("test = "))

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
    return indeks

def kelulusan():
    if indeks == "A" or "B" or "C" or "D":
        statuskelulusan = ("LULUS")
    else:
        statuskelulusan = ("TIDAK LULUS")
    return statuskelulusan

print("test program")
print (indeksnilai("Mahardika"),kelulusan("Mahardika"))