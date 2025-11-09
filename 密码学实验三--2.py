import random
from math import gcd
from sympy import mod_inverse

def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

def generate_large_prime(bits=16):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num): return num

def generate_rsa_keys(bits=16):
    while True:
        p = generate_large_prime(bits)
        q = generate_large_prime(bits)
        while p == q: q = generate_large_prime(bits)
        n = p * q
        phi_n = (p-1) * (q-1)
        e = 3
        if gcd(e, phi_n) == 1: break
    d = mod_inverse(e, phi_n)
    return (e, n), (d, n)

def encrypt(m, pub_key):
    e, n = pub_key
    return [pow(ord(char), e, n) for char in m]

def decrypt(c, priv_key):
    d, n = priv_key
    return ''.join(chr(pow(char, d, n)) for char in c)

def rsa_test():
    pub_key, priv_key = generate_rsa_keys(bits=16)
    print("Public key:", pub_key)
    print("Private key:", priv_key)
    message = "Hello, RSA!"
    encrypted = encrypt(message, pub_key)
    print("Ciphertext:", encrypted)
    decrypted = decrypt(encrypted, priv_key)
    print("Plaintext:", decrypted)

rsa_test()