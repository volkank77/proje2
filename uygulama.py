# rehber_islemleri modülünü içeri aktar
import rehber_islemleri

def menu_goster():
    """
    Kullanıcıya seçenekleri gösteren menüyü yazdırır.
    """
    print("\n" + "="*30)
    print("📞 Basit Telefon Rehberi Uygulaması")
    print("="*30)
    print("1. Kişi Ekle")
    print("2. Rehberi Görüntüle")
    print("3. Kişi Sil")
    print("4. Kişi Güncelle")
    print("5. Çıkış")
    print("="*30)

def kisi_ekle_arayuzu():
    """
    Kullanıcıdan yeni kişi bilgilerini alır ve ekleme fonksiyonunu çağırır.
    """
    print("\n--- Kişi Ekle ---")
    isim = input("Eklenecek kişinin adı: ").strip()
    telefon = input("Eklenecek kişinin telefon numarası: ").strip()

    if isim and telefon:
        # Modüldeki fonksiyonu çağır
        rehber_islemleri.kisi_ekle(isim, telefon)
    else:
        print("Hata: İsim ve telefon alanı boş bırakılamaz.")

def rehberi_goruntule_arayuzu():
    """
    Rehberi okur ve ekrana listeler.
    """
    print("\n--- Telefon Rehberi ---")
    kisiler = rehber_islemleri.rehberi_oku()
    
    if not kisiler:
        print("Rehberde kayıtlı kimse yok.")
        return

    # Tablo formatında yazdırmak için
    max_isim_uzunluk = max(len(kisi['isim']) for kisi in kisiler) if kisiler else 0
    
    print("-" * (max_isim_uzunluk + 20))
    print(f"{'İsim':<{max_isim_uzunluk}} | Telefon")
    print("-" * (max_isim_uzunluk + 20))

    for kisi in sorted(kisiler, key=lambda x: x['isim']): # İsim sırasına göre sırala
        print(f"{kisi['isim']:<{max_isim_uzunluk}} | {kisi['telefon']}")
    
    print("-" * (max_isim_uzunluk + 20))

def kisi_silme_arayuzu():
    """
    Kullanıcıdan silinecek kişinin ismini alır ve silme fonksiyonunu çağırır.
    """
    print("\n--- Kişi Sil ---")
    isim = input("Silinecek kişinin adı: ").strip()

    if isim:
        # Modüldeki fonksiyonu çağır
        rehber_islemleri.kisi_sil(isim)
    else:
        print("Hata: İsim alanı boş bırakılamaz.")

def kisi_guncelle_arayuzu():
    """
    Kullanıcıdan güncellenecek kişiyi ve yeni bilgileri alır, güncelleme fonksiyonunu çağırır.
    """
    print("\n--- Kişi Güncelle ---")
    eski_isim = input("Güncellenecek kişinin mevcut adı: ").strip()
    
    if not eski_isim:
        print("Hata: Mevcut isim alanı boş bırakılamaz.")
        return

    # Hangi bilginin güncelleneceğini sor
    print("Güncellemek istediğiniz alanları girin (boş bırakırsanız değişmez):")
    yeni_isim = input(f"Yeni isim (mevcut: {eski_isim}): ").strip() or None
    yeni_telefon = input(f"Yeni telefon numarası: ").strip() or None
    
    # En az bir alanın güncellenip güncellenmediğini kontrol et
    if yeni_isim is None and yeni_telefon is None:
        print("İsim veya telefon numarası girilmedi. Güncelleme yapılmadı.")
        return

    # Modüldeki fonksiyonu çağır
    rehber_islemleri.kisi_guncelle(eski_isim, yeni_isim, yeni_telefon)


def main():
    """
    Ana uygulama döngüsü.
    """
    while True:
        menu_goster()
        secim = input("Lütfen bir seçenek girin (1-5): ").strip()

        if secim == '1':
            kisi_ekle_arayuzu()
        elif secim == '2':
            rehberi_goruntule_arayuzu()
        elif secim == '3':
            kisi_silme_arayuzu()
        elif secim == '4':
            kisi_guncelle_arayuzu()
        elif secim == '5':
            print("\nProgramdan çıkılıyor. Güle güle! 👋")
            break
        else:
            print("Geçersiz seçenek. Lütfen 1 ile 5 arasında bir sayı girin.")

# Uygulama buradan başlar
if __name__ == "__main__":
    main()