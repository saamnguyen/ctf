from random import choices
import string
from Crypto.Random import get_random_bytes

chars = string.ascii_uppercase
print(chars)
s = ''.join(choices(chars, k=16))
key = get_random_bytes(16)
print(key)
print(s)

msg = f"Welcome Hackers, this cryptosystem is under construction, can you please decrypt the 's' for me {s}."
print(msg.encode())

_nonce = bytes.fromhex(input("Your nonce: "))
print(_nonce)
print(len(_nonce))
_nonce = _nonce + bytes(20 - len(_nonce))
print(_nonce)
_ct = bytes.fromhex(input("Your ciphertext: "))
print(_ct)
