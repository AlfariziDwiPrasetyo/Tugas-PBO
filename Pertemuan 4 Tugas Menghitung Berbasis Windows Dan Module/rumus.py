from math import pi


def luas_balok(panjang, lebar, tinggi):
    return (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)


def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi


def volume_kubus(rusuk):
    return rusuk * rusuk * rusuk


def luas_kubus(rusuk):
    return 6 * rusuk * rusuk


def luas_bola(radius):
    return 4 * pi * radius**2


def volume_bola(radius):
    return (4/3) * pi * radius**3


def luas_selimut_kerucut(radius, s):
    return pi * radius * s


def luas_permukaan_kerucut(radius, s):
    return pi * radius * s + pi * radius**2


def volume_kerucut(radius, s):
    return pi * radius * s + pi * radius**2


def luas_limas_segiempat(panjang, tinggi):
    ls = 0.5 * panjang * tinggi
    la = panjang**2
    return ls * 5


def volume_limas_segiempat(panjang, tinggi):
    ls = 0.5 * panjang * tinggi
    la = panjang**2
    return (1/3) * la * tinggi


def luas_limas_segitiga(a, t):
    ls = 0.5 * a * t
    return ls * 4


def volume_limas_segitiga(a, t):
    ls = 0.5 * a * t
    return (1/3) * ls * t


def volume_prisma_segitiga(a, t, tinggi):
    return 0.5 * a * t * tinggi


def luas_permukaan_prisma_segitiga(a, t, tinggi):
    keliling_segitiga = a**3
    luas_alas = keliling_segitiga * t
    return luas_alas + a * tinggi


def luas_permukaan_selinder(radius, tinggi):
    return 2 * pi * radius * tinggi + 2 * pi * radius ** 2


def luas_selimut_selinder(radius, tinggi):
    return 2 * pi * radius * tinggi


def volume_selinder(radius, tinggi):
    return pi * radius**2 * tinggi
