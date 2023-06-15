
import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):   
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    return wordlist

def is_word(word_list, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'ps4/words.txt'
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    def get_message_text(self):
        return self.message_text
    
    def get_valid_words(self):
        copy = self.valid_words.copy()
        return copy 
    
    def build_transpose_dict(self, vowels_permutation):
        dic = dict()
        for i in range(len(vowels_permutation)):
            dic[VOWELS_LOWER[i]] = vowels_permutation[i]
            dic[VOWELS_UPPER[i]] = vowels_permutation[i].upper()
        for i in range(len(CONSONANTS_LOWER)):
            dic[CONSONANTS_LOWER] = CONSONANTS_LOWER[i]
            dic[CONSONANTS_UPPER] = CONSONANTS_UPPER[i]
        return dic

    
    def apply_transpose(self, transpose_dict):
        newstr = list()
        text = self.get_message_text()
        for i in range(len(text)):
            if text[i] in transpose_dict:
                newstr.append(transpose_dict[text[i]])
            else:
                newstr.append(text[i])
        return "".join(newstr) 
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        perlist = get_permutations(VOWELS_LOWER)
        bestshift = [0, 0, ""]
        for i in perlist:
            bestshift[0] = 0
            dic = SubMessage.build_transpose_dict(self, i)
            tempstr = SubMessage.apply_transpose(self, dic)
            check = tempstr.split()
            for j in check:
                if is_word(SubMessage.get_valid_words(self), j): 
                    bestshift[0] += 1
            if bestshift[0] > bestshift[1]:
                bestshift[1] = bestshift[0]
                bestshift[2] = i
        return SubMessage.apply_transpose(self, SubMessage.build_transpose_dict(self, bestshift[2]))



if __name__ == '__main__':

    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
