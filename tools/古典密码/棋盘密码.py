DEFAULT_PASSWORD_TABLE = "abcdefghiklmnopqrstuvwxyz"


class ADFGX():

    DECODE_MAP = {("12345"[j] + "12345"[i]): DEFAULT_PASSWORD_TABLE[i + j * 5] for i in range(5) for j in range(5)}

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
            map(lambda x: cls.DECODE_MAP.get(x, x), message.split(" ")
                )
        )


def test():
    message = "Attack at once"
    r = ADFGX.encode(message)
    print("密文: {}".format(r))

    r = ADFGX.decode(r)
    print("明文: {}".format(r))


if __name__ == '__main__':
    test()
