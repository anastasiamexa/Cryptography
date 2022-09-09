import gmpy2
from Crypto.Util.number import long_to_bytes

c = 44981230718212183604274785925793145442655465025264554046028251311164494127485

decrypted = long_to_bytes(c)
print(decrypted)