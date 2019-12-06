from random import randint
from hashlib import sha256
import time

def is_Prime(num):
	if num > 1:
	   for i in range(2,num):
	       if (num % i) == 0:
	           return False
	           break
	   else:
	       return True
	else:
	   return False

def randomPrimP_InRange(starFrom, endAt):
	while True:
		prime = randint(starFrom, endAt)
		if is_Prime(prime) == True:
			return prime
	return 0

def randomPrimQ_InRange(starFrom, endAt, p):

	while True:
		prime = randint(starFrom, endAt)
		if is_Prime(prime) == True and prime != p and (prime - p >= 1000 or p - prime >= 1000):
			return prime
	return 0

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

def encry(message, n, e):
	m = message % n
	return (m**e) % n

def decry(cipher, n, d):
	c = cipher % n
	return (c**d) % n

def hashFunction(message):
    hashed = sha256(message.encode("UTF-8")).hexdigest()
    return hashed
start = time.time()

p = 4019#randomPrimP_InRange(1000, 4999)
q = 8009#randomPrimQ_InRange(1000, 4999, p)
n = p * q
phi = (p - 1) * (q - 1)

e = 1
for x in range(2, phi):
  if (gcd(x, phi) == 1):
  	e = x
  	break

d = 1
for y in range(2, phi):
  if ((e*y)%phi  == 1):
  	d = y
  	break
message = "Hello"

hashed = hashFunction(message)

cipher = [None] * len(message)

for z in range(len(message)):
  cipher[z] = encry(ord(message[z]), n, e)

private_key = (n, e)
public_key = (n, d)
print ("p:", p)
print ("q:", q)
print ("n:", n)
print ("phi:", phi)
print ("e:", e)
print ("d:", d)
print ("public key:", private_key)
print ("private key:", public_key)
print ("message:", message)
print ("cipher message:" )
for q in range(len(cipher)): 
    print cipher[q]

print "Encrypting..."

message_decrypted = ""
for a in range(len(cipher)):
  message_decrypted = message_decrypted + chr(decry(cipher[a], n, d))
  print message_decrypted

print ("message decrypted:", message_decrypted)

end = time.time()
print (end - start)



