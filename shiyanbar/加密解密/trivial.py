"""
原题 trivial http://www.shiyanbar.com/ctf/1980


An unlocked terminal is displaying the following:

Encryption complete, ENC(???,T0pS3cre7key) = Bot kmws mikferuigmzf rmfrxrwqe abs perudsf! Nvm kda ut ab8bv_w4ue0_ab8v_DDU

You poke around and find this interesting file.

加密函数
#!/usr/bin/env python
import sys

alphaL = "abcdefghijklnmopqrstuvqxyz"
alphaU = "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
num    = "0123456789"
keychars = num+alphaL+alphaU

if len(sys.argv) != 3:
  print "Usage: %s SECRET_KEY PLAINTEXT"%(sys.argv[0])
  sys.exit()

key = sys.argv[1]
if not key.isalnum():
  print "Your key is invalid, it may only be alphanumeric characters"
  sys.exit()

plaintext = sys.argv[2]

ciphertext = ""
for i in range(len(plaintext)):
  rotate_amount = keychars.index(key[i%len(key)])
  if plaintext[i] in alphaL:
    enc_char = ord('a') + (ord(plaintext[i])-ord('a')+rotate_amount)%26
  elif plaintext[i] in alphaU:
    enc_char = ord('A') + (ord(plaintext[i])-ord('A')+rotate_amount)%26
  elif plaintext[i] in num:
    enc_char = ord('0') + (ord(plaintext[i])-ord('0')+rotate_amount)%10
  else:
    enc_char = ord(plaintext[i])
  ciphertext = ciphertext + chr(enc_char)

print "Encryption complete, ENC(%s,%s) = %s"%(plaintext,key,ciphertext)
"""


class Func():

    # 整理一下加密函数
    # 缺了 w/W 有坑
    alphaL = "abcdefghijklnmopqrstuvqxyz"
    alphaU = "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
    num = "0123456789"
    keychars = num + alphaL + alphaU

    def __init__(self, key):
        self.key = key

    def encode(self, plaintext):
        ciphertext = ""
        for i in range(len(plaintext)):
            rotate_amount = self.keychars.index(self.key[i % len(self.key)])
            if plaintext[i] in self.alphaL:
                enc_char = ord('a') + (ord(plaintext[i]) - ord('a') + rotate_amount) % 26
            elif plaintext[i] in self.alphaU:
                enc_char = ord('A') + (ord(plaintext[i]) - ord('A') + rotate_amount) % 26
            elif plaintext[i] in self.num:
                enc_char = ord('0') + (ord(plaintext[i]) - ord('0') + rotate_amount) % 10
            else:
                enc_char = ord(plaintext[i])
            ciphertext = ciphertext + chr(enc_char)
        return ciphertext

    def decode(self, ciphertext):
        plaintext = ""
        for idx, c in enumerate(ciphertext):
            rotate_amount = self.keychars.index(self.key[idx % len(self.key)])
            if c in self.alphaL or c in "w":
                i = ord("a") + (ord(c) - ord('a') - rotate_amount) % 26
            elif c in self.alphaU or c in "W":
                i = ord("A") + (ord(c) - ord('A') - rotate_amount) % 26
            elif c in self.num:
                i = ord("0") + (ord(c) - ord('0') - rotate_amount) % 10
            else:
                i = ord(c)
            plaintext += chr(i)
        return plaintext


def test():
    f = Func(key="T0pS3cre7key")
    plaintext = "123789abcxyzABCXYZ"
    print("plaintext:", plaintext)
    ciphertext = f.encode(plaintext)
    print("ciphertext:", ciphertext)
    ciphertext_decode = f.decode(ciphertext)
    print("ciphertext_decode:", ciphertext_decode)
    assert ciphertext_decode == plaintext


if __name__ == '__main__':
    func = Func(key="T0pS3cre7key")
    s = "Bot kmws mikferuigmzf rmfrxrwqe abs perudsf! Nvm kda ut ab8bv_w4ue0_ab8v_DDU"
    print(s)
    r = func.decode(s)
    print(r)
