from Crypto.Util.number import getPrime, bytes_to_long
from Crypto.PublicKey import RSA
from secret import  getNextPrime

p = getPrime(1024)
print(p)
q = getNextPrime(p)
print(q)
n = p * q
print(n)
e = 65537

# key = RSA.construct((n, e)).export_key().decode()

# with open("key", "w") as f:
#     f.write(key)

# m = bytes_to_long(flag.encode())
# c = pow(m, e, n)
# print(f"c = {c}")
