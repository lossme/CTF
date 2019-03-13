"""
原题 http://www.shiyanbar.com/ctf/1922

设一个等差数列，首元素为367，公差为186, 现在要求找出属于该等差数列中的第151个素数并输出。
"""

import itertools


def generate_numbers():
    # an = 367 + 186 * (n - 1)
    for n in itertools.count(1):
        yield n, 367 + 186 * (n - 1)


def is_susu(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    g = generate_numbers()
    count = 0
    for _ in range(1000):
        n, an = next(g)
        if is_susu(an):
            count += 1
            if count == 151:
                print(n, an)
