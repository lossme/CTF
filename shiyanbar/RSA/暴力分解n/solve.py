import gmpy2
p = gmpy2.mpz(286924040788547268861394901519826758027)
q = gmpy2.mpz(258631601377848992211685134376492365269)
n = p * q
e = 65537
phin = (p - 1) * (q - 1)

c = int.from_bytes(open("data/flag.enc", "rb").read(), "big")

d = gmpy2.invert(e, phin)

plain_text_code = gmpy2.powmod(c, d, n)
plain_text_code = int(plain_text_code)

plain_text = plain_text_code.to_bytes(plain_text_code.bit_length() // 8 + 1, "big")
print(plain_text)
