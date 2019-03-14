## wifi抓包解包

[A记录](http://www.shiyanbar.com/ctf/1853)


```sh
>>> aircrack-ng shipin.cap
Opening shipin.cap
Read 16664 packets.

   #  BSSID              ESSID                     Encryption

   1  00:1D:0F:5D:D0:EE  0719                      WPA (1 handshake)

Choosing first network as target.

Opening shipin.cap
Please specify a dictionary (option -w).


Quitting aircrack-ng...

```

可以看到这里是`wpa`加密，`bssid=00:1D:0F:5D:D0:EE`，`essid=0719`

开始破解

```sh
# 字典 https://github.com/rootphantomer/Blasting_dictionary
>>> aircrack-ng shipin.cap -w 常用密码.txt
Opening shipin.cap
Read 16664 packets.

   #  BSSID              ESSID                     Encryption

   1  00:1D:0F:5D:D0:EE  0719                      WPA (1 handshake)

Choosing first network as target.

Opening shipin.cap
Reading packets, please wait...

                                 Aircrack-ng 1.2 beta3


                   [00:00:00] 20 keys tested (671.48 k/s)


                           KEY FOUND! [ 88888888 ]


      Master Key     : B4 30 38 0F 24 7B 57 AC DE B5 3A 7F 2E FE 6B 45
                       0B 34 02 C3 89 F9 69 D5 B7 35 87 1B FB 4C EE 7F

      Transient Key  : 17 AE 23 D0 69 7C 0D 45 2B 40 F6 7D 06 C9 C5 6F
                       25 F0 B0 48 7A 6C 22 7C E2 73 50 71 46 FE 5D 0C
                       8F 59 01 BE 66 56 DF 1E 58 DD 34 DB BF A7 2D FD
                       2C 53 11 7F B2 E5 F0 16 7F 57 F5 6A 04 36 F5 71

      EAPOL HMAC     : 75 19 C5 F3 3E 33 58 23 CA 4B A1 85 FB 46 C0 2A

```

有了密码之后，开始解包

```sh
>>> airdecap-ng shipin.cap -p 88888888 -e0719
Total number of packets read         16664
Total number of WEP data packets         0
Total number of WPA data packets        27
Number of plaintext data packets         0
Number of decrypted WEP  packets         0
Number of corrupted WEP  packets         0
Number of decrypted WPA  packets        16

>>> ls
shipin.cap  shipin-dec.cap  常用密码.txt
```

得到`shipin-dec.cap`就可以用`wireshark`进行分析了
