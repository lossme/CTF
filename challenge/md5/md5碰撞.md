```python

import hashlib

def md5(s):
    return

a = "4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa200a8284bf36e8e4b55b35f427593d849676da0d1555d8360fb5f07fea2"
b = "4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa202a8284bf36e8e4b55b35f427593d849676da0d1d55d8360fb5f07fea2"


# 008ee33a9d58b51cfeb425b0959121c9
hashlib.md5(bytes.fromhex(a)).hexdigest()

# 008ee33a9d58b51cfeb425b0959121c9
hashlib.md5(bytes.fromhex(b)).hexdigest()
```

