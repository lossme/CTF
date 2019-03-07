def func_caesar(s, diff):
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c = a[diff:] + a[:diff]
    d = b[diff:] + b[:diff]

    f = str.maketrans(a + b, c + d)
    return s.translate(f)


if __name__ == '__main__':
    s = "NKW uzu pfl jrp"
    print("密    文: {}".format(s))

    for i in range(26):
        res = func_caesar(s, i)
        print("diff={:0>2} : {}".format(i, res))
