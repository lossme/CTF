"""
http://www.shiyanbar.com/ctf/1892

在线代的课本上出现了一堆神秘字母

dloguszijluswogany

而旁边的矩阵是

1 2
0 1

快找出flag吧
"""

import itertools

import numpy as np


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


a = np.array([[1, 2], [0, 1]])
print("a:\n", a)

s = "dloguszijluswogany"
plantext = ""
for item in grouper(s, n=2):
    b = np.array([ord(c) - 96 for c in item])
    # a dot b
    r = np.linalg.inv(a).dot(b) % 26
    plantext += "".join(map(lambda x: chr(int(x + 96)), r))

print("plantext:", plantext)
