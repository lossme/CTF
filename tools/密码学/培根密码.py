class Bacon():

    def __init__(self, a, b, cipher=1):
        self.a = a
        self.b = b
        if cipher == 1:
            self.decode_map = {
                0: 'a',
                1: 'b',
                2: 'c',
                3: 'd',
                4: 'e',
                5: 'f',
                6: 'g',
                7: 'h',
                8: 'i',  # i/j
                9: 'k',
                10: 'l',
                11: 'm',
                12: 'n',
                13: 'o',
                14: 'p',
                15: 'q',
                16: 'r',
                17: 's',
                18: 't',
                19: 'u',  # u/v
                20: 'w',
                21: 'x',
                22: 'y',
                23: 'z'
            }
            self.encode_map = {v: k for k, v in self.decode_map.items()}
            self.encode_map.setdefault("v", 19)
            self.encode_map.setdefault("j", 8)

        if cipher == 2:
            self.decode_map = {idx: i for idx, i in enumerate("abcdefghijklmnopqrstuvwxyz")}
            self.encode_map = {v: k for k, v in self.decode_map.items()}

    def encode(self, message, sep=None):
        s = message.lower()

        rv = " ".join(
            "{:0>5b}".format(self.encode_map.get(c, 0))
            for c in s
        )
        return rv.replace("0", self.a).replace("1", self.b)

    def decode(self, message, sep=None):
        s = message.replace(self.a, "0").replace(self.b, "1")
        return "".join(
            self.decode_map.get(int("0b" + i, base=2), " ") for i in s.split(sep=sep)
        )


def test():
    bacon = Bacon(a="A", b="B", cipher=1)
    message = "ABABA ABBAB BAABB AABAA"

    r = bacon.decode(message)
    print("明文: {}".format(r))

    r = bacon.encode(r)
    print("密文: {}".format(r))


if __name__ == '__main__':
    test()
