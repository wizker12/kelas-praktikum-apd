cuaca = "mendung"

if cuaca == "mendung":
    print("hari ini mendung")
else:
    print("hari ini mendung")

umur = int(input("Masukan umur anda : "))
if umur > 0:
    if umur <= 10:
        print( " umur anda termasuk kategori anak-anak")
    elif umur <= 18:
        print("umur anda termasuk kategori remaja")
    elif umur <=35:
        print("umur anda termasuk kategori dewasa")
    elif umur <=65:
        print('umur anda termasuk kategori paruh baya')
    else:
        print("umur anda termasuk kategori tua")
else:
    print("input usia harus bilangan positif")

nim = int(input("masukkan nim: "))

if nim >= 1 and nim <= 50 :  
    if nim >= 1 and nim <= 25 :
        print("Kelas A'1")
    else :
        print("Kelas A'2")
elif nim >= 51 and nim <= 100 :
    if nim >= 51 and nim <= 75 :  
        print ("Kelas B'1")
    else :
        print("Kelas B'2")
elif nim >= 101 and nim <= 121 :
    if nim >= 101 and nim <= 110 :
        print("Kelas c'1")
    else : 
        print("Kelas C'2")
else :
    print("Anda bukan mahasiswa informatika 24")

nim = int(input("Masukkan nim: "))
hasil = "Kelas A" if nim >= 1 and nim <=50 else "Kelas B" if nim >= 51 and nim <= 100 else "Kelas C" if nim >= 1-1 and nim <= 121 else "mahasiswa siluman"
print(hasil)