import timeit

if __name__ == "__main__":
    
    fp = open("RSAencryptDecrypt.csv","w")

    header = '''
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
    '''

    code1024 = '''
if __name__ == "__main__":
    data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt massa ut ."
    key = RSA.generate(1024)
    privateKey = key
    publicKey = key.publickey()
    cipher = PKCS1_OAEP.new(publicKey)
    ciphertext = cipher.encrypt(data.encode())
    cipherNew = PKCS1_OAEP.new(privateKey)
    cipherNew.decrypt(ciphertext)
    '''
    
    code2048 = '''
if __name__ == "__main__":
    data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt massa ut ."
    key = RSA.generate(2048)
    privateKey = key
    publicKey = key.publickey()
    cipher = PKCS1_OAEP.new(publicKey)
    ciphertext = cipher.encrypt(data.encode())
    cipherNew = PKCS1_OAEP.new(privateKey)
    cipherNew.decrypt(ciphertext)
    '''
    
    code3072 = '''
if __name__ == "__main__":
    data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt massa ut ."
    key = RSA.generate(3072)
    privateKey = key
    publicKey = key.publickey()
    cipher = PKCS1_OAEP.new(publicKey)
    ciphertext = cipher.encrypt(data.encode())
    cipherNew = PKCS1_OAEP.new(privateKey)
    cipherNew.decrypt(ciphertext)
    '''

fp.writelines("EncryptDecryptRSA(1024),EncryptDecryptRSA(2048),EncryptDecryptRSA(3072)\n")
encryptDecrypt1024 = 0
encryptDecrypt2048 = 0
encryptDecrypt3072 = 0
for i in range(100):
    encryptDecrypt1024 = timeit.timeit(setup=header, stmt=code1024, number=10000)
    encryptDecrypt2048 = timeit.timeit(setup=header, stmt=code2048, number=10000)
    encryptDecrypt3072 = timeit.timeit(setup=header, stmt=code3072, number=10000)
    fp.writelines(f"{encryptDecrypt1024},{encryptDecrypt2048},{encryptDecrypt3072}\n")
fp.close()