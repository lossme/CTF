"""
原题 解码磁带 http://www.shiyanbar.com/ctf/1891
"""


def decode(message):
    return "".join(chr(int(i.replace("o", "1").replace("_", "0"), base=2)) for i in message.split())


s = """o____o_
oo__o_o
oo_o__o
oo_o_o_
oo_o__o
oo_ooo_
oo__ooo
_o_ooo_
"""

result = decode(s)
print(result)
# Beijing.


# -----------------------

s2 = """o_o_ooo
oo_o___
oo__o_o
ooo__o_
oo__o_o
_o_____
ooo_o__
oo_o___
oo__o_o
ooo__o_
oo__o_o
_o_____
oo_o__o
ooo__oo
_o_____
oo____o
_o_____
ooo_ooo
oo_o__o
oo_oo__
oo_oo__
_o_oo__
ooo_o__
oo_o___
oo__o_o
ooo__o_
oo__o_o
_o_____
oo_o__o
ooo__oo
_o_____
oo____o
_o_____
ooo_ooo
oo____o
oooo__o
_o_ooo_
"""

result = decode(s2)

print("simCTF{%s}" % result)
# simCTF{Where there is a will,there is a way.}
