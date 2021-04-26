
print ("Nama : Muhammad Farid Al Muiz")
print ("NIM : 04119005")
print ("Prodi : Sistem Komputer")
print ("Kampus : Universitas Narottama")
kalimat = input("Masukan Kalimat :")
file = kalimat.split()
jumlah=len(file)
for kata in kalimat.split():
    print(kata)
print("")
print(file)
print("jumlah kata yang dimasukkan", jumlah)
