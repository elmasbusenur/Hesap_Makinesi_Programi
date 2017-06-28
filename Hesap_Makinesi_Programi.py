secenek1 = "1) toplama işlemi"
secenek2 = "2) çıkarma işlemi"
secenek3 = "3) çarpma işlemi"
secenek4 = "4) bölme işlemi"

print("Toplama işlemi için=1")
print("Çıkarma işlemi için=2")
print("Çarpma işlemi için=3")
print("Bölme işlemi için=4")

secenek=int(input("Lütfen bir işlem seçiniz:"))

while True:
    if (secenek < 1 or secenek > 4):
        print("Lütfen 1-4 arası bir secenek seciniz!")
        secenek = int(input("Lütfen bir işlem seçiniz:"))
    else:
        break
soruAdedi=int(input("kac sayi ile islem yapmak istiyorsun?"))
while True:
    if (secenek == 3 and soruAdedi > 9 or soruAdedi < 1):
        print("Lütfen 1-9 arası bir sayı giriniz!")
        soruAdedi = int(input("kac sayi ile islem yapmak istiyorsun?"))
    else:
        break
while True:
    if (secenek == 4 and soruAdedi > 2 ):
        print("Lütfen 2 sayi ile işlem yapınız!")
        soruAdedi = int(input("kac sayi ile islem yapmak istiyorsun?"))
    else:
        break

print("secenek : " + str(secenek) + ". seçeneği seçtiniz" )

print("soru adedi: " + str(soruAdedi))
sayilar=[]

for i in range(0,soruAdedi):
    sira = i+1
    sayi = int(input("Lütfen "+str(sira)+". sayiyi giriniz: "))
    sayilar.insert(i, sayi)

for i in range(0, len(sayilar)):
   print(str(sayilar[i]))

sonuc = 0
carpmaSonuc=1
bolmeSonuc=1
for i in range(0, len(sayilar)):
    if secenek == 1:
        sonuc = sayilar[i] + sonuc
    if secenek == 2:
        sonuc= sayilar[i] - sonuc
    if secenek == 3:
        carpmaSonuc= sayilar[i]*carpmaSonuc
    if secenek == 4:
        bolmeSonuc= sayilar[i] / bolmeSonuc
if secenek == 3:
    sonuc= carpmaSonuc
if secenek == 4:
    sonuc=bolmeSonuc

print("Sonuç: " + str(sonuc))


