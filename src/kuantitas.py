
def HitungKuantitas(daftar):
    
    for item in daftar:
        jumlah = int(input(f"masukan kuantitas barang  {item['barang']}: "))
        item['kuantitas'] = jumlah
        
    return daftar

def SubTotal(daftar):
    bucket = []
    for item in daftar:
        item['subtotal'] = item['harga_satuan'] * item['kuantitas']
        bucket.append(item)
    
    print('subtotal', bucket)
    return bucket
    
def Total(daftar):
    total = []
    for x in daftar: 
        total.append(x['subtotal'])
    Sum = sum(total)
    print("total: ",Sum)
    
            
    
def MetodePembayaran():
    print("Metode Pembayaran:\n1.COD(bayar ditempat).\n2.transfer bank.")
    metbayar=int(input("masukan metode pembayaran yang anda inginkan: "))
    if metbayar == 1 :
        bayar = "pembayaran berhasil!!!.n\Pesanan anda akan menuju ke lokasi anda sekitar beberapa hari lagi"
    elif metbayar == 2 :
        norek=int(input("masukan nomor rekening yang anda gunakan: "))
        sandirek=int(input("masukan sandi rekening anda : "))
        bayar = ("pembayaran berhasil dengan nomor rekening: ",norek)
    else :
        bayar = "mohon masukan data yang benar"
    return bayar 