import re


class Func():

    def __init__(self, seq):
        self.seq = seq
        self.pattern = re.compile("".join((r'(\w)' for _ in seq)))
        self.encode_cub = "".join((r'\{}'.format(i) for i in seq))
        self.decode_sub = "".join((r'\{}'.format(seq.index(i) + 1) for i in sorted(seq)))

    def encode(self, message):
        return self.pattern.sub(self.encode_cub, message)

    def decode(self, message):
        return self.pattern.sub(self.decode_sub, message)


def test():
    s = """\
ABCDE
FGHIJ
KLNMO
PQRST
UVWXY
"""

    func = Func(seq=[2, 3, 4, 5, 1])
    r = func.encode(s)
    print("密文:\n{}".format(r))
    r = func.decode(r)
    print("明文:\n{}".format(r))


if __name__ == '__main__':
    test()
