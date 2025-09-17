class Main:
    def main():
        pass

    def uiLogin():
        pass

    def uiMenu():
        pass

    def uiHitungPembayaran():
        pass

    def uiCetakStruk():
        pass
#======================================================
class HitungPembayaran:
    def __init__(self, idMenu, namaMenu, harga, jumlah, totalHarga):
        self.idMenu=idMenu
        self.namaMenu=namaMenu
        self.harga=harga
        self.jumlah=jumlah
        self.total=harga*jumlah
        self.totalHarga=totalHarga
    
    def insertPembayaran(self):
        pass

    def updatePembayaran(self):
        pass
    
    def deletePembayaran(self):
        pass
    
    def cariDataPembayaranByIdMenu(self):
        pass

#======================================================
class PembayaranTunai:
    def hitungTotalHarga():
        pass

#======================================================
class PembayaranByCard:
    def hitungTotalHarga():
        pass

#======================================================
class TabelHitungPembayaran:
    def __init__(self, idMenu, namaMenu, harga, jumlah, totalHarga):
        self.idMenu=idMenu
        self.namaMenu=namaMenu
        self.harga=harga
        self.jumlah=jumlah
        self.total=harga*jumlah
        self.totalHarga=totalHarga

    def setidMenu():
        pass
        
    def getidMenu():
        pass
        
    def setnamaMenu():
        pass
        
    def getnamaMenu():
        pass
        
    def setHarga():
        pass

    def getHarga():
        pass
        
    def setJumlah():
        pass
    
    def getJumlah():
        pass
    
    def setTotalHarga():
        pass
        
    def getTotalHarga():
        pass
        
#======================================================
class TabelPembayaranByCard:
    def __init__(self, idCard, jenisCard, namaBank, totalHarga):
        self.idCard=idCard
        self.jenisCard=jenisCard
        self.namaBank=namaBank
        self.totalHarga=totalHarga

    def setidCard():
        pass

    def getidCard():
        pass

    def setJenisCard():
        pass

    def getJenisCard():
        pass

    def setnamaBank():
        pass

    def getnamaBank():
        pass

    def setTotalHarga():
        pass

    def getTotalHarga():
        pass

#======================================================
class CetakStruk:
    def cetakStruk():
        pass

#======================================================
class TcetakStruk:
    def __init__(self, noStruk, totalHarga):
        self.noStruk=noStruk
        self.totalHarga=totalHarga
        
#======================================================
class LoginKasir:
    def __init__(self, username, password):
        self.username=username
        self.password=password

    def validasiLogin():
        pass

    def logout():
        pass

#======================================================
class KoneksiDatabase:
    def __init__(self, host, database, userName, password):
        self.host=host
        self.database=database
        self.userName=userName
        self.password=password

    def membukaKoneksi():
        pass

    def eksekusiQuerySelect():
        pass

    def eksekusiQueryInsert():
        pass

    def eksekusiQueryUpdate():
        pass

    def eksekusiQueryDelete():
        pass

    def tutupKoneksi():
        pass