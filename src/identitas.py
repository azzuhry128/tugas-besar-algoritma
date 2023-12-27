def MasukkanIdentitas():
    Niga = []
    nama = input("Masukkan Nama :")
    noTelp = input("Masukkan No.Telp :")
    Niga.append(noTelp)
    Niga.append(nama)
    
    print(Niga)

    print(nama)
    print(noTelp) 

    return(Niga)

print(MasukkanIdentitas())
