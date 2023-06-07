import random
import string

WORDLIST_FILENAME = "Ps2/words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.\n")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()

def get_guessed_word(secret_word, letters_guessed):
    ans = ""  
    for i in secret_word:
      cond = False
      for j in letters_guessed:
        if j == i:
          ans = ans + j
          cond = True
      if not cond: ans = ans + "_ "
    return ans

def get_available_letters(letters_guessed):
    
    ans = []
    for i in string.ascii_lowercase:
      ans.append(i)
    for j in letters_guessed:
      ans.remove(j)
    return ans

def count_letters(secret_word):
    ans = 0
    for i in secret_word:
        ans = ans + 1
    return ans   
    

def hangman(secret_word):
    vowels = "aeiou"
    guess_num = 6
    letters_guessed = ""
    print("The word has:", count_letters(secret_word), "letters")
    while guess_num > 0:
      cond = False
      cont = False
      vow = False
      print("You have:", guess_num, "guesses")
      print("Available letters:", get_available_letters(letters_guessed))
      guess = input("Press enter a letter to guess:")
      if not guess.isalpha():
         print("You haven't entered a letter\n")
         print(get_guessed_word(secret_word, letters_guessed))
         print("------------------------------")
         continue
      for i in letters_guessed:
         if guess.lower() == i:
            cont = True
      if cont == True:
         guess_num = guess_num - 1
         print("You have already guessed this lettter\n")
         print(get_guessed_word(secret_word, letters_guessed))
         print("------------------------------")
         continue 
      for i in secret_word:         
          if guess.lower() == i:
              print("You have guessed a letter!")
              letters_guessed = letters_guessed + guess 
              cond = True
              break
      if cond == False:
          print("You have guessed a wrong letter!")
          for i in vowels:
              if guess.lower() == i:
                  vow = True
          if vow == False:
              guess_num = guess_num - 1
          else:
              guess_num = guess_num - 2
      if secret_word == get_guessed_word(secret_word, letters_guessed):
         print("\nYou have won!")
         break
      print(get_guessed_word(secret_word, letters_guessed))
      print("------------------------------\n")
    if guess_num <= 0:
       print("You have lost! The word was:", secret_word)


def match_with_gaps(letters_guessed, secret_word, words):
    temp = list(get_guessed_word(secret_word, letters_guessed).replace(" ", ""))
    lst = list(words)
    if not len(lst) == len(temp):
       return False
    for i in range(0, len(temp)):
       if temp[i] == "_":
          lst[i] = "_"
    if lst == temp:
       return True 
    else:
       return False
       



def show_possible_matches(letters_guessed, secret_word):
    hint_list = []
    for word in wordlist:
       if match_with_gaps(letters_guessed,secret_word, word):
          hint_list.append(word)
    return hint_list


def hangman_with_hints(secret_word):
    vowels = "aeiou"
    guess_num = 6
    letters_guessed = ""
    print("The word has:", count_letters(secret_word), "letters")
    while guess_num > 0:
      cond = False
      cont = False
      vow = False
      print("You have:", guess_num, "guesses")
      print("Available letters:", get_available_letters(letters_guessed))
      guess = input("Please enter a letter to guess or a * to get a hint:")
      if guess == "*":
         print("The matching words are:")
         print(show_possible_matches(letters_guessed, secret_word))
         print(get_guessed_word(secret_word, letters_guessed))
         print("------------------------------")
         continue
      if not guess.isalpha():
         print("You haven't entered a letter\n")
         print(get_guessed_word(secret_word, letters_guessed))
         print("------------------------------")
         continue
      for i in letters_guessed:
         if guess.lower() == i:
            cont = True
      if cont == True:
         guess_num = guess_num - 1
         print("You have already guessed this lettter\n")
         print(get_guessed_word(secret_word, letters_guessed))
         print("------------------------------")
         continue 
      for i in secret_word:         
          if guess.lower() == i:
              print("You have guessed a letter!")
              letters_guessed = letters_guessed + guess 
              cond = True
              break
      if cond == False:
          print("You have guessed a wrong letter!")
          for i in vowels:
              if guess.lower() == i:
                  vow = True
          if vow == False:
              guess_num = guess_num - 1
          else:
              guess_num = guess_num - 2
      if secret_word == get_guessed_word(secret_word, letters_guessed):
         print("\nYou have won!")
         break
      print(get_guessed_word(secret_word, letters_guessed))
      print("------------------------------\n")
    if guess_num <= 0:
       print("You have lost! The word was:", secret_word)

if __name__ == "__main__":

    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
