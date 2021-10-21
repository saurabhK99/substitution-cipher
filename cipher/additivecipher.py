# Program to implement Additive Cipher for encryption and decryption

class AdditiveCipher:
    def __init__(self, key):
        self.key = key


    # returns the index of the given alphabet
    def index(self, alphabet):
        return ord(alphabet.upper()) - ord('A')


    # returns a cipher text by encrypting a plain text using additive cipher algorithm
    def encrypt(self, plainTxt):
        cipherTxt = str()

        for x in plainTxt:
            if x.isalpha():
                cipherTxt  += chr((self.index(x) + self.key)%26 + ord('A'))
            else:
                cipherTxt += x 

        return cipherTxt


    # returns a plain text by decrypting a cipher text using additive cipher algorithm
    def decrypt(self, cipherTxt):
        plainTxt = str()

        for x in cipherTxt:
            if x.isalpha():
                plainTxt  += chr((self.index(x) - self.key)%26 + ord('A'))
            else:
                plainTxt += x 

        return plainTxt


if __name__ == '__main__':
    add = AdditiveCipher(3)

    print(add.encrypt('hello'))
    print(add.decrypt(add.encrypt('hello')))