import random
import sys

def zorluk_sec():
    print("""
SAYI TAHMİN OYUNUNA HOŞGELDİN!

    1) Kolay Seviye (1-50)
    2) Orta Seviye  (1-100)
    3) Zor Seviye   (1-500)
    4) İmkansız     (1-10000)
    5) Çıkış
    """)

    while True:
        try:
            secim = int(input("Seçimini Yap Dostum!: "))
            if secim in [1, 2, 3, 4, 5]:
                return secim
            else:
                print("Lütfen listeden bir sayı seç.")
        except ValueError:
            print("Lütfen yalnızca sayı gir!")


def sayi_uret(secim):
    if secim == 1:
        print("1-50 arasında bir sayı tuttum, tahmin et!")
        return random.randint(1, 50), 50

    elif secim == 2:
        print("1-100 arasında bir sayı tuttum, tahmin et!")
        return random.randint(1, 100), 100

    elif secim == 3:
        print("1-500 arasında bir sayı tuttum, göster şansını!")
        return random.randint(1, 500), 500

    elif secim == 4:
        print("1-10000 arasında bir sayı tuttum, bilirsen efsanesin!")
        return random.randint(1, 10000), 10000

    elif secim == 5:
        sys.exit()


def sayi_tahmin_oyunu():
    secim = zorluk_sec()
    sayi, ust_sinir = sayi_uret(secim)
    gecmis = []

    sayac = 0

    while True:
        try:
            tahmin = int(input("Tahminin: "))
            sayac += 1
            gecmis.append(tahmin)
        except ValueError:
            print("⛔ Lütfen yalnızca sayı gir!")
            continue

        # ✔️ Doğru sınır kontrolü
        if not (1 <= tahmin <= ust_sinir):
            print(f"⛔ Tahmin sınır dışında! (1 - {ust_sinir}) arasında değer gir.")
            continue

        if tahmin < sayi:
            print("🔼 Daha yüksek bir sayı söyle.")

        elif tahmin > sayi:
            print("🔽 Daha düşük bir sayı söyle.")

        else:
            print(f"\n🎉 Tebrikler! {sayac} tahminde bildin!")
            print(f"📌 Tuttuğum sayı: {sayi}")
            print("\nTahminlerin :\n\n", gecmis)

            tekrar = input("\nTekrar oynamak ister misin? (E/H): ").lower()
            if tekrar == "e":
                sayi_tahmin_oyunu()
            else:

                print("Güle güle dostum!")
                sys.exit()


# Programı başlat
sayi_tahmin_oyunu()
