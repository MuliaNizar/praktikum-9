# Deklarasi array umtuk menyimpan angka ganjil dan genap
ganjil = []
genap = []

# Meminta input pengguna
for i in range(10):
    angka = int(input(f"Masukan angka ke-{i+1}: "))
    
    # Memisahkan angka ganjil dan genap
    if angka % 2 == 0:
        genap.append(angka)
    else:
        ganjil.append(angka)
        
# Menampilkan Hasil
print(f"Angka genap: {genap}")
print(f"angka ganjil: {ganjil}")