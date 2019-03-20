import gmpy2


class RSA():

    def __init__(self, n, e, d=None):
        self.n = n
        self.e = e
        self.d = d

    def encode(self, plaintext):
        code = int.from_bytes(plaintext.encode(), "big")
        cipher = gmpy2.powmod(code, self.e, self.n)
        return cipher

    def decode(self, cipher):
        assert self.d
        code_decrypt = int(gmpy2.powmod(cipher, self.d, self.n))
        plaintext = code_decrypt.to_bytes(code_decrypt.bit_length() // 8 + 1, "big").decode()
        return plaintext


def test():

    p = 258631601377848992211685134376492365269
    q = 286924040788547268861394901519826758027
    n = p * q
    e = 65537
    phin = (p - 1) * (q - 1)
    d = gmpy2.invert(e, phin)
    plaintext = "flag"
    rsa = RSA(n=n, e=e, d=d)
    cipher = rsa.encode(plaintext)
    plaintext_decrypt = rsa.decode(cipher)

    print("plaintext:", plaintext)
    print("cipher:", cipher)
    print("plaintext_decrypt:", plaintext_decrypt)

    assert plaintext_decrypt == plaintext


if __name__ == '__main__':
    test()
