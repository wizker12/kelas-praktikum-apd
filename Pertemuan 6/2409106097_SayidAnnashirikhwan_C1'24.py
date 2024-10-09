# # daftar_buku = {
# # "Buku1" : "Harry Potter",
# # "Buku2" : "Percy Jackson",
# # "Buku3" : "Twillight"
# # }
# # print(daftar_buku["Buku1"])
# # print(daftar_buku["Buku2"])
# # print(daftar_buku[True])
# # print(daftar_buku)


#  Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#     }
# }

# print(Biodata["KRS"][0])
# print(Biodata["Sosial Media"][Email])

# games = dict(sekiro = "Action", Pokemon = "Adventure",
#              Valorant = "FPS"
# # print(games["Pokemon"])
# Valorant = {"nama" : {123 : "informatika"}} )
# print(games[valorant])


# Games = {
#     "Game1" : "PUBG MOBILE",
#     "Game2" : "Mobile Legend",
#     "Game3" : {
#         "Nama" : "coc",
#         "genre" : "strategy"
#     }
# }

# print((Games.get('Game3')).get('genre'))





# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }


# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# #tanpa menggunakan items
# for i in Nilai:
#     print(i)
# print("")
# # menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")



# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }

#Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller", "Rush Hours : "Comedy" })

# #Setelah Ditambah
# print(Film)


# Film["Zombieland"] = "Comedy"
# Film.update 


# simpan = Film.pop('Hours')
# # Film.clear()
# print(Film)
# print(simpan)

# Buku = {
# "No Longer Human" : "Osamu Dazai",
# "Harry Potter" : "J.K. Rowlings",
# "Hamlet" : "William Shakespeare"
# }
# pinjam = Buku.copy()
# print("Dictionary yang Telah Disalin : ", pinjam)


# #menggunakan keys
# for i in Nilai.keys():
#     print(i)

# print("")
# #menggunakan value
# for i in Nilai.values():
#     print(i)

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")

# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")

# #setelah menggunakan setdefault
# print(Nilai)



# Musik = {
#     "The Chainsmoker" : ["All we Know", "TheParis"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
# print("")


# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
#     print("")


# Nilai = {
#     "Matematika" : 90,
#     "Biologi" : 80,
#     "Kimia" : 70,
#     "Fisika" : 80
# }

# total = 0
# for i in Nilai.values():
#     total += i


# print (total)
# print (total/4)

