# Collatz Tabanlı Şifreleme ve Kriptanaliz (Toy Project)

Bu proje, **Collatz (tek/çift) kuralını** temel alan deterministik bir yapı
kullanılarak sözde-rastgele sayı üretimi, anahtar türetme ve
XOR tabanlı basit bir stream şifreleme algoritması tasarlamayı amaçlamaktadır.

Projenin ana hedefi **kriptografik güvenlik sağlamak değil**,
tasarlanan bir algoritmanın **nasıl analiz edilebileceğini ve kırılabileceğini**
uygulamalı olarak göstermektir.

---

## Collatz Kuralı

Algoritmanın temelinde aşağıdaki Collatz kuralı yer almaktadır:

- Eğer sayı **tek** ise → `3n + 1`
- Eğer sayı **çift** ise → `n / 2`

Bu kurallar tekrar edilerek algoritmanın iç durumu (state) deterministik
bir şekilde güncellenir.

---

## Proje Mimarisi

Proje üç ana bileşenden oluşmaktadır:

### 1. CollatzMix (RNG)

- Bir başlangıç değeri (**seed**) ile başlar.
- Her adımda Collatz tek/çift kuralı uygulanır.
- Elde edilen değerler basit bir karıştırma (mix) fonksiyonundan geçirilerek
  64-bit sözde-rastgele çıktılar üretilir.

### 2. Anahtar / Keystream Türetme

- CollatzMix çıktıları birleştirilerek **256-bit (32 byte)** uzunluğunda
  bir anahtar veya keystream elde edilir.
- Aynı seed kullanıldığında her zaman aynı anahtar üretilir.

### 3. Şifreleme (XOR Stream Cipher)

- Üretilen keystream, düz metin (plaintext) ile XOR işlemine sokulur.
- XOR işlemi simetrik olduğu için aynı işlem çözme (decrypt) için de kullanılır.

---

## Kırma (Attack) Senaryosu

Bu proje bilinçli olarak **kırılabilir** şekilde tasarlanmıştır.

Kullanılan zayıflıklar:

- Algoritma **deterministiktir** (aynı seed → aynı keystream).
- Seed uzayı **küçük** tutulmuştur (örnek: 1–100.000).
- Mesajın başlangıcı tahmin edilebilir bir prefix içerir (örnek: `"MSG:"`).

### Saldırı Yöntemi

1. Ciphertext ele geçirilir.
2. Olası seed değerleri brute-force yöntemiyle denenir.
3. Her denemede elde edilen plaintext, bilinen prefix ile kontrol edilir.
4. Doğru seed bulunduğunda tüm mesaj çözülebilir.

Bu saldırı `attack/break_demo.py` dosyasında uygulanmıştır.

---

## Dosya Yapısı
