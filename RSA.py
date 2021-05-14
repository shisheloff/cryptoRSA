import random

# def encrypt(message or File):
# def decrypt(message or File):
# def sign(File):
# def verify(File):
# def isPrime(num):

first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]


def nBitRandom(n):
    return random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)


def getLowLevelPrime(n):
    while True:
        pc = nBitRandom(n)
        for divisor in first_primes_list:
            if pc % divisor == 0 and divisor ** 2 <= pc:
                break
            else:
                return pc


def millerRabinAlg(mra):
    maxDivisionByTwo = 0
    ec = mra - 1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionByTwo += 1
        assert (2 ** maxDivisionByTwo * ec == mra - 1)

        def trialComposite(roundTester):
            if pow(roundTester, ec, mra) == 1:
                return False
            for i in range(maxDivisionByTwo):
                if pow(roundTester, 2 ** i * ec, mra) == mra - 1:
                    return False

        numberOfRabinTrials = 20
        for i in range(numberOfRabinTrials):
            round_tester = random.randrange(2, mra)
            if trialComposite(round_tester):
                return False
            return True


def getPrimeNumber():
    primeCandidate = getLowLevelPrime(1024)
    while True:
        if not millerRabinAlg(primeCandidate):
            continue
        else:
            return primeCandidate


def getKey():
    firstPrimeNum = getPrimeNumber()
    secondPrimeNum = getPrimeNumber()
    n = firstPrimeNum * secondPrimeNum
    phi = (firstPrimeNum - 1) * (secondPrimeNum - 1)
