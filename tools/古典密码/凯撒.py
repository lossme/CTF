class Caesar():

    @classmethod
    def encode(cls, message, diff=0):
        a = "abcdefghijklmnopqrstuvwxyz"
        b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        c = a[diff:] + a[:diff]
        d = b[diff:] + b[:diff]
        f = str.maketrans(a + b, c + d)
        return message.translate(f)

    decode = encode


def test():
    s = "NKW uzu pfl jrp"
    print("密  文: {}".format(s))

    for i in range(26):
        res = Caesar.decode(s, i)
        print("diff={:0>2} : {}".format(i, res))


if __name__ == '__main__':
    test()
