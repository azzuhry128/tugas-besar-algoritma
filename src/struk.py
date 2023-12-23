pesanan = {
    "resi": 8374862837,
    "pembeli": 'surya atmajaya',
    'hp' : '082249034332',
    'barang': [
        {
            "nama": "cultivator",
            "harga": 10000000,
            "kuantitas": 3,
            "subtotal": 30000000
        },
        {
            "nama": "sprayer",
            "harga": 20000000,
            "kuantitas": 2,
            "subtotal": 40000000
        },
    ],
    'total': 70000000
}



def cetakStruk(data):
    resi, pembeli, hp, barang, total = data.values()

    print(f'''
        RESI PEMBELIAN
        NO RESI       : {resi}
        nama pembeli  : {pembeli}
        nomor hp      : {hp}
    ''')

    for items in barang:
        print(f'''
        nama barang: {items["nama"]}
        harga barang: {items["harga"]}
        kuantitas: {items["kuantitas"]}
        subtotal: {items["subtotal"]}
        ''')

    print(f'''
        total: {total}
    ''')

cetakStruk(pesanan)