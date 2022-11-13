# Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.

import time

class Bilgisayar():
    def __init__(self,pc_durum = "Kapalı",pc_ses = 0,pc_wifi = "Kapalı"):
        self.pc_durum = pc_durum
        self.pc_ses = pc_ses
        self.pc_wifi = pc_wifi

    def pc_ac(self):
        if (self.pc_durum == "Açık"):
            print("Bilgisayar zaten açık!")
        else:
            print("Bilgisayar açılıyor...")
            time.sleep(2)
            self.pc_durum = "Açık"

    def pc_kapat(self):
        if (self.pc_durum == "Kapalı"):
            print("Bilgisayar zaten kapalı!")
        else:
            print("Bilgisayar kapatılıyor...")
            time.sleep(2)
            self.pc_durum = "Kapalı"

    def pc_uyku (self):
        if (self.pc_durum == "Uyku"):
            print("Bilgisayar zaten uyku modunda.")
        else:
            print("Uyku moduna alınıyor...")
            time.sleep(2)
            self.pc_durum = "Uyku Modunda"

    def pc_ses (self):
        while True:
            cevap = input("Açmak için '>'\nKısmak için: '<'\nSusturmak için: 'x'\nÇıkış: 'Çıkış'")
            if (cevap == ">"):
                if (self.pc_ses != 30):
                    self.pc_ses += 1
                    print("Ses: ",self.pc_ses)
            elif (cevap == "<"):
                if (self.pc_ses != 0):
                    self.pc_ses -= 1
                    print("Ses: ",self.pc_ses)
            elif (cevap == "x"):
                if (self.pc_ses > 0):
                    self.pc_ses = 0
                    print("Bilgisayar susturuldu!")
                    print("Ses: ",self.pc_ses)
            else:
                print("Ses güncellendi: ",self.pc_ses)
                break

    def pc_wifi_ac (self):
        if (self.pc_wifi == "Açık"):
            print("WiFi zaten açık.")
        else:
            print("WiFi açılıyor...")
            time.sleep(2)
            self.pc_wifi = "Açık"

    def pc_wifi_kapat (self):
        if (self.pc_wifi == "Kapalı"):
            print("WiFi zaten kapalı.")
        else:
            print("WiFi kapatılıyor...")
            time.sleep(2)
            self.pc_wifi == "Kapalı"

    def __str__ (self):
        return "PC Durumu: {}\nPC Sesi: {}\nPC Wifi Durumu: {}\n".format(self.pc_durum,self.pc_ses,self.pc_wifi)

bilgisayar = Bilgisayar()

print("""
1. Bilgisayarı Aç
2. Bilgisayarı Kapat
3. Bilgisayarı Uyku Moduna Al
4. Ses Ayarları
5. WiFi Aç
6. WiFi Kapat
7. Bilgisayar Durumu
* Çıkış yapmak için 'q' ya basınız.
    """)

while True:
        islem = input("İşlem Seçiniz: ")

        if (islem == "q"):
            print("Program sonlandırılıyor...")
            time.sleep(2)
            break
        elif (islem == "1"):
            bilgisayar.pc_ac()
        elif (islem == "2"):
            bilgisayar.pc_kapat()
        elif (islem == "3"):
            bilgisayar.pc_uyku()
        elif (islem == "4"):
            bilgisayar.pc_ses()
        elif (islem == "5"):
            bilgisayar.pc_wifi_ac()
        elif (islem == "6"):
            bilgisayar.pc_wifi_kapat()
        elif (islem == "7"):
            print(bilgisayar)
        else:
            print("Geçersiz İşlem!")












