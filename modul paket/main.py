from luas.persegi import *
from luas.persegipanjang import *
from luas.segitiga import *
from luas.lingkaran import *
from luas.trapesium import *
from luas.jajargenjang import *
from volume.kubus import *
from volume.balok import *
from volume.tabung import *
from volume.kerucut import *
from volume.limas import *
from volume.prisma import *

while True:
    print(" ")
    print("----- PERHITUNGAN LUAS DAN VOLUME -----")
    print(" ")
    print("Pilih perhitungan dibawah ini : ")
    print("1. Menghitung luas bangun 2 dimensi")
    print("2. Menghitung volume bangun 3 dimensi")
    print("3. Exit")
    print(" ")
    pilih = input("Pilih (1, 2 atau 3) : ")
    print(" ")

    if pilih == "1":
        print("----- Pilih bangun 2 dimensi -----")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Segitiga")
        print("4. Lingkaran")
        print("5. Jajar Genjang")
        print("6. Trapesium")
        print(" ")
        
        #input pilihan 2 dimensi
        dua_dimensi = input("Pilih bangun datar yang akan dihitung : ") 
        
        if dua_dimensi == "1": #pilih menu persegi
            sisi_persegi = float(input("Panjang Sisi : ")) #input sisi persegi
            luas = (persegi(sisi_persegi)) #import rumus persegi dan hitung
            print('Luas Persegi = ', (luas)) #cetak hasil persegi
            
        elif dua_dimensi == "2": #plih menu persegi panjang
            panjang_pp = float(input("Masukkan Panjang : ")) #input panjang
            lebar_pp = float(input("Masukkan Lebar : ")) #input lebar
            luas = (persegi_panjang(panjang_pp, lebar_pp)) #import rumus persegi panjang dan hitung
            print('Luas Persegi Panjang = ', (luas)) #cetak hasil persegi panjang
    
        elif dua_dimensi == "3": #pilih menu segitiga
            alas_segitiga = float(input("Masukkan Alas : ")) #input alas
            tinggi_segitiga = float(input("Masukkan Tinggi : ")) #input tinggi
            luas = (segitiga(alas_segitiga, tinggi_segitiga)) #import rumus segitiga dan hitung
            print('Luas Segitiga = ', (luas)) #cetak hasil segitiga
            
        elif dua_dimensi == "4": #pilih menu lingkaran
            jari_lingkaran = float(input("Masukkan Jari-jari : ")) #input jari-jari lingkaran
            luas = (lingkaran(jari_lingkaran)) #import rumus lingkaran dan hitung
            print('Luas Lingkaran = ', (luas)) #cetak hasil lingkaran
            
        elif dua_dimensi == "5": #plih menu jajar genjang
            alas_jajargenjang = float(input("Masukkan Alas : ")) #input alas
            tinggi_jajargenjang = float(input("Masukkan Tinggi : ")) #input tinggi
            luas = (jajar_genjang(alas_jajargenjang, tinggi_jajargenjang)) #import rumus jajar genjang dan hitung
            print('Luas Jajar Genjang = ', (luas)) #cetak hasil jajar genjang
            
        elif dua_dimensi == "6": #pilih menu trapesium
            atas_trapesium = float(input("Masukkan Panjang Atas : ")) #input panjang atas
            bawah_trapesium = float(input("Masukkan Sisi Bawah : ")) #input sisi bawah
            tinggi_trapesium = float(input("Masukkan Tinggi : ")) #input tinggi
            luas = (trapesium(atas_trapesium, bawah_trapesium, tinggi_trapesium)) #import rumus trapesium dan hitung
            print('Luas Trapesium = ', (luas)) #cetak hasil trapesium
            
        else: print("-----Pilihan menu tidak tersedia-----")
        
    elif pilih == "2":
        print("----- Pilih bangun 3 dimensi -----")
        print("1. Kubus")
        print("2. Balok")
        print("3. Tabung")
        print("4. Kerucut")
        print("5. Limas")
        print("6. Prisma")
        print(" ")

        #input pilihan 3 dimensi
        tiga_dimensi=input("Pilih bangun ruang yang akan dihitung : ") 
        
        if tiga_dimensi == "1": #pilih menu kubus
            sisi_kubus = float(input("Masukkan Panjang Sisi : ")) #input sisi
            volume = (kubus(sisi_kubus)) #import rumus kubus dan hitung
            print('Volume Kubus = ', (volume)) #cetak hasil kubus
            
        elif tiga_dimensi == "2": #pilih menu balok
            panjang_balok = float(input("Masukkan Panjang : ")) #input panjang
            lebar_balok = float(input("Masukkan Lebar : ")) #input lebar
            tinggi_balok = float(input("Tinggi : ")) #input tinggi
            volume = (balok(panjang_balok, lebar_balok, tinggi_balok)) #import rumus balok dan hitung
            print('Volume Balok = ', (volume)) #cetak hasil balok
            
        elif tiga_dimensi == "3": #pilih menu tabung
            jari_tabung = float(input("Masukkan Jari-jari : "))
            tinggi_tabung = float(input("Masukkan Tinggi : "))
            volume = (tabung(jari_tabung, tinggi_tabung)) #import rumus tabung dan hitung
            print('Volume Tabung = ', (volume)) #cetak hasil tabung
            
        elif tiga_dimensi == "4": #pilih menu kerucut
            jari_kerucut = float(input("Masukkan Jari-jari : ")) #input jari-jari
            tinggi_kerucut = float(input("Masukkan Tinggi : ")) #input tinggi
            volume = (kerucut(jari_kerucut, tinggi_kerucut)) #import rumus kerucut dan hitung
            print('Volume Kerucut = ', (volume)) #cetak hasil kerucut
            
        elif tiga_dimensi == "5": #pilih menu limas
            lalas_limas = float(input("Masukkan Luas Alas : ")) #input alas
            tinggi_limas = float(input("Masukkan Tinggi : ")) #input tinggi
            volume = (limas(lalas_limas, tinggi_limas)) #import rumus limas dan hitung
            print('Volume Limas = ', (volume)) #cetak hasil limas
            
        elif tiga_dimensi == "6": #pilih menu prisma
            lalas_prisma = float(input("Masukkan Luas Alas : ")) #input alas
            tinggi_prisma = float(input("Masukkan Tinggi : ")) #input tinggi
            volume = (prisma(lalas_prisma, tinggi_prisma)) #import rumus prisma dan hitung
            print('Volume Prisma = ', (volume)) #cetak hasil prisma
     
    elif pilih == "3":
        kembali = input("Apakah anda ingin mengulang? (Y/N) ")
        if kembali == "N":
            print('-----Terima Kasih-----')
        elif kembali == "Y":
            continue       
        
        else: print("-----Pilihan menu tidak tersedia-----")
            
    else : print("-----Pilihan menu tidak tersedia-----")