import random as r

#Global Degiskenler
uretilen = []
girilen = []
sayac = 0
kontrol =0
adim = 0

#6 adet 1-49 arasında random sayı üretme
for i in range(0, 6):
    x = r.randint(1, 49)
    uretilen.append(x)

# print(uretilen) Sistemin ürettiği sayıyı önceden görmek için.

print("\n")   
print("--- 1-49 Arasi Sayi tahmininde Bulunun ---")

#Üretilen sayilari tahmin etmek için
while True:
    deger = int(input("%d.tahmininiz: " % (adim+1)))
    if deger > 0 and deger<49  :
        girilen.append(deger)
        adim+=1
        kontrol+=1
        if kontrol==6:
            break
    else:
         print("Lütfen 1-49 arası sayi giriniz.")
   
#Uretilen sayiyi yazdirma
for c in uretilen:
    if c in girilen:
        sayac+=1  
print("Üretilen Sayilar: ",uretilen) 
  

# Sonucu yazdirma.
if(sayac==0):
    print("Maalesef tahminleriniz doğru değil.")
else:
    print("%d tane doğru tahminde bulunduz."%(sayac)) 

