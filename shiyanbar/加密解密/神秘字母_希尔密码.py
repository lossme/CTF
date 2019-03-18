"""
http://www.shiyanbar.com/ctf/1892

在线代的课本上出现了一堆神秘字母

dloguszijluswogany

而旁边的矩阵是

1 2
0 1

快找出flag吧
"""


import numpy as np


# 将文本拆成 (2, 9)
s = "dloguszijluswogany"
s1 = ""
s2 = ""
for idx, c in enumerate(s):
    if idx % 2 == 0:
        s1 += c
    else:
        s2 += c
print("s1:", s1)
print("s2:", s2)
l1 = list(map(lambda x: ord(x) - 96, s1))
l2 = list(map(lambda x: ord(x) - 96, s2))
print("l1:", l1)
print("l2:", l2)


# a dot b
a = np.array([[1, 2], [0, 1]])
print("a:\n", a)

b = np.array([l1, l2])
print("b:\n", b)

r = np.linalg.inv(a).dot(b) % 26

print("a.dot(b) = r:\n", r)
r1 = "".join(map(lambda x: chr(int(x + 96)), r[0]))
r2 = "".join(map(lambda x: chr(int(x + 96)), r[1]))
print("r1:", r1)
print("r2:", r2)

plantext = "".join(map(lambda x: x[0] + x[1], zip(r1, r2)))
print("plantext:", plantext)
