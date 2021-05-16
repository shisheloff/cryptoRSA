import hashlib
import random

# def encrypt(message or File):
# def decrypt(message or File):
# def sign(File):
# def verify(File):

first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]


def extended_gcd(a, b):
    y, x = (1, 0)
    real, imagine = (1, 0)
    a_start, b_start = a, b

    while b:
        q = a // b
        a, b = b, (a % b)

        real, x = x, (real - (q * x))
        imagine, y = y, (imagine - (q * y))

    if real < 0:
        real += b_start
    if imagine < 0:
        imagine += a_start
    return real, imagine, a


def find_d(e, p, q):
    x = extended_gcd(e, ((p - 1) * (q - 1)))
    if x[2] == 1:
        return x[1] % ((p - 1) * (q - 1))
    else:
        return "Pick for e not valid"


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
    e = 65537
    d = find_d(e, firstPrimeNum, secondPrimeNum)
    while d < 0:
        d += phi
    publicKey = [e, n]
    privateKey = [d, n]
    pk = open('pk', 'w')
    for i in publicKey:
        pk.write("%s\n" % i)
    pb = open('pb', 'w')
    for i in privateKey:
        pb.write("%s\n" % i)
    pk.close()
    pb.close()


def hexToInt(x):
    return eval("0x" + x)


def encrypt(msg, publicKeyFile):
    pk = open(publicKeyFile, 'r')                                          # открытие файла с октрытым ключом
    msg = hashlib.sha256(msg.encode('utf-8')).hexdigest().upper() # получение хеша сообщения
    msg = hexToInt(msg)
