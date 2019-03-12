class Func():

    DECODE_MAP = {
        "由": "1",
        "中": "2",
        "人": "3",
        "工": "4",
        "大": "5",
        "王": "6",
        "夫": "7",
        "井": "8",
        "羊": "9",
        "口": "0"
    }
    ENCODE_MAP = {v: k for k, v in DECODE_MAP.items()}

    @classmethod
    def encode(cls, message):
        return "".join(
            cls.ENCODE_MAP[i] for i in message
        )

    @classmethod
    def decode(cls, message):
        return "".join(
            cls.DECODE_MAP[c] for c in message
        )


def test():
    message = "".join(
        str(ord(i)) for i in "CTF"
    )

    r = Func.encode(message)
    print("密文: {}".format(r))

    r = Func.decode(r)
    print("明文: {}".format(r))

    message = "".join(
        chr(int(r[idx:idx + 2])) for idx in range(0, len(r), 2)
    )
    print("message: {}".format(message))


if __name__ == '__main__':
    test()
