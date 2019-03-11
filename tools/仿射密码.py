
class Func():

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.ENCODE_MAP = self.create_map(a, b)
        self.DECODE_MAP = {v: k for k, v in self.ENCODE_MAP.items()}

    @classmethod
    def create_map(cls, a, b):
        return {chr(i + 65): chr(((a * i + b) % 26) + 65) for i in range(26)}

    def encode(self, message):
        s = message.upper()
        return "".join(map(lambda x: self.ENCODE_MAP.get(x, " "), s))

    def decode(self, message):
        s = message.upper()
        return "".join(map(lambda x: self.DECODE_MAP.get(x, " "), s))


if __name__ == '__main__':
    func = Func(a=5, b=8)

    message = "offensive time tomorrow morning at ten o'clock"
    r = func.encode(message)
    print("密文: {}".format(r))

    r = func.decode(r)
    print("明文: {}".format(r))
