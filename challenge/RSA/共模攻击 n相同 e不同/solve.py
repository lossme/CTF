"""
原题 http://www.shiyanbar.com/ctf/1834

攻击条件
当两个用户使用相同的模数 N、不同的私钥时，加密同一明文消息时即存在共模攻击。
设两个用户的公钥分别为e1和e2，且两者互质。
当攻击者截获c1和c2后，就可以恢复出明文。
"""
import re
import collections
import itertools

import gmpy2


Item = collections.namedtuple("Item", ["n", "e", "c"])
item_list = []


def parse_file(file):
    # 解析文本
    with open(file) as f:
        for line in f:
            r = re.search(r'\{(\w*) : (\w*) : (\w*)\}', line)
            n, e, c = r.groups()
            item = Item(
                n=int(n.rstrip("L"), base=16),
                e=int(e.rstrip("L"), base=16),
                c=int(c.rstrip("L"), base=16)
            )
            item_list.append(item)
    return item_list


def find_e1_e2_prime(item_list):
    # 找出e1 e2 互质的
    for item1, item2 in itertools.combinations(item_list, 2):
        if gmpy2.gcd(item1.e, item2.e) == 1:
            yield item1, item2


def decode(item1, item2):
    n1, e1, c1 = item1.n, item1.e, item1.c
    n2, e2, c2 = item2.n, item2.e, item2.c
    # n1 == n2 , e1 e2 互质
    assert n1 == n2
    assert gmpy2.gcd(e1, e2) == 1
    n = n1
    gcd, s, t = gmpy2.gcdext(e1, e2)
    if s < 0:
        s = -s
        c1 = gmpy2.invert(c1, n)
    if t < 0:
        t = -t
        c2 = gmpy2.invert(c2, n)
    plain_code = gmpy2.powmod(c1, s, n) * gmpy2.powmod(c2, t, n) % n
    plain_code = int(plain_code)
    return plain_code.to_bytes(plain_code.bit_length() // 8 + 1, "big")


if __name__ == '__main__':
    item_list = parse_file("data/data.txt")
    for item1, item2 in find_e1_e2_prime(item_list):
        b_plain_text = decode(item1, item2)
        print(b_plain_text)
