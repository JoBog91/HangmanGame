import random

print('H A N G M A N')

menu = input('Type "play" to play the game, "exit" to quit:')
words_list = ['python', 'java', 'kotlin', 'javascript']
mash_choice = random.choice(words_list)
lives = 8
b = ("-" * (len(mash_choice)))
char_list = []

while lives != 0 and menu == "play":
    print('\n{}'.format("".join(b)))
    char = input('Input a letter:')

    if len(char) > 1:
        char_list.append(char)
        print('You should input a single letter')
        continue

    elif char.islower() == False:
        char_list.append(char)
        print('Please enter a lowercase English letter')
        continue

    elif char in b or char in char_list:
        print("You've already guessed this letter")

    elif char in mash_choice:
        for i in range(len(mash_choice)):
            if mash_choice[i] == char:
                b = b[:i] + char + b[i + 1:]

    else:
        char_list.append(char)
        print("That letter doesn't appear in the word")
        lives -= 1

    if b.count('-') == 0:
        print('You guessed the word' + ' ' + mash_choice + '!')
        print('You survived!')
        break

if lives == 0:
        print('You lost!')

