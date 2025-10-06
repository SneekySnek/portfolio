# Course name: Intro to Security 2025
# Student name and id: Bror Hansen, broh
# Date: 06/10/26
# Part 1
#
# Known stuff:
# The public shared base g = 42
# The public shared prime p = 29837
# System’s public key PK = gx mod p = 22690
# You intercept one of these encrypted messages:
# c1 = 23447
# c2 = 8372

PK = 22690 # g^x mod p
g = 42
p = 29837
c1 = 23447
c2 = 8372

def private_key (p,g,PK):
    acc = g % p
    x = 1
    while acc != PK:
        x += 1
        acc = (acc * g) % p

    print("Private key x =", x)
    return x

def decrypt (c1,c2,x,p):
    sharedSecret = pow(c1,x,p)
    s_inverse = pow(sharedSecret, p - 2, p)
    s_number = (c2 * s_inverse) % p
    print("Decrypted student number =", s_number)
    return s_number


#Find the private key x
priv_key = private_key(p,g,PK)
#Decrypited student number
decrypt(c1,c2,priv_key,p)

 