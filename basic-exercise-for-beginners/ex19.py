"""
- Exercise: 19: Print Alternate Prime Numbers till 20
- A Prime Number is a number that can only be divided by itself and 1 without remainders 
(e.g., 2, 3, 5, 7, 11).
"""

def main():
    prime = []
    alprime = []
    n = 0

    for i in range(2, 21):
        for j in range(1, 20):
            if i % j == 0:
                n += 1
    
        if n == 2:
            prime.append(i)
            n = 0
        else:
            n = 0

    prime = list(map(str, prime))

    for _ in range(len(prime)):
        if _ % 2 == 0:
            alprime.append(prime[_])
    
    alprime = list(map(str,alprime))

    print(f"All prime numbers from 1 to 20: {", ".join(prime)}")
    print(f"Alternate prime numbers from 1 to 20: {", ".join(alprime)}")
main()