class Rot13():

    @classmethod
    def encode(cls, message):
        a = "abcdefghijklmnopqrstuvwxyz"
        b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        c = a[13:] + a[:13]
        d = b[13:] + b[:13]
        f = str.maketrans(a + b, c + d)
        return message.translate(f)

    decode = encode


def test():
    message = "ABC xyz"

    r = Rot13.encode(message)
    print("密文: {}".format(r))

    r = Rot13.decode(r)
    print("明文: {}".format(r))


if __name__ == '__main__':
    test()
