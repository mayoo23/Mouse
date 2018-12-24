print("===================== OOP =====================")
print(" Program pendaftaran perguruan silat ")
print("\n")
class PerguruanSilat():
	def __init__ (self, nama, umur):
		self.nama = nama
		self.umur = umur
		print("Anggota baru : %s" % self.nama)
	def info(self):
		print("Nama : %s, Umur : %s"% (self.nama, self.umur))
		
class Pelatih():
	def __init__(self, nama, umur, honor):
		self.nama = nama
		self.umur = umur
		self.honor = honor
		print("Pelatih baru : %s" % self.nama)
	def info(self):
		print("Nama : %s memiliki Honor : %s" % (self.nama,self.honor))
		
class Murid():
	def __init__(self, nama, umur, tingkatan):
		self.nama = nama
		self.umur = umur
		self.tingkatan = tingkatan
		print("Murid lama : %s" % self.nama)
	def info(self):
		print("Nama Murid : %s, Tingkatannya : %s" % (self.nama,self.tingkatan))

class MuridBaru():
	def __init__(self, nama, umur, tingkatan):
		self.nama = nama
		self.umur = umur
		self.tingkatan = tingkatan
		print("Murid baru : %s" % self.nama)
	def info(self):
		print("Nama Murid baru : %s, Tingkatannya : %s" % (self.nama,self.tingkatan))

		
namaa=str(input("Nama: "))
umurr=int(input("Umur: "))
tingkat=str(input("tingkatan: "))
print("\n")

	



