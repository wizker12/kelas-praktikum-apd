# def salam():
#     print(salam)

#     pilihan = 0

#     if pilihan == 1:
#         teks()
    
#     elif pilihan == 2:
#         teks()

#     elif pilihan == 3:
#         teks()

#     print (hasil)


# def penjumlahan():
#     hasil = 7+3
#     print (hasil)

# penjumlahan():

# a = int(input ("bilangan pertama: "))
# b = int(input ("bilangan kedua: "))
# c = int(input ("bilangan ketiga: "))

# def penjumlahan(a,b,c):
#     hasil = a+b+c
#     print(hasil)


# penjumlahan(3,6,8)

# def penjumlahan():
# a = int(input ("bilangan pertama: "))
# b = int(input ("bilangan kedua: "))
# c = int(input ("bilangan ketiga: "))



# def penjumlahan(a,b):
#     hasil = a*b
#     print(hasil)


# penjumlahan(5,3)

# def luas_persegi(sisi):
#     luas = sisi*sisi
#     print(f"luas persegi: {luas}")

# sisi = int(input("Sisi persegi"))

# luas_persegi(sisi)


# def volume_persegi(sisi):
#     volume = sisi*sisi*sisi
#     print(f"volume persegi: {volume}")

# sisi = int(input("volume persegi"))

# volume_persegi(sisi)

# def kali(a,b):
#     hasil = a*b
#     return hasil

# print (kali(5,5))x

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# # rumus: sisi x sisi x sisi
# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print ("Volume Persegi = ", volume)


# a = int(input("masukin nangka:"))

# def perjumlahan(a):
#     hasil = a+a
#     return hasil
# def perkalian(a):
#     kali = perjumlahan(a)*a
#     print("Hasilnya : ", kali)

# perkalian(a)


a= 1
b= 2

# def perjumlahan(a,b):
#     a= 5
#     b=4
#     hasil = a+b
#     print (hasil)

# perjumlahan(a,b)

def show_menu():
    print ("\n")
    print ("----------- MENU---------- ")
    print ("[1] Show Data")
    print ("[2] Insert Data")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Exit")
menu = input("PILIH MENU> ")
print ("\n")

if menu == "1":
    show_data()
elif menu == "2":
    insert_data()
elif menu == "3":
    edit_data()
elif menu == "4":
    delete_data()
elif menu == "5":
    exit()
else:
    print ("Salah pilih!")