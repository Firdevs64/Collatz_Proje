"""
Basit XOR stream cipher (eğitim amaçlı)
"""

from src.collatzmix import CollatzMix

def keystream(seed: int, nbytes: int) -> bytes:
    rng = CollatzMix(seed)
    out = bytearray()
    while len(out) < nbytes:
        out.extend(rng.next_u64().to_bytes(8, "big"))
    return bytes(out[:nbytes])


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def encrypt(seed: int, plaintext: bytes) -> bytes:
    ks = keystream(seed, len(plaintext))
    return xor_bytes(plaintext, ks)


def decrypt(seed: int, ciphertext: bytes) -> bytes:
    return encrypt(seed, ciphertext)
