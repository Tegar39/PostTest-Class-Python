class Main:
    def main(self):
        pass

    def uiLogin(self):
        pass

    def uiMenu(self):
        pass

    def uiHitungPembayaran(self):
        pass

    def uiCetakStruk(self):
        pass
#======================================================
class HitungPembayaran:
    def __init__(self, idMenu: str, namaMenu: str, harga: float, jumlah: int, totalHarga: float):
        self.idMenu=idMenu
        self.namaMenu=namaMenu
        self.harga=harga
        self.jumlah=jumlah
        self.total=self.harga*self.jumlah
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
    def __init__(self):
        pass

    def hitungTotalHarga(self):
        pass

#======================================================
class PembayaranByCard:
    def __init__(self):
        pass

    def hitungTotalHarga(self):
        pass

#======================================================
class TabelHitungPembayaran:
    def __init__(self, idMenu: str, namaMenu: str, harga: float, jumlah: int, totalHarga: float):
        self.idMenu=idMenu
        self.namaMenu=namaMenu
        self.harga=harga
        self.jumlah=jumlah
        self.total=harga*jumlah
        self.totalHarga=totalHarga

    def setidMenu(self):
        pass
        
    def getidMenu(self):
        pass
        
    def setnamaMenu(self):
        pass
        
    def getnamaMenu(self):
        pass
        
    def setHarga(self):
        pass

    def getHarga(self):
        pass
        
    def setJumlah(self):
        pass
    
    def getJumlah(self):
        pass
    
    def setTotalHarga(self):
        pass
        
    def getTotalHarga(self):
        pass
        
#======================================================
class TabelPembayaranByCard:
    def __init__(self, idCard: str, jenisCard: str, namaBank: str, totalHarga: float):
        self.idCard=idCard
        self.jenisCard=jenisCard
        self.namaBank=namaBank
        self.totalHarga=totalHarga

    def setidCard(self):
        pass

    def getidCard(self):
        pass

    def setJenisCard(self):
        pass

    def getJenisCard(self):
        pass

    def setnamaBank(self):
        pass

    def getnamaBank(self):
        pass

    def setTotalHarga(self):
        pass

    def getTotalHarga(self):
        pass

#======================================================
class CetakStruk:
    def cetakStruk(self):
        pass

#======================================================
class TcetakStruk:
    def __init__(self, noStruk: str, totalHarga: float):
        self.noStruk=noStruk
        self.totalHarga=totalHarga
        
#======================================================
class LoginKasir:
    def __init__(self, username: str, password: str):
        self.username=username
        self.password=password

    def validasiLogin(self):
        pass

    def logout(self):
        pass

#======================================================
class KoneksiDatabase:
    def __init__(self, host: str, database: str, userName: str, password: str):
        self.host=host
        self.database=database
        self.userName=userName
        self.password=password

    def membukaKoneksi(self):
        pass

    def eksekusiQuerySelect(self):
        pass

    def eksekusiQueryInsert(self):
        pass

    def eksekusiQueryUpdate(self):
        pass

    def eksekusiQueryDelete(self):
        pass

    def tutupKoneksi(self):
        pass
