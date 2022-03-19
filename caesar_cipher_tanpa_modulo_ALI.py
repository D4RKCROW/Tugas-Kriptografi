
def caesar_enkripsi(kalimat_awal,kunci):
  enkripsi = ''
  for i in kalimat_awal:
    if i.isupper():
      rumus = 65 + ((ord(i) - 65 + kunci)) 
      enkripsi = enkripsi + chr(rumus)                              
    elif i.islower():
      rumus = 97 + ((ord(i) - 97 + kunci))
      enkripsi = enkripsi + chr(rumus)
    else:
      enkripsi = enkripsi + i
 
  print("Hasil enkripsinya adalah:",enkripsi)
  
def caesar_dekripsi(hasil_enkripsi,kunci):
  dekripsi = ''
  for i in hasil_enkripsi:
    if i.isupper():
        rumus = 65 + ((ord(i) - 65 - kunci)) 
        dekripsi = dekripsi + chr(rumus)                              
    elif i.islower():
        rumus = 97 + ((ord(i) - 97 - kunci)) 
        dekripsi = dekripsi + chr(rumus)
    else:
        dekripsi = dekripsi + i  
 
  print("Hasil dekripsi dari kalimat tersebut adalah : ",dekripsi)

print("Masukkan pilihan")
print("1. Enkripsi")
print("2. Dekripsi")
pilihan = int(input())
if pilihan == 1:
    kalimat_awal = input("Masukkan kalimat yang akan di enkripsi: ")
    kunci = int(input("Masukkan kunci : "))
    caesar_enkripsi(kalimat_awal,kunci)
if pilihan == 2:
    hasil_enkripsi = input("Masukkan kalimat yang akan di dekripsi : ")
    kunci = int(input("Masukkan kunci : "))
    caesar_dekripsi(hasil_enkripsi,kunci)
