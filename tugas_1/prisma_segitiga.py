print("=========================PRISMA SEGITIGA==========================")

a = 21
t = 12
tinggi = 12
tinggi_alas = 20

kel_segitiga = 3 ** a

# luas
luas_sisi_prisma = kel_segitiga * tinggi
luas_permukaan_prisma = kel_segitiga * tinggi + a * t

# volume
volume = 0.5 * a * t * tinggi


print("Luas permukaan prisma segitiga adalah: ", luas_permukaan_prisma)
print("Luas sisi prisma segitiga adalah: ", luas_sisi_prisma)
print("Volume prisma segitiga : ", volume)
