

from tabulate import tabulate
import datetime


# tanggalPembelian = datetime.datetime.now()
# kodeResi = int(datetime.datetime.now() * 1000)

# pesanan = {
#     "resi": kodeResi,
#     "pembeli": 'surya atmajaya',
#     'hp' : '082249034332',
#     'barang': [["cultivator", 10000000, 3, 30000000],["sprayer", 20000000, 2, 40000000],],
#     'metode': 'kartu debit',
#     'total': 70000000
# }

kodeResi = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
header = ['nama barang', 'harga satuan', 'kuantitas', 'subtotal']

def CetakStruk(identitas, dataPembelian, total, metode):
    # resi, pembeli, hp, barang, metode, total = data.values()
    print('kode resi: ', kodeResi)
    print('nama pembeli: ', identitas[1])
    print('nomor hp pembeli: ', identitas[0])
    # print(tabulate(dataPembelian, headers=header, tablefmt='grid'))
    print(dataPembelian)
    print('total pembayaran: ', total)
    print('metode pembayaran: ', metode)
    
    # print
    
    
    # print("\nresi pembelian")
    # print("NO. Resi: ", resi)
    # print("nama pembeli: ", identitas[0])
    # print("telepon: ", identitas[1])

    # print(tabulate(order, headers=header, tablefmt='grid'))

    # for items in barang:
    #     print(f'''
    #     nama barang: {items["nama"]}
    #     harga barang: {items["harga"]}
    #     kuantitas: {items["kuantitas"]}
    #     subtotal: {items["subtotal"]}
    #     ''')