# def items(self):
#     self.items = []
    
# def tambahKuantitas(self):
#     self
    
def HitungKuantitas(daftar):
    kuantitas = []
    array = []
    x=daftar.values()
    
    for item in x:
        jumlah = input(f"masukan kuantitas barang  {item}")
        kuantitas.append(item)
        kuantitas.append(jumlah)  
        array.append(kuantitas)
        
    # print(kuantitas)
    # print(array)
    return array
    
# def Chekout(array):
#     subtotal = []
#     for x in array:
#         subtotal.append(x[1])
#         break
    
#     print(subtotal)

def Chekout(array):
    for x in set(map(tuple, array)):
        print(list(x)[0])
    
    # print("/n----Chekout----")
    # for item in array.items:
    #     print(f"{item.nama}- harga: {item.harga} - jumlah: {item.jumlah}")
    # total = array.hitung_total()
    # print(f"total Pembayaran: {total}")
    # print("---terima kasih telah berbelanja!---")
    # array.items = []
    

# def metode_pembayaran():
#     print("Metode Pembayaran:\n1.COD(bayar ditempat).\n2.transfer bank.\n3.SpayLater.\n4.Via agen/Mitra")
#     metbayar=int(input("masukan metode pembayaran yang anda inginkan: "))
#     if metbayar == 1 :
#         bayar = "Pesanan anda akan menuju ke lokasi anda sekitar beberapa hari lagi"
#     elif metbayar == 2 :
#         norek=int(input("masukan nomor rekening yang anda gunakan: "))
#         sandirek=int(input("masukan sandi rekening anda : "))
#         bayar = ("pembayaran berhasil dengan nomor rekening: ",norek)
#     elif metbayar == 3 :
#         bayar = "Pembayaran berhasil Tunggu Konfirmasi Beberapa saat lagi"
#     elif metbayar == 4 :
#         agen=str(input("masukan Nama Agen Cabang Yang anda Gunakan: "))
#         bayar = ("Pembayaran berhasil melalui agen: ",agen)
#     else :
#         bayar = "mohon masukan data yang benar"
#     return bayar 