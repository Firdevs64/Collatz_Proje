from src.collatzmix import CollatzMix, derive_key
from src.cipher import encrypt, decrypt


def main():
    # Burayı İSTERSEN sabit bırak, istersen random seç (ama saldırı için seed aralığı küçük olsun!)
    seed = 1337

    # 1) RNG çıktıları
    rng = CollatzMix(seed)
    print("5 adet u64 çıktı:")
    for _ in range(5):
        print(rng.next_u64())

    # 2) 256-bit key
    key = derive_key(seed)
    print("\n256-bit key (hex):", key.hex())

    # 3) Şifreleme
    # Bilinen prefix: "MSG:" -> saldırıda işimize yarayacak (known-plaintext)
    msg = b"MSG: Collatz demo | DATE: 2025-12-30 | DATA: Hello"
    ct = encrypt(seed, msg)
    pt = decrypt(seed, ct)

    print("\nPlaintext:", msg)
    print("Ciphertext(hex):", ct.hex())
    print("Decrypted:", pt)


if __name__ == "__main__":
    main()
