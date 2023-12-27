import sys
sys.path.insert(1, './src')

from identitas import MasukkanIdentitas
from pemilihan import PilihMenu

def main():
    identitasPembeli = MasukkanIdentitas()
    daftarPilihan = PilihMenu()
    print('identitas pembeli:', identitasPembeli)
    print('daftar pilihan barang:', daftarPilihan)

main()