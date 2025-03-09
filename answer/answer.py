from pwn import *

server_ip = "127.0.0.1"
server_port = 7201

XOR_KEY = 0x19  # XOR 키값
ENCODED_SECRET = "XOR"

decoded_phrase = ''.join(chr(ord(c) ^ XOR_KEY) for c in ENCODED_SECRET)

r = remote(server_ip, server_port)

print(r.recvuntil(b": ").decode())

r.sendline(decoded_phrase.encode())

print(r.recvline().decode())

r.close()

