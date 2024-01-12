<<<<<<< HEAD


=======
import datetime
>>>>>>> 36522363d3019172d354446f691fcde7bf0f3e43
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

<<<<<<< HEAD
def CetakStruk(identitas, dataPembelian, total, metode):
    # resi, pembeli, hp, barang, metode, total = data.values()
    print('kode resi: ', kodeResi)
    print('nama pembeli: ', identitas[1])
    print('nomor hp pembeli: ', identitas[0])
    # print(tabulate(dataPembelian, headers=header, tablefmt='grid'))
    print(dataPembelian)
    print('total pembayaran: ', total)
    print('metode pembayaran: ', metode)
    
=======
date= datetime.datetime.now()
formatted_date = date.strftime('%Y-%m-%d')
miliseconds = int(date.timestamp() * 1000)

pesanan = {
    "resi": miliseconds,
    'tanggal': formatted_date,
    "pembeli": 'surya atmajaya',
    'hp' : '082249034332',
    'barang': [{"cultivator", 10000000, 3, 30000000},{"sprayer", 20000000, 2, 40000000},],
    'metode': 'kartu debit',
    'total': 70000000
}

def CetakStruk(data):
    resi, tanggal,pembeli, hp, barang, metode, total = data.values()

    print("\nresi pembelian")
    print("NO. Resi: ", resi)
    print("tanggal: ", tanggal)
    print("nama pembeli: ", pembeli)
    print("telepon: ", hp)

    print(tabulate(barang, headers=header, tablefmt='grid'))

    print('metode pembayaran: ', metode)
    print('total pembayaran: ', total)

CetakStruk(pesanan)
>>>>>>> 36522363d3019172d354446f691fcde7bf0f3e43
