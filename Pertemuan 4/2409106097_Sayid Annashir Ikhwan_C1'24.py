simpan = [12, "udin petot", 14.5, True, 'A']
for i in simpan:
        print (i) 


makanan = ["mie", "sop","bakso"]
minuman = ["es teh,",]


print("menu rumah makan informatika 24: ")
print("------------------------------------")
simpan = ["nasi goreng", "mie goreng", "mie ayam", "bakso", "soto"]
for i, menu in enumerate(simpan,start=100):
    print(f"{i}.{menu}")

  

print("menu rumah makan informatika 24: ")
print("------------------------------------")  
simpan = ["nasi goreng", "mie goreng", "mie ayam", "bakso", "soto"]
for i in range(len(simpan)):    
    print(f"{i+1}. {simpan[i]}")



jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
print(f"Total perulangan: {hitung}")


hitung = 0
while True:
    hitung += 1
    ulang = input("Masih Ingin Mengulang? ")
    if ulang == "tidak" or ulang =="Tidak":
        break

print(f"Total Perulangan: {hitung}")




jawab = "ya"
hitung = 0
while(true):   
    hitung += 1
    jawab = input("balikan lagi tidak? ")
    if jawab == "ga" or jawab == "engga" :
        print(f"Total perulangan: {hitung}") 



hitung = 0
while(true):   
    hitung += 1
    ulang = input("masih ingin lanjut? ")
    if ulang == "y" or jawab == "y":
        print("oke kita lanjut")






print("Daftar bilangan ganjil dari 1-10")
for i in range(10):
    if i % 2 ==0:
        continue
    print(i)                       





Buatlah program yang dapat menentukan dan menghitung jumlah bilangan prima
dengan range bilangan mulai dari 1

print("Daftar bilangan prima dari 2-100")
for i in range(100):
    if i % 3 ==0:
        continue
    print(i)                       


def is_prima(n):
  "menentukan dan menghitung jumlah bilangan prima"
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

print("Bilangan prima  1-50:")
for i in range(1, 50):
  if is_prima(i):
    print(i, end=" ")