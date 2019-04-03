"""
适用情况：e过大或过小。

工具：https://github.com/pablocelayes/rsa-wiener-attack

在e过大或过小的情况下，可使用算法从e中快速推断出d的值。详细的算法原理可以阅读：低解密指数攻击 。
"""

import ContinuedFractions
import Arithmetic
import RSAvulnerableKeyGenerator


def hack_RSA(e, n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)

    for (k, d) in convergents:

        # check if d is actually the key
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s * s - 4 * n
            if(discr >= 0):
                t = Arithmetic.is_perfect_square(discr)
                if t != -1 and (s + t) % 2 == 0:
                    print("Hacked!")
                    return d

# TEST functions


def test_hack_RSA():
    print("Testing Wiener Attack")
    n = 0x92411fa0c93c1b27f89e436d8c4698bcf554938396803a5b62bd10c9bfcbf85a483bd87bb2d6a8dc00c32d8a7caf30d8899d90cb8f5838cae95f7ff5358847db1244006c140edfcc36adbdcaa16cd27432b4d50d2348b5c15c209364d7914ef50425e4c3da07612cc34e9b93b98d394b43f3eb0a5a806c70f06697b6189606eb9707104a7b6ff059011bac957e2aae9ec406a4ff8f8062400d2312a207a9e018f4b4e961c943dfc410a26828d2e88b24e4100162228a5bbf0824cf2f1c8e7b915efa385efeb505a9746e5d19967766618007ddf0d99525e9a41997217484d64c6a879d762098b9807bee46a219be76941b9ff31465463981e230eecec69691d1
    e = 0x6f6b385dd0f06043c20a7d8e5920802265e1baab9d692e7c20b69391cc5635dbcaae59726ec5882f168b3a292bd52c976533d3ad498b7f561c3dc01a76597e47cfe60614f247551b3dbe200e2196eaa001a1d183886eeacddfe82d80b38aea24de1a337177683ed802942827ce4d28e20efef92f38f1b1a18c66f9b45f5148cceabfd736de8ac4a49e63a8d35a83b664f9f3b00f822b6f11ff13257ee6e0c00ca5c98e661ea594a9e66f2bd56b33d9a13f5c997e67a37fcf9a0c7f04d119fe1ba261127357e64a4b069aefed3049c1c1fe4f964fd078b88bedd064abea385cfebd65e563f93c12d34eb6426e8aa321033cfd8fe8855b9e74d07fe4f9d70de46f
    print("(e,n) is (", e, ", ", n, ")")

    hacked_d = hack_RSA(e, n)

    print("d is", hacked_d)


if __name__ == "__main__":
    test_hack_RSA()
