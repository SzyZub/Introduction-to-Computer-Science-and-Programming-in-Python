

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
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

def get_story_string():
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'ps4/words.txt'
class Message(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    def get_message_text(self):
        return self.message_text
    def get_valid_words(self):
        self.copy = self.valid_words.copy()
        return self.copy
    def build_shift_dict(self, shift):
        low = string.ascii_lowercase
        high = string.ascii_uppercase
        lowdict = dict()
        highdict = dict()
        for i in range(len(low)):
            lowdict[low[i]] = low[(i + shift)%26]
            highdict[high[i]] = high[(i + shift)%26]
        lowdict.update(highdict)
        return lowdict

    def apply_shift(self, shift):
        newstr = list()
        lett = self.build_shift_dict(shift)
        text = self.get_message_text()
        for i in range(len(text)):
            if text[i] in lett:
                newstr.append(lett[text[i]])
            else:
                newstr.append(text[i])
        return "".join(newstr)

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)
    def get_shift(self):
        return self.shift

    def get_encryption_dict(self):
        newdict = self.encryption_dict.copy()
        return newdict
    
    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    def change_shift(self, shift):
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(shift)
        self.message_text_encrypted = Message.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self, text)

    def decrypt_message(self):
        bestshift = [0, 0, 0]
        shift = 0
        while shift < 26:
            bestshift[0] = 0
            newword = Message.apply_shift(self, shift)
            check = newword.split()
            for i in check:
                if is_word(Message.get_valid_words(self), i):
                    bestshift[0] += 1
            if bestshift[0] > bestshift[1]:
                bestshift[1] = bestshift[0]
                bestshift[2] = shift
            shift += 1
        return (bestshift[2], Message.apply_shift(self, bestshift[2]))

if __name__ == '__main__':

    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
