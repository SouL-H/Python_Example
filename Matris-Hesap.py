
#Matris hesapları için yardimci kütüphane
import numpy as np

#Kullanin girdisine göre değer oluşturmak için oluşturulan fonksiyon
def matris_olustur(x,y):
    flag=[]
    for satir in range(x):
        tutucu=[]
        for sutun in range(y):
            tutucu.append(int(input("Matrisin[%d][%d].degerini girin : " % (satir,sutun))))
        flag.append(tutucu)
    return np.matrix(flag)
# Global değişkenler
A = []
B = []
C = []
E1= []
E2= []
E3= []
E4= []

#Kullanicidan matris degerleri alma ve değişkene atama
for q in range(3):
    print()
    x=int(input("%d.matrisin satir sayisi girin : "% (q+1)));
    y=int(input("%d.matrisin satir sayisi girin : "% (q+1)));
    print()
    if q==0:
        A=matris_olustur(x,y)
    elif q==1:
        B=matris_olustur(x,y)
    else:
        C=matris_olustur(x,y)



print("Girilen A matrisi")
print(A,"\n")
print("Girilen B matrisi")
print(B,"\n")
print("Girilen C matrisi")
print(C,"\n")
print("Hesaplanan D Matris")
D=np.array(A.transpose()+B*C)
print(D,"\n")
print("Satirlari toplanmis E Dizisi")
E=np.array(D.sum(axis=1))
print(E,"\n")

#E dizisi için matematik hesabi yapma
for dongu in range(len(E)):
    E1.append(np.cos(E[dongu]))
    E2.append(np.math.log(E[dongu]))    
    E3.append(np.math.factorial(E[dongu]))
    E4.append(np.math.sqrt(E[dongu]))
    
#Cıktılar 
print("E’nin elemanlarının kosinüsü: ",E1)
print("E’nin elemanlarının logaritması: ",E2)
print("E’nin elemanlarının faktörüyeli: ",E3)
print("E’nin elemanlarının kökü: ",E4)
