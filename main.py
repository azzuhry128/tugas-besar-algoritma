import sys
sys.path.insert(1, './src')

from identitas import MasukkanIdentitas
from pemilihan import PilihMenu
from kuantitas import HitungKuantitas
from kuantitas import SubTotal
from kuantitas import MetodePembayaran
from kuantitas import Total
from struk import CetakStruk

def main():
    identitasPembeli = MasukkanIdentitas()
    daftarPilihan = PilihMenu()
    kuantitas = HitungKuantitas(daftarPilihan)
    subtotal = SubTotal(kuantitas)
    total = Total(subtotal)
    metode = MetodePembayaran()
    CetakStruk(identitasPembeli, subtotal, total, metode)
    

main()