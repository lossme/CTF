## 查看公钥文件

```sh
# 查看公钥文件
>>> openssl rsa -pubin -in data/public.pem -text -modulus

Public-Key: (256 bit)
Modulus:
    00:a4:10:06:de:fd:37:8b:73:95:b4:e2:eb:1e:c9:
    bf:56:a6:1c:d9:c3:b5:a0:a7:35:28:52:1e:eb:2f:
    b8:17:a7
Exponent: 65537 (0x10001)
Modulus=A41006DEFD378B7395B4E2EB1EC9BF56A61CD9C3B5A0A73528521EEB2FB817A7
writing RSA key
-----BEGIN PUBLIC KEY-----
MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAKQQBt79N4tzlbTi6x7Jv1amHNnDtaCn
NShSHusvuBenAgMBAAE=
-----END PUBLIC KEY-----
```

## 查看私钥文件

```sh
>>> openssl rsa -in data/private.pem -text -modulus
Private-Key: (256 bit)
modulus:
    00:a4:10:06:de:fd:37:8b:73:95:b4:e2:eb:1e:c9:
    bf:56:a6:1c:d9:c3:b5:a0:a7:35:28:52:1e:eb:2f:
    b8:17:a7
publicExponent: 65537 (0x10001)
privateExponent:
    33:02:28:a0:bb:e9:c1:19:b6:b9:fe:b3:4b:67:3e:
    6d:9a:ac:3a:d8:14:09:69:4b:57:68:71:52:12:54:
    a2:c1
prime1:
    00:d7:db:8f:68:bc:ec:6d:76:84:b3:72:01:38:5d:
    29:8b
prime2:
    00:c2:92:a2:72:e8:33:9b:14:5d:9d:f6:74:b9:a8:
    75:d5
exponent1:
    1a:e7:f2:4b:42:e9:51:87:a9:68:d8:b8:10:37:84:
    9b
exponent2:
    23:38:55:cd:84:f8:aa:6e:b2:4f:80:a8:3a:5f:23:
    0d
coefficient:
    7a:03:84:33:ad:8d:01:60:a5:6c:3a:f1:29:63:77:
    a0
Modulus=A41006DEFD378B7395B4E2EB1EC9BF56A61CD9C3B5A0A73528521EEB2FB817A7
writing RSA key
-----BEGIN RSA PRIVATE KEY-----
MIGpAgEAAiEApBAG3v03i3OVtOLrHsm/VqYc2cO1oKc1KFIe6y+4F6cCAwEAAQIg
MwIooLvpwRm2uf6zS2c+bZqsOtgUCWlLV2hxUhJUosECEQDX249ovOxtdoSzcgE4
XSmLAhEAwpKicugzmxRdnfZ0uah11QIQGufyS0LpUYepaNi4EDeEmwIQIzhVzYT4
qm6yT4CoOl8jDQIQegOEM62NAWClbDrxKWN3oA==
-----END RSA PRIVATE KEY-----
```

## 生成私钥文件

```sh
# 生成私钥文件
# https://github.com/ius/rsatool
python rsatool.py \
    -p 286924040788547268861394901519826758027 \
    -q 258631601377848992211685134376492365269 \
    -e 65537 \
    -o private.pem
```

## 根据私钥解密enc文件

```sh
openssl rsautl -inkey private.pem -decrypt -in flag.enc
```


## 暴力分解

在线分解 http://factordb.com/index.php

- yafu

```sh
# yafu
>>> yafu-x64.exe
>>> factor(0xA41006DEFD378B7395B4E2EB1EC9BF56A61CD9C3B5A0A73528521EEB2FB817A7)
...
...
...
***factors found***

P39 = 286924040788547268861394901519826758027
P39 = 258631601377848992211685134376492365269

ans = 1

# p q 相邻比较近
>>> yafu.exe

fermat(n, pow(n, 0.5))
```

- msieve
```sh
msieve146.exe 0xA41006DEFD378B7395B4E2EB1EC9BF56A61CD9C3B5A0A73528521EEB2FB817A7
```


