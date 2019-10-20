from  Nilai import Nilai

class AplikasiNilai :
    name = input("Masukkan Nama Mahasiswa : ")
    nilai = input("Masukkan Nilai : ")
    objek = Nilai(name , int(nilai))
    print()
    print("Nama Mahasiswa : " , objek.tampilNama())
    print("Nilai : " , objek.tampilNilai())
    print("Grade : " ,objek.cariNilai())