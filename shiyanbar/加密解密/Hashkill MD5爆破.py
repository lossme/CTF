"""
原题 http://www.shiyanbar.com/ctf/1807

6ac66ed89ef9654cf25eb88c21f4ecd0是flag的MD5码，（格式为ctf{XXX_XXXXXXXXXXX_XXXXX}）由一个0-1000的数字，下划线，纽约的一个区，下划线，一个10000-15000的数字构成。

"""
import itertools
import hashlib

a = ["{}".format(i) for i in range(1000)]
# a = ["{:0>3d}".format(i) for i in range(1000)]

b = ['thebronx', 'brooklyn', 'manhattan', 'queens', 'statenlsland']

c = ["{:0>5d}".format(i) for i in range(10000, 15000)]


for i, j, k in itertools.product(a, b, c):
    s = "ctf{%s_%s_%s}" % (i, j, k)
    if hashlib.md5(s.encode()).hexdigest() == "6ac66ed89ef9654cf25eb88c21f4ecd0":
        print(s)
        break
