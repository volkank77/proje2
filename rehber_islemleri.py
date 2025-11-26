import os

# Rehber dosyasının adı
DOSYA_ADI = "rehber.txt"

def rehberi_oku():
    """
    Dosyadaki tüm kişileri okur ve liste olarak döndürür.
    Her kişi, {'isim': '...', 'telefon': '...'} formatında bir sözlüktür.
    Dosya yoksa boş bir liste döndürür.
    """
    if not os.path.exists(DOSYA_ADI):
        return [] # Dosya yoksa boş liste döndür

    kisiler = []
    try:
        with open(DOSYA_ADI, 'r', encoding='utf-8') as f:
            for satir in f:
                satir = satir.strip()
                if satir: # Boş satırları atla
                    try:
                        isim, telefon = satir.split(':')
                        kisiler.append({'isim': isim.strip(), 'telefon': telefon.strip()})
                    except ValueError:
                        # Hatalı formatlı satırları yoksay
                        print(f"Uyarı: Hatalı formatlı satır atlandı: {satir}")
        return kisiler
    except IOError:
        print(f"Hata: {DOSYA_ADI} dosyası okunamadı.")
        return []

def rehberi_kaydet(kisiler):
    """
    Verilen kişi listesini dosyaya kaydeder (eski içeriği siler).
    """
    try:
        with open(DOSYA_ADI, 'w', encoding='utf-8') as f:
            for kisi in kisiler:
                # 'İsim:Telefon' formatında kaydet
                f.write(f"{kisi['isim']}:{kisi['telefon']}\n")
        return True
    except IOError:
        print(f"Hata: {DOSYA_ADI} dosyasına yazılamadı.")
        return False

def kisi_ekle(isim, telefon):
    """
    Yeni bir kişiyi rehbere ekler.
    """
    kisiler = rehberi_oku()
    # Aynı isimde kişi var mı kontrol et (basitlik için)
    for kisi in kisiler:
        if kisi['isim'].lower() == isim.lower():
            print(f"Hata: '{isim}' adında bir kişi zaten rehberde var.")
            return False

    kisiler.append({'isim': isim, 'telefon': telefon})
    if rehberi_kaydet(kisiler):
        print(f"'{isim}' rehbere başarıyla eklendi.")
        return True
    return False

def kisi_sil(isim):
    """
    Belirtilen isimdeki kişiyi rehberden siler.
    """
    kisiler = rehberi_oku()
    eski_sayi = len(kisiler)
    
    # Silinecek kişinin hariç tutulduğu yeni bir liste oluştur
    yeni_kisiler = [kisi for kisi in kisiler if kisi['isim'].lower() != isim.lower()]

    if len(yeni_kisiler) < eski_sayi:
        if rehberi_kaydet(yeni_kisiler):
            print(f"'{isim}' rehberden başarıyla silindi.")
            return True
        return False # Kaydetme hatası
    else:
        print(f"Hata: '{isim}' rehberde bulunamadı.")
        return False

def kisi_guncelle(eski_isim, yeni_isim=None, yeni_telefon=None):
    """
    Belirtilen isimdeki kişinin bilgilerini günceller.
    """
    kisiler = rehberi_oku()
    guncellendi = False

    for kisi in kisiler:
        if kisi['isim'].lower() == eski_isim.lower():
            if yeni_isim is not None:
                kisi['isim'] = yeni_isim
            if yeni_telefon is not None:
                kisi['telefon'] = yeni_telefon
            guncellendi = True
            break
            
    if guncellendi:
        if rehberi_kaydet(kisiler):
            print(f"'{eski_isim}' kişisinin bilgileri başarıyla güncellendi.")
            return True
        return False # Kaydetme hatası
    else:
        print(f"Hata: '{eski_isim}' rehberde bulunamadı.")
        return False