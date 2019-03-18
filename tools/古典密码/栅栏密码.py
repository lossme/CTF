import itertools


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


class Fence():

    @staticmethod
    def get_fence_numbers(message):
        s_len = len(message)
        return [i for i in range(2, s_len - 1) if s_len % i == 0]

    @staticmethod
    def encode(message, fence_number):
        chunk_len = len(message) // fence_number
        data = ["".join(i) for i in grouper(message, chunk_len, fillvalue=" ")]

        return "".join(
            data[row][col]
            for col in range(chunk_len)
            for row in range(fence_number)
        )

    decode = encode


def test():
    message = "tn c0afsiwal kes,hwit1r  g,npt  ttessfu}ua u  hmqik e {m,  n huiouosarwCniibecesnren."
    print("message: {}".format(message))
    fence_numbers = Fence.get_fence_numbers(message)
    for fence_number in fence_numbers:
        r = Fence.decode(message, fence_number)
        print("fence_number={}: {}".format(fence_number, r))


if __name__ == '__main__':
    test()
