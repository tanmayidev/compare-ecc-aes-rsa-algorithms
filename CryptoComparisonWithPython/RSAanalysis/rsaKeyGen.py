import timeit

if __name__ == "__main__":
    fp = open("RSAkeyGen.csv","w")
    headerKeyGen = '''
from Crypto.PublicKey import RSA
    '''
    code1024 = '''
if __name__ == "__main__":
    key = RSA.generate(1024)
    '''
    code2048 = '''
if __name__ == "__main__":
    key = RSA.generate(2048)
    '''
    code3072 = '''
if __name__ == "__main__":
    key = RSA.generate(3072)
    '''

fp.writelines("keyGenRSA(1024),keyGenRSA(2048),keyGenRSA(3072)\n")
keyGen1024 = 0
keyGen2048 = 0
keyGen3072 = 0
for i in range(100):
    keyGen1024 = timeit.timeit(setup=headerKeyGen, stmt=code1024, number=10000)
    keyGen2048 = timeit.timeit(setup=headerKeyGen, stmt=code2048, number=10000)
    keyGen3072 = timeit.timeit(setup=headerKeyGen, stmt=code3072, number=10000)
    fp.writelines(f"{keyGen1024},{keyGen2048},{keyGen3072}\n")
fp.close()