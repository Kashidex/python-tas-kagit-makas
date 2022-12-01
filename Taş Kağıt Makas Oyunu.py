import random;
durum = True;
while durum:
 print("Seçim yapınız");
 print("1 : Taş");
 print("2 : Kağıt");
 secim = input("3 : Makas");
 botsecim = random.randint(1,3);

#Berabere Durumları
 if secim == "1" and botsecim == 1:
   print("Rakibin Seçimi: Taş");
   print("Senin Seçimin: Taş");
   print("Sonuç: Berabere");
 elif secim == "2" and botsecim == 2:
   print("Rakibin Seçimi: Kağıt");
   print("Senin Seçimin: Kağıt");
   print("Sonuç: Berabere");
 elif secim == "3" and botsecim == 3:
   print("Rakibin Seçimi: Makas");
   print("Senin Seçimin: Makas");
   print("Sonuç: Berabere");
 #Kazanma Durumları
 elif secim == "1" and botsecim == 3:
   print("Rakibin Seçimi: Makas");
   print("Senin Seçimin: Kağıt");
   print("Sonuç: Kazandın");
 elif secim == "2" and botsecim == 1:
   print("Rakibin Seçimi: Taş");
   print("Senin Seçimin: Kağıt");
   print("Sonuç: Kazandın");
 elif secim == "3" and botsecim == 2:
   print("Rakibin Seçimi: Kağıt");
   print("Senin Seçimin: Makas");
   print("Sonuç: Kazandın");
 #Kaybetme Durumları
 elif secim == "1" and botsecim == 2:
   print("Rakibin Seçimi: Kağıt");
   print("Senin Seçimin: Taş");
   print("Sonuç : Kaybettin");
 elif secim == "2" and botsecim == "3":
   print("Rakibin Seçimi: Makas");
   print("Senin Seçimin: Kağıt");
   print("Sonuç: Kaybettin");
 elif secim == "3" and botsecim == 1:
   print("Rakibin Seçimi: Taş");
   print("Senin Seçimin: Makas");
   print("Sonuç: Kaybettin");
#1, 2 veya 3 sayısından başka bir sayı girilmesi durumunda hata verme durumu
 else:
    print("Lütfen geçerli bir cevap giriniz.")