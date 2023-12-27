pesanan = {
    "resi": 8374862837,
    "pembeli": 'surya atmajaya',
    'hp' : '082249034332',
    'barang': [["cultivator", 10000000, 3, 30000000],["sprayer", 20000000, 2, 40000000],],
    'metode': 'kartu debit',
    'total': 70000000
}

from tabulate import tabulate

header = ['nama barang', 'harga satuan', 'kuantitas', 'subtotal']

def cetakStruk(data):
    resi, pembeli, hp, barang, metode, total = data.values()

    print("\nresi pembelian")
    print("NO. Resi: ", resi)
    print("nama pembeli: ", pembeli)
    print("telepon: ", hp)

    print(tabulate(barang, headers=header, tablefmt='grid'))

    # for items in barang:
    #     print(f'''
    #     nama barang: {items["nama"]}
    #     harga barang: {items["harga"]}
    #     kuantitas: {items["kuantitas"]}
    #     subtotal: {items["subtotal"]}
    #     ''')
    print('metode pembayaran: ', metode)
    print('total pembayaran: ', total)

cetakStruk(pesanan)