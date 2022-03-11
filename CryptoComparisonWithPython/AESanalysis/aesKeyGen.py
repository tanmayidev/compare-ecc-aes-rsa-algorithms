import timeit

if __name__ == "__main__":
    fp = open("AESkeyGen_new.csv","w")
    headerKeyGen = '''
from Crypto.Random import get_random_bytes
    '''
    code16 = '''
if __name__ == "__main__":
    key = get_random_bytes(16)
    '''
    code24 = '''
if __name__ == "__main__":
    key = get_random_bytes(24)
    '''
    code32 = '''
if __name__ == "__main__":
    key = get_random_bytes(32)
    '''

fp.writelines("keyGenAES(128),keyGenAES(192),keyGenAES(256)\n")
keyGen128 = 0
keyGen192 = 0
keyGen256 = 0
for i in range(100):
    keyGen128 = timeit.timeit(setup=headerKeyGen, stmt=code16, number=10000)
    keyGen192 = timeit.timeit(setup=headerKeyGen, stmt=code24, number=10000)
    keyGen256 = timeit.timeit(setup=headerKeyGen, stmt=code32, number=10000)
    fp.writelines(f"{keyGen128},{keyGen192},{keyGen256}\n")
fp.close()