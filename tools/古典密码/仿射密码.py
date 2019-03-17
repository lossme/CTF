
class Func():

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.ENCODE_MAP = self.create_map(a, b)
        self.DECODE_MAP = {v: k for k, v in self.ENCODE_MAP.items()}

    @classmethod
    def create_map(cls, a, b):
        code_map = {}
        for i in range(26):
            code_map[chr(i + 65)] = chr(((a * i + b) % 26) + 65)
            code_map[chr(i + 97)] = chr(((a * i + b) % 26) + 97)
        return code_map

    def encode(self, message):
        return "".join(
            map(
                lambda x: self.ENCODE_MAP.get(x, x), message
            )
        )

    def decode(self, message):
        return "".join(
            map(
                lambda x: self.DECODE_MAP.get(x, x), message
            )
        )


def test():
    func = Func(a=5, b=8)

    message = "offensive time tomorrow morning at ten o'clock"
    r = func.encode(message)
    print("密文: {}".format(r))

    r = func.decode(r)
    print("明文: {}".format(r))


if __name__ == '__main__':
    test()
