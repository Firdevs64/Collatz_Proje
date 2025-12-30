MASK64 = (1 << 64) - 1

def collatz_step(n: int) -> int:
    if n <= 0:
        raise ValueError("n pozitif olmalı")
    return 3 * n + 1 if (n & 1) else n // 2

def mix64(x: int) -> int:
    x &= MASK64
    x ^= (x >> 30) & MASK64
    x = (x * 0xbf58476d1ce4e5b9) & MASK64
    x ^= (x >> 27) & MASK64
    x = (x * 0x94d049bb133111eb) & MASK64
    x ^= (x >> 31) & MASK64
    return x & MASK64

class CollatzMix:
    def __init__(self, seed: int):
        if seed <= 0:
            raise ValueError("seed pozitif olmalı")
        self.state = seed

    def next_u64(self) -> int:
        s = self.state
        for _ in range(5):
            s = collatz_step(s)
            if s == 1:
                s += 0x9E3779B97F4A7C15
        self.state = s
        return mix64(s)

def derive_key(seed: int, key_len: int = 32) -> bytes:
    rng = CollatzMix(seed)
    out = bytearray()
    while len(out) < key_len:
        out.extend(rng.next_u64().to_bytes(8, "big"))
    return bytes(out[:key_len])
