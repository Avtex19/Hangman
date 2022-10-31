from random import randint


def displayIntro():
    print('''_______________________________________________
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
_______________________________________________
_____________________Rules_____________________
Try to guess the hidden word one letter at a   
time. The number of dashes are equivalent to   
the number of letters in the word. If a player 
suggests a letter that occurs in the word,     
blank places containing this character will be 
filled with that letter. If the word does not  
contain the suggested letter, one new element  
of a hangman’s gallow is painted. As the game  
progresses, a segment of a victim is added for 
every suggested letter not in the word. Goal is
to guess the word before the man hangs!        
_______________________________________________''')


def displayEnd(result):
    if result:
        print('''________________________________________________________________________
          _                                  _                          
         (_)                                (_)                         
__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    
\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   
 \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      
  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      
           | |   (_)    | |                  | (_)                      
        ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ 
       / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|
      | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   
       \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   
________________________________________________________________________''')
    else:
        print(''' __     __           _           _   _                                    
 \ \   / /          | |         | | | |                                   
  \ \_/ /__  _   _  | | ___  ___| |_| |                                   
   \   / _ \| | | | | |/ _ \/ __| __| |                                   
    | | (_) | |_| | | | (_) \__ \ |_|_|                                   
    |_|\___/ \__,_| |_|\___/|___/\__(_)                                   
        _______ _                                        _ _          _ _ 
       |__   __| |                                      | (_)        | | |
          | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |
          | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |
          | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|
          |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)''')


def displayHangman(state):
    if state == 5:
        print('''  ._______.   
     |/          
     |           
     |           
     |           
     |           
     |           
 ____|___  ''')
    elif state == 4:
        print('''  ._______.   
     |/      |   
     |           
     |           
     |           
     |           
     |           
 ____|___ ''')
    elif state == 3:
        print('''._______.   
     |/      |   
     |      (_)  
     |           
     |           
     |           
     |           
 ____|___    ''')
    elif state == 2:
        print('''._______.   
     |/      |   
     |      (_)  
     |       |   
     |       |   
     |           
     |           
 ____|___   ''')
    elif state == 1:
        print(''' ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |           
     |           
 ____|___        
           ''')
    elif state == 0:
        print('''._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |      / \  
     |           
 ____|___        
             ''')


def getWord():
    wordsFile = open("hangman-words.txt", "r")
    list = wordsFile.readlines()
    wordsFile.close()
    return list[randint(0, len(list) - 1)]


def valid(c):
    return c.islower() and len(c) == 1


def play():
    word = getWord()
    state = 5
    outguessed = '_' * (len(word)-1)

    while state > 0 and outguessed != word:
        displayHangman(state)
        print("Guess the word: ", outguessed)
        guess = str(input("Enter the letter: "))
        while not valid(guess):
            guess = str(input("Enter the letter "))

        if guess in word:
            print("The letter, ", guess, "is in the word")
            output = ""
            for i in range(len(word)):
                if guess == word[i]:
                    output = output + guess
                else:
                    output = output + outguessed[i]
            outguessed = output
        else:
            print("\nSorry,", guess, "isn't in word")
            state = state - 1

    if state == 0:
        displayHangman(state)
        print("\nHidden word was: ", word)


def doYouWantToPlayAgain():
    x = str(input("Do you want to play again? "))
    if x == "yes":
        return True
    else:
        return False


def hangman():
    whileCond = True
    while whileCond:
        displayIntro()
        result = play()
        displayEnd(result)
        whileCond = doYouWantToPlayAgain()



if __name__ == "__main__":
    hangman()

