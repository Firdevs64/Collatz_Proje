# Kriptanaliz (Cryptanalysis)

## Zayıflık 1: Deterministik yapı
Aynı seed her zaman aynı keystream ürettiği için algoritma rastgelelik sağlamaz.

## Zayıflık 2: Küçük seed uzayı -> brute-force
Seed 1..100000 aralığındaysa tüm seed değerleri denenebilir.

## Zayıflık 3: Known-plaintext (bilinen prefix)
Mesajın "MSG:" ile başladığı bilindiğinde, her seed denenip çözülmüş metnin
prefix kontrolü ile doğru seed hızlıca bulunabilir.

## Sonuç
Seed bulunduğunda aynı keystream üretildiği için tüm mesaj çözülebilir.
Bu nedenle tasarım kriptografik olarak güvenli değildir (eğitim amaçlıdır).
