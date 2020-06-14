print("\n")
print("--- Floyd üçgeni ---")
#Input Deger alma
girdi = int(input("Oluşturulacak Floyd üçgenin satir sayisini giiriniz: "))
sayici=1
print("\n")

#Floyd üçgeni oluşturma
for i in range(1,girdi+1):
    for j in range(1,i+1):
        print(sayici,end="\t")
        sayici+=1
    print("")
