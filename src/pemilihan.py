import mysql.connector

def connectionDatabase():
    connector = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="algoritma"
            )
    if connector.is_connected:
        print("Database terkoneksi")
        return connector
    else:
        print("Gagal terhubung ke Database")
        return False
connectionDatabase()

# def piliMenu(nama):
#     try:
#         conn = connectionDatabase()
#         cursor = conn.cursor()
#         sql = "SELECT * FROM barang WHERE nama = %s" 
#         data = (nama,)
#         cursor.execute(sql,data)
#         result = cursor.fetchall()
#         if result:  
#             print(result)
#         else:
#             print("Tidak ada data yang ditemukan")
#     except mysql.connector.Error as error:
#         print("kesalahan : ",error)
#     finally:
#         if conn.is_connected():
#             cursor.close()
#             conn.close()

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
            daftarPilihan.append(namaBarang)
        elif pilihan == '2':
            dictionary = {f"data{x+1}": value for x, value in enumerate(daftarPilihan)}
            print(dictionary)
            return dictionary