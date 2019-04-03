"""
pip install pycrypto
"""
import gmpy2
from Crypto.PublicKey import RSA
from Crypto.Util.number import getPrime
from Crypto.Cipher import PKCS1_OAEP


def generate_key(bits=1024):
    # 生成公钥私钥文件
    p = getPrime(bits)
    q = getPrime(bits)
    n = p * q
    e = 65537
    phin = (p - 1) * (q - 1)
    d = int(gmpy2.invert(e, phin))
    pubkey = RSA.construct((n, e))
    privatekey = RSA.construct((n, e, d, p, q))

    with open("pubkey.pem", "wb") as f:
        f.write(pubkey.exportKey(format="PEM"))
    with open("private.pem", "wb") as f:
        f.write(privatekey.exportKey(format="PEM"))


def generate_key2(bits=1024):
    # 生成公钥私钥文件
    privatekey = RSA.generate(bits, e=65537)
    pubkey = privatekey.publickey()
    with open("pubkey.pem", "wb") as f:
        f.write(pubkey.exportKey(format="PEM"))
    with open("private.pem", "wb") as f:
        f.write(privatekey.exportKey(format="PEM"))


def main1():
    # 常规加密解密

    # 加密
    pubkey = RSA.importKey(open('pubkey.pem').read())
    with open("flag.enc", "wb") as f:
        data = pubkey.encrypt("flag_is_rsa_oaep".encode(), K="x")
        f.write(data[0])

    # 解密
    privatekey = RSA.importKey(open('private.pem').read())

    with open('flag.enc', 'rb') as f:
        print(privatekey.decrypt(f.read()))


def main2():
    # 最优非对称加密填充 oaep padding

    # 加密
    pubkey = RSA.importKey(open('pubkey.pem').read())
    oaep = PKCS1_OAEP.new(pubkey)
    with open("flag.enc", "wb") as f:
        data = oaep.encrypt("flag_is_rsa_oaep".encode())
        f.write(data)

    # 解密
    privatekey = RSA.importKey(open('private.pem').read())
    oaep = PKCS1_OAEP.new(privatekey)
    with open('flag.enc', 'rb') as f:
        print(oaep.decrypt(f.read()))


if __name__ == '__main__':
    # generate_key1()
    # generate_key2()
    # main1()
    main2()
