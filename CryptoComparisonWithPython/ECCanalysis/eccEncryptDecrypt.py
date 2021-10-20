from timeit import timeit
if __name__ == "__main__":
    fp = open("ECCencryptDecrypt.csv","w")
    headers = '''
from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt
    '''
    code = '''
if __name__ == "__main__":
    eth_k = generate_eth_key()
    print("Ethereum Keys:")
    sk = eth_k.to_hex()
    pk = eth_k.public_key.to_hex()
    data = b"Hi Kanda"
    decrypt(sk, encrypt(pk, data))
    '''
    fp.writelines("EncryptDecryptECC(NIST-P256)\n")
    encryptDecrypt = 0
    for i in range(100):
        encryptDecrypt = timeit(setup=headers, stmt=code, number=10000)
        fp.writelines(f"{encryptDecrypt}\n")
    fp.close()