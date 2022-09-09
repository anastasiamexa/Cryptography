import gmpy2
from Crypto.Util.number import long_to_bytes

c = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957

# using gmpy2 iroot() function to find the cubic root of c
decrypted = long_to_bytes(gmpy2.iroot(c,3)[0]) # return only the first element
# the second element of the tuple is bool, indicating if the result is exact or not.
print(decrypted)