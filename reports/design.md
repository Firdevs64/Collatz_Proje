# Tasarım (Design)

## Amaç
Bu çalışmanın amacı, Collatz (tek/çift) kuralını temel alan deterministik bir yapı
kullanarak sözde-rastgele sayı üretmek, bu yapıdan bir anahtar/keystream türetmek
ve XOR tabanlı basit bir stream şifreleme algoritması tasarlamaktır.

Bu tasarımın ana hedefi kriptografik güvenlik sağlamak değil; analiz edilebilir,
kırılabilir ve eğitim amaçlı bir örnek oluşturmaktır.

---

## Collatz Kuralı
Algoritmanın temelini oluşturan Collatz kuralı şu şekildedir:

- Eğer n tek sayı ise → n = 3n + 1  
- Eğer n çift sayı ise → n = n / 2  

Bu kurallar tekrar edilerek sayı dizisi üretilir ve algoritmanın iç durumu
deterministik olarak güncellenir.

---

## Genel Mimari
Algoritma üç ana bileşenden oluşmaktadır:

1. **CollatzMix (RNG)**
   - Başlangıç değeri (seed) ile başlar.
   - Her adımda Collatz tek/çift kuralı uygulanır.
   - Elde edilen değerler basit bir karıştırma (mix) fonksiyonundan geçirilerek
     64-bit çıktı üretilir.

2. **Anahtar / Keystream Türetme**
   - CollatzMix çıktıları birleştirilerek sabit uzunlukta (varsayılan 256-bit)
     bir anahtar veya keystream elde edilir.

3. **Şifreleme (XOR Stream Cipher)**
   - Üretilen keystream, düz metin (plaintext) ile XOR işlemine sokulur.
   - Aynı seed kullanıldığında aynı keystream üretildiği için çözme işlemi de
     XOR ile gerçekleştirilir.

---

## Tehdit Modeli
Bu tasarımda aşağıdaki varsayımlar yapılmıştır:

- Saldırgan şifreli metni (ciphertext) görebilir.
- Başlangıç değeri (seed) sınırlı bir aralıkta seçilmiş olabilir.
- Mesaj formatının veya başlangıç kısmının (örneğin "MSG:") tahmin edilebilir
  olduğu durumlar mevcuttur.

---

## Tasarım Kararları
- Algoritma bilinçli olarak **deterministik** tasarlanmıştır.
- Seed uzayı küçük tutulabilir, böylece brute-force saldırıları mümkündür.
- XOR tabanlı şifreleme tercih edilmiştir çünkü analiz ve kırma süreci
  kağıt üzerinde kolayca açıklanabilmektedir.

---

## Güvenlik Değerlendirmesi
Bu tasarım kriptografik olarak güvenli değildir.
Deterministik yapı, küçük seed uzayı ve bilinen düz metin (known-plaintext)
senaryoları altında algoritma kırılabilir durumdadır.

**Bu tasarım özellikle analiz ve kırma yapılabilsin diye basit tutulmuştur.  
Kriptografik güvenlik iddiası yoktur.**
