# from Crypto.Cipher import AES
# import timeit


# if __name__ == "__main__":
#     fp = open("AESencrypt.csv","w")
#     headerEncrypt = '''
# from Crypto.Random import get_random_bytes
import timeit

if __name__ == "__main__":
    
    fp = open("AESencryptDecrypt.csv","w")

    header = '''
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
    '''

    code16 = '''
if __name__ == "__main__":
    data = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt massa ut tellus lobortis blandit id et neque. Nam in consectetur ante, ut cras amet."
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext = cipher.encrypt(data)
    cipherNew = AES.new(key, AES.MODE_EAX,cipher.nonce)
    cipherNew.decrypt(ciphertext)
    '''
    
    code24 = '''
if __name__ == "__main__":
    data = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt massa ut tellus lobortis blandit id et neque. Nam in consectetur ante, ut cras amet."
    key = get_random_bytes(24)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext = cipher.encrypt(data)
    cipherNew = AES.new(key, AES.MODE_EAX,cipher.nonce)
    cipherNew.decrypt(ciphertext)
    '''
    
    code32 = '''
if __name__ == "__main__":
    data = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent tincidunt massa ut tellus lobortis blandit id et neque. Nam in consectetur ante, ut cras amet."
    key = get_random_bytes(32)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext = cipher.encrypt(data)
    cipherNew = AES.new(key, AES.MODE_EAX,cipher.nonce)
    cipherNew.decrypt(ciphertext)
    '''

fp.writelines("EncryptDecrypt(128),EncryptDecrypt(192),EncryptDecrypt(256)\n")
encryptDecrypt128 = 0
encryptDecrypt192 = 0
encryptDecrypt256 = 0
for i in range(100):
    encryptDecrypt128 = timeit.timeit(setup=header, stmt=code16, number=10000)
    encryptDecrypt192 = timeit.timeit(setup=header, stmt=code24, number=10000)
    encryptDecrypt256 = timeit.timeit(setup=header, stmt=code32, number=10000)
    fp.writelines(f"{encryptDecrypt128},{encryptDecrypt192},{encryptDecrypt256}\n")
fp.close()
