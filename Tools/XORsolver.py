#!/usr/bin/env python

from pwn import *
from base64 import b64decode

ciphertext = b64decode("s5qQ … gg==")

for key in range(256):
    plaintext = xor(key, ciphertext)
    if "flag{" in plaintext:
        print plaintext
