from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def aeskeyGenerator():
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    return cipher


if __name__ == "__main__":
    print(aeskeyGenerator)