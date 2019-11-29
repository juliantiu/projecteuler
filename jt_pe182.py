# !/usr/local/bin/python3

""" 
Julian Tiu
Project Euler #182

Running (assuming python v 3.7.x):
    $ python jt_pe182.py

Answer:
    399788195976

Why I chose this problem:
    I took a cryptography class to satisfy my cybersecurity minor, and we learned how the RSA
    encryption scheme worked. Since this problem involves RSA encryption, I thought it was 
    fitting to attempt.

Quick Summary:
    In RSA encryption, the ciphertext, c, can be calculated with c = m^e mod n where e is any
    number within [1, phi] and gcd(e, phi) = 1, where phi is (p-1)*(q-1). In my aglorithm, 
    for each e that satisfies gcd(e, phi) = 1 and (gcd(e-1, p-1) + 1) * (gcd(e-1, q-1) + 1) < 10, 
    sum this e with the previous candidate e's. Why (gcd(e-1, p-1) + 1) * (gcd(e-1, q-1) + 1) < 10 ? 
    Refer to the NOTES.


######################################### NOTES

My initial design calculated for all 
possible c = m^e mod n where c = m, and out of
all e's from [1, phi-1], figure out a minimum 
threshold of the amount of c = m. This required 
three nested loops. I thought this to be too long
to compute for a typical Project Euler problem. 

Unfortunately, RSA unconcealed messages were
not covered in my cryptography textbook, but
further research led me to these resources:

- Recent Advances in RSA Cryptography by Stefan Katzenbeisser (p. 69)
- https://www.youtube.com/watch?v=_rgobarnEOs (26:45)

A lemma states that:
"The number of fixed points of the RSA
permutation, i.e. elements x exists in Zn
is the product of two primes p and q and 
gcd(e, phi) = 1 satisfying x^e mod n, is
given by 
p(e,n) = (gcd(e-1, p-1)+1) * (gcd(e-1, q-1)+1)"

Furthermore the text states that since p-1 and
q-1 and e-1 are all even, the number of unconcealed
messages is at least 9.

Therefore a "minimum" threshold for unconcealed 
messages in the problem statement should be 9 if 
all e's would produce at least 9 unconcealed 
messages.

Therefore:
(gcd(e-1, p-1) + 1) * (gcd(e-1, q-1) + 1) < 10

############################################"""

# GCD calculation by Euclidean method
def gcd(quotient, remainder):
    while(remainder):
        quotient, remainder = remainder, quotient % remainder
    return quotient

# returns the sum of e's that generate the minimum unconcealed messages
def sumE():
    # p, q, and phi are given in the problem statement
    p = 1009 
    q = 3643
    phi = (p-1) * (q-1)
    sumOfEs = 0

    for e in range(1, phi):
        numUnconcealedMessages = (gcd(e-1, p-1) + 1) * (gcd(e-1, q-1) + 1)
        if (gcd(e, phi) == 1) and (numUnconcealedMessages < 10):
            sumOfEs += e
    
    return sumOfEs

if __name__ == "__main__":
    print(sumE())