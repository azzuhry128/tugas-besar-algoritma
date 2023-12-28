import mysql.connector

connector = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="algoritma"
)

def PilihMenu():
    daftarPilihan = []
    while True :
        print("==========PILIHAN MENU==========")
        print("1.Lihat Harga Barang")
        print("2.KELUAR")
        pilihan=input("Masukkan Pilihan Anda[1-2] : ")
        if pilihan == '1':
            print("=====BARANG YANG  DI JUAL=====")
            print("cultivator")
            print("traktor")
            print("mesin perontok padi")
            namaBarang=input("masukkan Nama Barang [cultivator/traktor/mesin perontok padi] : ")
            
            cursor = connector.cursor()
            sql = "SELECT harga FROM barang WHERE nama=%s"
            
            cursor.execute(sql,(namaBarang,))
            hargaBarang = cursor.fetchone()
            
            dictionary = {}
            dictionary['barang'] = namaBarang
            dictionary['harga_satuan'] = hargaBarang[0]
            daftarPilihan.append(dictionary)
        elif pilihan == '2':
            # dictionary = {f"data{x+1}": value for x, value in daftarPilihan}
            return daftarPilihan