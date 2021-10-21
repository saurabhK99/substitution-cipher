#Performs letter frequency attack

class LetterFrequencyAttack:
    letterPrecedence = ['e', 't', 'a', 'o',
                        'i', 'n', 's', 'h',
                        'r', 'd', 'l', 'c',
                        'u', 'm', 'w', 'f',
                        'g', 'y', 'p', 'b',
                        'v', 'k', 'j', 'q',
                        'x', 'z'] 

    def __init__(self, cipherTxt, on='MONOALPHABETIC_CIPHER'):
        self.cipherTxt = cipherTxt.upper()
        self.on = on
        self.at = 0
        self.frequencies = self.count()


    # returns the next letter with highest frequency
    def findNextMax(self):
        max = [None, 0]

        for key in self.frequencies:
            if self.frequencies[key] > max[1]:
                max[0] = key
                max[1] = self.frequencies[key]

        if  len(self.frequencies):
            self.frequencies.pop(max[0])
        
        else:
            self.frequencies = self.count()
            self.at += 1

        return max


    # returns a dictonary with the frequencies of each letter in the cipher text
    def count(self):
        freq = {}

        for x in self.cipherTxt:
            if x.isalpha():
                if x not in freq:
                    freq[x] = 1
                else:
                    freq[x] += 1 

        return freq


    #returns a possible plain text for the corresponding cipher text
    def attack(self):
        plainTxt = str()


        #if text is encrypted with additive cipher
        if self.on == 'ADDITIVE_CIPHER':
            max = self.findNextMax()
            key = (ord(max[0]) - ord(LetterFrequencyAttack.letterPrecedence[self.at].upper()))%26
            plainTxt = self.additiveDecrypt(self.cipherTxt, key)
            
        else: 
            plainTxt = self.decrypt()

        return plainTxt

    # returns a plain text by decrypting a cipher text using additive cipher algorithm
    def additiveDecrypt(self, cipherTxt, key):
        plainTxt = str()

        for x in cipherTxt:
            if x.isalpha():
                plainTxt  += chr((ord(x) - ord('A') - key)%26 + ord('A'))
            else:
                plainTxt += x 

        return plainTxt

    # tries a subset of the permutation of mapping of letters
    def decrypt(self):
        plainTxt = self.cipherTxt
            
        self.frequencies = self.count()

        while len(self.frequencies):
            [max,_] = self.findNextMax()
            plainTxt = plainTxt.replace(max, LetterFrequencyAttack.letterPrecedence[self.at])   
            self.at = (self.at+1) % 26
                
        return plainTxt