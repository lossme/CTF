import gmpy2

p = gmpy2.mpz(258631601377848992211685134376492365269)
q = gmpy2.mpz(286924040788547268861394901519826758027)
e = gmpy2.mpz(65537)
n = p * q
phin = (p - 1) * (q - 1)
d = gmpy2.invert(e, phin)


message = "hello rsa"
print("message: {}".format(message))

code = int.from_bytes(message.encode(), "big")
print("code: {}".format(code))

cipher = gmpy2.powmod(code, e, n)
print("cipher: {}".format(cipher))


code_decrypt = int(gmpy2.powmod(cipher, d, n))
print("code_decrypt: {}".format(code_decrypt))


message_decrypt = code_decrypt.to_bytes(code_decrypt.bit_length() // 8 + 1, "big").decode()
print("message_decrypt: {}".format(message_decrypt))
