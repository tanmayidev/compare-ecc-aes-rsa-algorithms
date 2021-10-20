from timeit import timeit

if __name__ == "__main__":
    fp = open("ECCkeyGen.csv","w")
    headerKeyGen = '''
from ecies.utils import generate_eth_key
    '''
    code = '''
if __name__ == "__main__":
    key = generate_eth_key()
    '''

fp.writelines("keyGenECC(NIST-P256)\n")
keyGen = 0
for i in range(100):
    keyGen = timeit(setup=headerKeyGen, stmt=code, number=10000)
    fp.writelines(f"{keyGen}\n")
fp.close()