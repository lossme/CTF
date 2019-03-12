"""
公开密码表   来源
ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8    https://asecuritysite.com/encryption/ADFGVX
ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789    https://www.dcode.fr/adfgvx-cipher
Z8HV7XEQLTGPCAOWS06K4MJI1Y2FNBURD593    https://cryptocompanion.netlify.com/adfgvx
na1c3h8tb2ome5wrpd4f6g7i9j0klqsuvxyz    https://en.wikipedia.org/wiki/ADFGVX_cipher
dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g    https://kifanga.com/what-is-adfgvx-cipher/
co8xf4mk3az9nwl0jd5siyhup1vb6req7t2g    https://www.britannica.com/topic/ADFGVX-cipher
ai2o0d1bh6mstnwcq4lg7vyrf5e3xz9pjk8u    https://www.nku.edu/~christensen/1402%20ADFGVX.pdf
"""

DEFAULT_PASSWORD_TABLE = "ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8"


class ADFGX():

    DECODE_MAP = {("ADFGVX"[j] + "ADFGVX"[i]): DEFAULT_PASSWORD_TABLE[i + j * 6] for i in range(6) for j in range(6)}

    ENCODE_MAP = {v: k for k, v in DECODE_MAP.items()}

    @classmethod
    def set_password_table(cls, password_table):
        cls.DECODE_MAP = {("ADFGVX"[j] + "ADFGVX"[i]): password_table[i + j * 6] for i in range(6) for j in range(6)}
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
            map(
                lambda x: cls.DECODE_MAP.get(x, x), message.split()
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
