from math import gcd
def euqlid(n, m):
    while n!=0 and m !=0:
        if(n>m):
            n %= m
        else:
            m %= n
    return n+m

def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean_algorithm(b, a % b)
    return gcd, y, x - (a // b) * y


def encrypt(message, e, n):
    return pow(message, e, n)


def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)


p = 94483
q = 41521
n = p * q
m = (p - 1) * (q - 1)
e = []


for i in range(2, 10000):
    if gcd(i, m) == 1:
        print(i)
        e.append(i)

e = int(input("Выберите желаемый e: "))
k = euqlid(p - 1, q - 1)

d = pow(e, -1, m)
print("d = " + str(d))

d1 = int(d % (m / k))
print("d1 = " + str(d1))
M = 1032022

ciphertext = encrypt(M, e, n)
decrypted_message = decrypt(ciphertext, d1, n)

print("Ciphertext:", ciphertext)
print("Decrypted message:", decrypted_message)