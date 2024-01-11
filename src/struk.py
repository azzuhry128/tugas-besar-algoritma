import datetime
from tabulate import tabulate

header = ['nama barang', 'harga satuan', 'kuantitas', 'subtotal']

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