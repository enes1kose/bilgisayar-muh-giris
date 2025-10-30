# Basit Toplama ve Çıkarma Hesap Makinesi

def hesap_makinesi():
    print("Basit Hesap Makinesi (Sadece Toplama ve Çıkarma)")
    
    # Kullanıcıdan işlem tipini al
    islem = input("Yapmak istediğiniz işlemi seçin (+ veya -): ")
    
    if islem not in ['+', '-']:
        print("Geçersiz işlem! Sadece + veya - kullanabilirsiniz.")
        return  # Fonksiyonu sonlandırır
    
    # Kullanıcıdan sayıları al
    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
        return
    
    # İşlem yap ve sonucu göster
    if islem == '+':
        sonuc = sayi1 + sayi2
    else:  # islem == '-'
        sonuc = sayi1 - sayi2
    
    print(f"Sonuç: {sonuc}")

# Fonksiyonu çalıştır
hesap_makinesi()

