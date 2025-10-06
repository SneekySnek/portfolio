# Course name: Intro to Security 2025
# Student name and id: Bror Hansen, broh
# Date: 06/10/25
# Part 2: modify an intercepted ElGamal ciphertext so it decrypts to a chosen

# Known stuff:
# The public shared base g = 42
# The public shared prime p = 29837
# System’s public key PK = gx mod p = 22690
# You intercept one of these encrypted messages:
# c1 = 23447
# c2 = 8372


p = 29837
g = 42
PK = 22690
c1 = 23447
c2 = 8372

original_student_number = 26000  # From part 1
my_student_number = 111111      # chosen random student number

# Reduce both values modulo p (safe habit)
orig = original_student_number % p
target = my_student_number % p

# Compute multiplier t = target * orig^{-1} (mod p)
# Then c2' = c2 * t (mod p) will decrypt to target
factor = (target * pow(orig, p - 2, p)) % p
c2_new = (c2 * factor) % p

print("Modified ciphertext: c1 =", c1, ", c2 =", c2_new)

#taken from part_1
def decrypt (c1,c2,p):
    x = 24774
    s_inverse = pow(c1, -x, p)
    s_number = (c2 * s_inverse) % p
    return s_number


#Results using decrypt function from part_1 to compare.
decrypted = decrypt(c1, c2_new, p)
print("(verification) server would decrypt modified ciphertext to (mod p) =", decrypted)
print("(verification) desired target (mod p) =", target)