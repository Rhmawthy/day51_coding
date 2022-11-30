#program inputan menghitung volume kubus, lalu menentukan bilangan genap pada volume kubus

sisi= int(input("masukkan nilai sisi : "))

volume = sisi**3
print("volume kubus = ", volume)

if  volume %2 == 0 :
	print (volume, "merupakan angka genap")

else:
	print (volume, "merupakan angka ganjil")