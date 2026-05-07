#problem set 2
import random
import string
#辅助函数
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
     
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open('words.txt', 'r')
    # line: string
    line = inFile.readline()
     # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist
def choose_word(wordlist):
     """
     wordlist (list): list of words (strings)
     
     Returns a word from wordlist at random
     """
     return random.choice(wordlist)
       # Load the list of words into the variable wordlist
       # so that it can be accessed from anywhere in the program
     wordlist = load_words()
def has_player_won(secret_word,letters_guessed):
    #没有写出来的部分
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True

def get_word_progress(secret_word,letters_guessed):
    mylist=[]
    for i in secret_word:
        if i in letters_guessed:
            mylist.append(i)
        else:
            mylist.append('*')
    return ''.join(mylist)#这个是把列表转换为字符串用到的是  ''.join(列表)
#这个函数自己编写的完全正确
def get_available_letters(letters_guessed):
    letter='abcdefghijklmnopqrstuvwxyz'
    letters=list(letter)
    for i in letters_guessed:
        letters.remove(i)
    return ''.join(letters)

def hangman(secret_word,with_help):
    guesses_left=10
    letters_guessed=[]
    vowels=['a','e','i','o','u']
    print("欢迎来到Hangman")
    print(f"我想的单词有{len(secret_word)}个字母")
    print("——————————————————————————————————————————")
    while guesses_left>0 and not has_player_won(secret_word,letters_guessed):
        print(f"你还有{guesses_left}次猜词机会")
        print(f"剩余可用字母：{get_available_letters(letters_guessed)}")
        guess=input("请输入你的字母：").lower()
        if guess == "!" and with_help:
            if guesses_left<3:
                print("剩余猜词次数不够用了！！！",get_word_progress(secret_word,letters_guessed))
                print("————————————————————————————————————————")
                continue
            unguessed=[]
            #随机揭示一个未猜中字母
            for c in secret_word:
                if c not in letters_guessed:
                    unguessed.append(c)
                    revealed=random.choice(list(set(unguessed)))#random.choice(wordlist)从词库随机选一个秘密单词。set(word)是自动去重
                    letters_guessed.append(revealed)
                guesses_left -= 3
                print("Letter revealed:", revealed)
                print(get_word_progress(secret_word, letters_guessed))
                print("-------------")
                continue
         # 输入不合法（不是单个字母）
            if len(guess) != 1 or not guess.isalpha():#guess.isalpha()要求输入的必须是字母
                print("Oops! That is not a valid letter. Please input a letter from the alphabet:", get_word_progress(secret_word, letters_guessed))
                print("-------------")
                continue
            if guess in letters_guessed:
                print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed))
                print("-------------")
                continue

        # 加入已猜列表
        letters_guessed.append(guess)

        # 判断是否猜中
        if guess in secret_word:
            print("Good guess:", get_word_progress(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word:", get_word_progress(secret_word, letters_guessed))
            # 扣分规则：元音-2，辅音-1
            if guess in vowels:
                guesses_left -= 2
            else:
                guesses_left -= 1

        print("-------------")

    # 游戏结束
    if has_player_won(secret_word, letters_guessed):
        print("Congratulations, you won!")
        unique = len(set(secret_word))
        score = (guesses_left + 4 * unique) + 3 * len(secret_word)
        print("Your total score for this game is:", score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)

# ------------------------------
# 运行游戏
# ------------------------------
if __name__ == "__main__":
    hangman(choose_word(wordlist),with_help=False)

