import sys
sys.path.insert(1, './src')

from identitas import MasukkanIdentitas
from pemilihan import PilihMenu
from kuantitas import HitungKuantitas
from kuantitas import SubTotal
from kuantitas import MetodePembayaran
from kuantitas import Total

def main():
    # identitasPembeli = MasukkanIdentitas()
    daftarPilihan = PilihMenu()
    kuantitas = HitungKuantitas(daftarPilihan)
    subtotal = SubTotal(kuantitas)
    total = Total(subtotal)
    metode = MetodePembayaran()
    print(total)
    
    # checkout = Chekout(kuantitas)
    
    # print('identitas pembeli:', identitasPembeli)
    # print('daftar pilihan barang:', daftarPilihan)
    
    # print(kuantitas)

main()