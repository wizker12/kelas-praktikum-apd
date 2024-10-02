nama = ["shandy" , 106, True ,3.96]
matkul = ["APD",
          "APL" , 
          "WEB" , 
          "JARKOM" , 
          "BASDAT", 
          "STRUKDAT", 
          "PTI", 
          "KALKULUS" , 
          "PROBAS"]

print(matkul[6])


nama = ["shandy", 106,True,]

nama_mhs = [ "Celio”, “Afrizal”, “Farrel”, “Ghazali”]
            

            nama = ["shandy" ,106,True
                    ["yuyun" , 145] ,3.96, [123, "ALVITTO"]


MAKANAN = ["Bakso", "sate", "soto"]
print("sebelum: ")
print(MAKANAN)
# MAKANAN.append ("Nasi Goreng")
print("sesudah: ")
# Print (MAKANAN)
MAKANAN.insert(2, "Nasi Goreng")
print(MAKANAN)
MAKANAN[1] = ["ayam","bebek"]
print(MAKANAN)


makanan = ["bakso","sate","soto","nasi goreng","mie ayam","ayam bakar","cumi goreng"]
print("sebelum: ")
print(makanan)
# makanan.append("nasi goreng")
print("sesudah: ")
data = makanan.pop(5)
print(makanan)
print(data)


minuman = ["susu", "jus mangga","jus sirsak","es teler ","es teh","es buah"]
print("sebelum")
print(minuman)
del minuman[2]
print("sesudah")
print (minuman)
minuman[4] = "air putih"
print(minuman)
minuman.insert(0,"jus tomat")
print(minuman) 


makanan = ["bakso", "soto","sate","ikan", "bebek"], ["teh", "kopi","air"]

for i in makanan :
    print (i, end=" ")




makanan = [["bakso", "soto","sate","ikan", "bebek"], ["teh", "kopi","air"]]

for i in i :
    if isinstance(i, list):
        for j in i : 
            print(j)
        else:
            print(i)


akuns = []

while True: 
    print("Halo! selamat datang di aplikasi catatan")
    print("Silahkan pilih 'daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan login")
    print("1. Daftar akun")
    print("2. login")
    print("3. Exit")
    print("---------------------")
    opsi = input("pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("halo pengguna baru! ayo buat akun dulu")
        Username = input("Username: ")
        akuna = False 
        for akun in akuns:
            if akun[0] == Username: #Memeriksa apakah username sudah ada
                akuna = True
                break
        if akuna:
            print("Nama sudah terpakai untuk registrasi silahkan coba lagi")
        else:
            Password = input("Password: ")
            akuns.append([Username, Password, []]) #Simpan username, password dan catatan ( sebagai list kosong)
            print(f"akun anda berhasil terdaftar dengan ID: {Username}")

