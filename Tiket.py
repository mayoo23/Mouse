nama = input('Nama : ')
alamat = input('masukan Alamat : ')
KTP = int(input("Masukkan Nomer KTP Anda : "))
other = ()

other_Tujuan = input('Masukkan Tujuan Anda : ')
other_ASL = input('Masukkan Stasiun asal : ')
print("===================================== Stasiun Online ==========================================")
def guest(nama, alamat, KTP, other):
    print ("Nama Anda    :",nama)
    print ("Alamat Anda:",alamat)
    print ("Nomer KTP Anda   :",KTP)
    print ("Lain-lain    ")
    print (other_Tujuan)
    print (other_ASL)
guest(nama, alamat, KTP, other)

print ("==============================================================================================")
x = int(input("Masukkan Harga  : "))
jumlah_tiket = int(input("Masukkan jumlah tiket  = "))
total = x*jumlah_tiket
print("Total Harga", nama, "Anda adalah Rp.",total)
pembayaran = int(input("Tunai = "))
kekurangan = total-pembayaran
if(pembayaran>total):
	print("kembali Rp.", pembayaran-total)
	
print ("======================== Selamat Jalan, Semoga Selamat Sampai Tujuan==========================")