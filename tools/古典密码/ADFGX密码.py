"""
ADFGX 公开密码表

phqgmeaynofdxkrcvszwbutil   http://practicalcryptography.com/ciphers/adfgx-cipher/
btalpdhozkqfvsngicuxmrewy   https://en.wikipedia.org/wiki/ADFGVX_cipher
keyabcdfghilmnopqrstuvwxz   https://www.apprendre-en-ligne.net/crypto/bibliotheque/Plotz/Doc/ADFGVX.html
pgcenbqozrslaftmdviwkuyxh   [1]洪焘宇,柳庆志,王博.在古典密码学范畴下对ADFGX加密法的改进[J].科技创新导报,2013(14):217-218+221.
amretqdnfliobuyckhwzpvsgx   https://www.nku.edu/~christensen/1402%20ADFGVX.pdf
ABCDEFGHIKLMNOPQRSTUVWXYZ   https://www.dcode.fr/adfgx-cipher
"""

DEFAULT_PASSWORD_TABLE = "phqgmeaynofdxkrcvszwbutil"


class ADFGX():

    DECODE_MAP = {("ADFGX"[j] + "ADFGX"[i]): DEFAULT_PASSWORD_TABLE[i + j * 5] for i in range(5) for j in range(5)}

    ENCODE_MAP = {v: k for k, v in DECODE_MAP.items()}

    @classmethod
    def set_password_table(cls, password_table):
        cls.DECODE_MAP = {("ADFGX"[j] + "ADFGX"[i]): password_table[i + j * 5] for i in range(5) for j in range(5)}
        cls.ENCODE_MAP = {v: k for k, v in cls.DECODE_MAP.items()}

    @classmethod
    def encode(cls, message):
        s = message.lower()
        return " ".join(
            map(lambda c: cls.ENCODE_MAP.get(c, c), s)
        )

    @classmethod
    def decode(cls, message):
        return "".join(
            map(lambda x: cls.DECODE_MAP.get(x, x), message.split()
                )
        )


def test():
    message = "Attack at once"
    r = ADFGX.encode(message)
    print(r)

    r = ADFGX.decode(r)
    print(r)


if __name__ == '__main__':
    test()
