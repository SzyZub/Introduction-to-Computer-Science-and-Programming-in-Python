# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
   '*': 0 ,'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "PS3/words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.
    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 
	The score for a word is the product of two components:
	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played
	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
    word: string
    n: int >= 0
    returns: int >= 0
    """
    score = 0
    wordlen = 0
    ans = list(word.lower())
    for key, points in SCRABBLE_LETTER_VALUES.items():
        for i in ans:
            if key == i:
                score = score + points
    for i in ans:
        wordlen = wordlen + 1
    if (7*wordlen - 3*(n-wordlen)) > 1:
        score = score * (7 * wordlen - 3*(n-wordlen))
    return score
    

    
    
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line


def deal_hand(n):

    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    hand["*"] = 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand


def update_hand(hand, word):

    new_hand = hand.copy()
    for i in word.lower():
        if i in new_hand.keys():
            if new_hand[i] > 0: 
                new_hand[i] -= 1
            else:
                new_hand[i] = 0

    return new_hand  

def is_valid_word(word, hand, word_list):

    length = True
    inlist = False
    dictionary = {}

    if "*" in word:
        post = word.find("*")
        newword = list(word)
        for i in VOWELS:
            cond = 1
            newword[post] = i
            word ="".join(newword)
            if word.lower() in word_list:
                inlist = True
            
            for i in word.lower():
                if i in dictionary.keys():
                    dictionary[i] += 1
                else:
                    dictionary[i] = 1
        
            for x in dictionary.keys():
                if hand.get(x) == None or dictionary[x] > hand.get(x):
                    if cond == 1:
                        continue
                    length = False
    
            if inlist == True and length == True:
                return True
    else:
        if word.lower() in word_list:
            inlist = True
            
        for i in word.lower():
            if i in dictionary.keys():
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        
        for x in dictionary.keys():
            if hand.get(x) == None or dictionary[x] > hand.get(x):
                length = False
    
        if inlist == True and length == True:
            return True
        else:
            return False
    return False
            
def calculate_handlen(hand):

    count = 0
    for i in hand:
        count += 1
    return count


def play_hand(hand, word_list):  
    score = 0
    while True:
        if calculate_handlen(hand) > 0:
            display_hand(hand)
            inp = input("Enter word, or '!!' to indicate that you are finished: ")
            if inp == "!!":
                break
            if is_valid_word(inp, hand, word_list):
                print("You have earned:", get_word_score(inp, calculate_handlen(hand)), "points")
                score = score + get_word_score(inp, calculate_handlen(hand))
                print("Your total score is:", score, "\n")
            else:
                print("Invalid word\n")
            hand = update_hand(hand, inp)       
    print("You have earned:", score, "points!")
    return score

def substitute_hand(hand, letter):
    newhand = hand.copy()
    if not letter in hand:
        return hand 
    value = hand[letter]
    newhand.pop(letter)
    choices = VOWELS + CONSONANTS - newhand.keys()
    choices ="".join(choices)
    let = random.choice(choices)
    newhand[let] = value
    return newhand

       
    
def play_game(word_list):
    num = int(input("Please enter the number of hands you want to play: "))
    total_score = 0
    handsize = 7
    allow = 1
    temp = 0
    for i in range(0, num):
        allowance = 1
        hand = deal_hand(handsize)
        print("\nYour hand is:")
        display_hand(hand)
        while True:
            if allowance == 1:
                subs = input("\nIf you want to substitute a certain letter for a different random one please enter the letter, if not enter 'no': ")
                if not subs == "no":
                    allowance -= 1
                hand = substitute_hand(hand, subs)
            print("\nRound starting!")
            temp = total_score
            total_score = total_score + play_hand(hand, word_list)   
            if allow == 1:
                ans = input("\nDo you want to replay the previous hand? Answer 'yes' or 'no': ")
                if ans == "yes":
                    total_score = temp + play_hand(hand,word_list)
                    allow -=1
            break
    print("\nIn the whole game you have earned:", total_score, "points!")
    return total_score

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
