"""
原题 ROT-13变身了 http://www.shiyanbar.com/ctf/1901

提示：1、回旋13，回不回？ 2、有81,450,625种可能性
"""


s = "83 89 78 84 45 86 96 45 115 121 110 116 136 132 132 132 108 128 117 118 134 110 123 111 110 127 108 112 124 122 108 118 128 108 131 114 127 134 108 116 124 124 113 108 76 76 76 76 138 23 90 81 66 71 64 69 114 65 112 64 66 63 69 61 70 114 62 66 61 62 69 67 70 63 61 110 110 112 64 68 62 70 61 112 111 112"

message = "".join(map(lambda x: chr(int(x) - 13), s.split(" ")))
print(message)
# flag{www_shiyanbar_com_is_very_good_????}
# MD5: 38e4c352809e150186920aac37190cbc


# ------------------------------------
# math.pow(81450625, 1/4) = 95 应该是所有可见字符组成
# md5爆破
# python 1s 50w左右

import itertools
import string
import hashlib
import datetime


ds = datetime.datetime.now()
print("{}: running".format(ds))

for iter_times, item in enumerate(itertools.product(*[string.printable for i in range(4)])):
    s = "flag{www_shiyanbar_com_is_very_good_%s%s%s%s}" % item
    if hashlib.md5(s.encode()).hexdigest() == "38e4c352809e150186920aac37190cbc":
        dn = datetime.datetime.now()
        print("{}: done".format(dn))
        print("result={}".format(s))
        print("iter_times={} 耗时: {} s".format(iter_times, (dn - ds).seconds))
        break
