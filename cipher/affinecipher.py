# Program to implement Affine Cipher for encryption and decryption


#returns gcd of two numbers
def gcd(num1, num2):
    if num2 == 0:
        return num1
    return  gcd(num2, num1 % num2)


#returns the inverse of a number if it exists, else '-1', under mod
def inverse(number, mod):
    if gcd(number, mod) != 1:
        return None
    
    t1 = 0
    t2 = 1

    while number != 0:
        quotient = mod // number
        remainder = mod % number

        t = t1 - quotient*t2

        mod = number
        number = remainder

        t1 = t2
        t2 = t

    return t1


class AffineCipher:
    def __init__(self, key1, key2):
        self.key1 = key1
        self.key2 = key2
        self.keyInverse = inverse(self.key1, 26)


    #returns index of the given alphabet
    def index(self, alphabet):
        return ord(alphabet.upper()) - ord('A')


    # returns a cipher text by encrypting a plain text using affine cipher algorithm
    def encrypt(self, plainTxt):
        cipherTxt = str()

        if not self.keyInverse:
            return "INVERSE NOT FOUND!!"

        for x in plainTxt:
            if x.isalpha():
                cipherTxt  += chr((self.index(x)*self.key1 + self.key2)%26 + ord('A'))
            else:
                cipherTxt += x 

        return cipherTxt


    # returns a plain text by decrypting a plain text using additive cipher algorithm
    def decrypt(self, cipherTxt):
        plainTxt = str()

        if not self.keyInverse:
            return "INVERSE NOT FOUND!!"

        for x in cipherTxt:
            if x.isalpha():
                plainTxt  += chr(((self.index(x)-self.key2) * self.keyInverse)%26 + ord('A'))
            else:
                plainTxt += x 

        return plainTxt


if __name__ == '__main__':
    aff = AffineCipher(7,2)

    print(aff.encrypt("hello"))
    print(aff.decrypt(aff.encrypt("hello")))
    
