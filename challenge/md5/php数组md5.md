```php
if($_POST['param1']!==$_POST['param2'] && md5($_POST['param1'])===md5($_POST['param2'])){
        die("success!");
    }
```



php md5传入数组会回相同的md5值
payload
```
param1[]=1&param2[]=2
```
