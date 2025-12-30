from src.cipher import decrypt


KNOWN_PREFIX = b"MSG:"  # herkesin mesajı böyle başlayacak (kolay analiz/kırma)
MAX_SEED = 100000       # kolay olsun diye küçük tut (100k yeter)


def find_seed(ciphertext: bytes):
    for seed in range(1, MAX_SEED + 1):
        pt = decrypt(seed, ciphertext)
        if pt.startswith(KNOWN_PREFIX):
            return seed, pt
    return None, None


def main():
    ct_hex = input("Ciphertext hex gir: ").strip()
    ciphertext = bytes.fromhex(ct_hex)

    seed, pt = find_seed(ciphertext)
    if seed is None:
        print("Seed bulunamadı (MAX_SEED artır veya prefix değişmiş olabilir).")
    else:
        print("Seed bulundu:", seed)
        print("Plaintext:", pt)


if __name__ == "__main__":
    main()
