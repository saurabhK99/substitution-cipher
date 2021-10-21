# Program to implement 2 X 2 hill cipher for encryption and decryption

import numpy as np

class HillCipher:
    def __init__(self, keyList):
        self.keyMatrix = np.array([[keyList[0], keyList[1]],
                                  [keyList[2], keyList[3]]])
        
        self.keyAdjointMatrix = np.array([[keyList[3], -keyList[1]],
                                         [-keyList[2], keyList[0]]])

        self.keyDeterminant = (keyList[0]*keyList[3]
                              -keyList[2]*keyList[1])


    # returns the index of the given alphabet
    def index(self, alphabet):
        return ord(alphabet.upper()) - ord('A')


    # returns a cipher text by encrypting a plain text using hill cipher algorithm
    def encrypt(self, plainTxt):
        cipherTxt = str()

        plainTxtList = plainTxt.split()
        plainTxtMatrix = []

        # converting to numpy matrix
        prev = -1
        for word in plainTxtList:
            i=0
            temp = []
            for x in word:
                i += 1
                if prev > -1:
                    plainTxtMatrix.append([prev, self.index(x)])
                    prev = -1
                else:
                    temp.append(self.index(x))
                
                if len(temp) == 2:
                    plainTxtMatrix.append(temp)
                    temp=[]

                if i == len(word):
                    if len(temp) == 1:
                        prev = temp[0]
                        temp = []

        # adding extra character if length of plain text is odd
        if prev != -1:
            plainTxtMatrix.append([prev, self.index('x')])

        plainTxtMatrix = np.array(plainTxtMatrix)
        
        cipherTxtMatrix = plainTxtMatrix.dot(self.keyMatrix) 

        #converting to cipher text
        for list in cipherTxtMatrix:
            for x in list:
                cipherTxt += chr(x%26 + ord('A'))

        return cipherTxt


    # returns a plain text by decrypting a cipher text using hill cipher algorithm
    def decrypt(self, cipherTxt):
        plainTxt = str()

        

        cipherTxtList = cipherTxt.split()
        cipherTxtMatrix = []

        # converting to numpy matrix
        prev = -1
        for word in cipherTxtList:
            i=0
            temp = []
            for x in word:
                i += 1
                if prev > -1:
                    cipherTxtMatrix.append([prev, self.index(x)])
                    prev = -1
                else:
                    temp.append(self.index(x))
                
                if len(temp) == 2:
                    cipherTxtMatrix.append(temp)
                    temp=[]

                if i == len(word) and len(temp) == 1:
                        prev = temp[0]
                        temp = []

        # adding extra character if length of cipher text is odd
        if prev != -1:
            cipherTxtMatrix.append([prev, self.index('x')])

        cipherTxtMatrix = np.array(cipherTxtMatrix)

        plainTxtMatrix = cipherTxtMatrix.dot(self.keyAdjointMatrix) 

        for i in range(2):
            for j in range(2):
                plainTxtMatrix[i][j] = int(plainTxtMatrix[i][j])

        #converting to plain text
        for list in plainTxtMatrix:
            for x in list:
                plainTxt += chr(int(x * self.keyDeterminant)%26 + ord('A'))

        return plainTxt


if __name__ == '__main__':
    hill = HillCipher([2,3,3,4])
    print(hill.encrypt('jelly bean'))
    print(hill.decrypt('ERDZZYIMRB'))
    
    

    