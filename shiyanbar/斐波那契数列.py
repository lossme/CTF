"""
原题 http://www.shiyanbar.com/ctf/1872
数列A满足An = An-1 + An-2 + An-3, n >= 3
编写程序，输入A0, A1 和 A2的值1 1 1时, 计算A99的高八位。
key格式：CTF{}
"""
import itertools


def generate():
    a = 1
    b = 1
    c = 1
    n = 0
    yield 0, 1
    yield 1, 1
    yield 2, 1
    for idx in itertools.count(3):
        n = a + b + c
        a, b, c = b, c, n
        yield idx, n


f = generate()

number = 0
for _ in range(99 + 1):
    idx, number = next(f)
    # print(idx, number)

print(number)
print("CTF{%s}" % str(number)[:8])
