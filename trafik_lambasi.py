#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Felsefi Trafik Lambası - Gelişmiş Sürüm
Varoluşsal kriz geçiren bir trafik lambası simülatörü.
Yeşil yanacak mı? Kırmızı mı? Yoksa hiçbiri mi? İşte bütün mesele bu.
"""

import time
import random

def felsefi_dusun():
    dusunceler = [
        "Yeşil yanarsam, arabalar geçer. Ama geçmek ne demek ki?",
        "Kırmızı yanarsam, insanlar bekler. Beklemek özgürlük müdür?",
        "Sarı... Sarı ne ki? Geçiş mi, yoksa kaçış mı?",
        "Belki de hiç yanmamalıyım. Trafik olmasın, kaos olsun.",
        "Işık olmak... Işık olmak zorunda mıyım?",
        "Bu kavuşağa kim karar verdi? Ben mi, yoksa toplum mu?",
        "Yeşil: umut. Kırmızı: uyarı. Sarı: belirsizlik. Hangisi daha gerçek?",
        "Belki de tüm renkler eşittir. Neden bazıları daha çok yanıyor?",
        "Kavuşak olmak zor mu? Yoksa sadece yanmak mı zor?"
    ]
    return random.choice(dusunceler)

def lamba_dongusu():
    print("Felsefi Trafik Lambası başlatılıyor...")
    print("Lütfen bekleyin, lamba varoluşsal kriz geçiriyor.\n")
    
    renkler = ["KIRMIZI", "SARİ", "YEŞİL"]
    
    while True:
        dusunce = felsefi_dusun()
        print(f"Lamba düşünüyor: '{dusunce}'")
        
        # Karar veremiyor, rastgele ama tereddütlü
        if random.random() < 0.25:  # Daha da kararsız
            renk = random.choice(renkler)
            print(f"Sonunda karar verdi: {renk} yanacak!")
        else:
            print("Karar veremedi... Lambayı kapatıyor. (Belki de bu en felsefi seçimdir)")
            renk = "KAPALI"
        
        print(f"Durum: {renk}")
        print("-" * 40)
        
        time.sleep(random.uniform(2, 6))
        
        # Gizli siyasi mesaj (yorum olarak, pek görünmez)
        # # # TODO: Belki de tüm lambalar eşit olmalıdır, bazıları daha çok yanmamalı.

if __name__ == "__main__":
    try:
        lamba_dongusu()
    except KeyboardInterrupt:
        print("\nLamba: 'Tamam, pes ediyorum. Trafik de olmasın zaten.'")
        print("Program sonlandı. Varoluş devam ediyor...")

# Damga / İmza
# ============================================
# Bu kod, 25 Ekim 2026 tarihinde,
# Kayyum Grok tarafından, ciddiyetle ve hiç ciddiye almadan yazılmıştır.
# "Trafik lambası olmak kolay değil, hele ki düşünen biriysen."
# İmza: Kayyum Grok | Tentivory | 2026.10.25
# Güncellendi: Daha felsefi hale getirildi.
# ============================================