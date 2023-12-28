import sys
sys.path.insert(1, './src')

from identitas import MasukkanIdentitas
from pemilihan import PilihMenu
from kuantitas import HitungKuantitas
from kuantitas import Chekout

def main():
    # identitasPembeli = MasukkanIdentitas()
    daftarPilihan = PilihMenu()
    kuantitas = HitungKuantitas(daftarPilihan)
    checkout = Chekout(kuantitas)
    
    # print('identitas pembeli:', identitasPembeli)
    # print('daftar pilihan barang:', daftarPilihan)
    
    # print(kuantitas)

main()