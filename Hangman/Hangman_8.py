# Write your code here
import random
random.seed()

lista = ['python', 'java', 'kotlin', 'javascript']
solution = random.choice(lista)
letter_list = list(solution) 
letter_list_new = [] 
letter_set = set(letter_list)
letter_set_new = set(letter_list)
word = '-' * (len(solution))
outer_letters = []

print('H ' + 'A ' + 'N ' + 'G ' + 'M ' + 'A ' + 'N')
loop = 0
while True:
    start = str(input('Type \"play\" to play the game, \"exit\" to quit:'))
    if start == 'play':
        break
    elif start == 'exit':
        break 
    else:
        loop += 1
   
print('')

n = 0
count = 0
for n in range(1000):
    print('')
    print(word)
    guess = input('Input a letter:')
    letter_list = list(solution)
    letter_set = set(letter_list)
    letter_list_new = []
    if not guess.islower() and len(guess) == 1:
        print('Please enter a lowercase English letter')
    elif len(guess) != 1:
        print('You should input a single letter')
    elif guess in letter_set_new and len(letter_set_new) == 1:
        letter_set_new.remove(guess)
        x = 0
        for x in range(len(word)):
            letter_list = list(solution)
            if letter_list[x] in list(letter_set_new):
                letter_list[x] = '-'
                letter_list_new.append(letter_list[x])
            elif letter_list[x] not in list(letter_set_new):
                letter_list_new.append(letter_list[x])
        x += 1
        word = ''.join(letter_list_new)
        print(word)
        print('You guessed the word ' + word + '!')
        print('You survived!')
        break
    elif guess in letter_set_new and len(letter_set_new) > 1:
        letter_set_new.remove(guess)
        y = 0
        for y in range(len(word)):
            letter_list = list(solution)
            if letter_list[y] in list(letter_set_new):
                letter_list[y] = '-'
                letter_list_new.append(letter_list[y])
            elif letter_list[y] not in list(letter_set_new):
                letter_list_new.append(letter_list[y])
        y += 1
        word = ''.join(letter_list_new) 
        if count == 8:
            print('')
            print(word)
            print('You lost!')
            break 
    elif guess in letter_set and guess not in letter_set_new and count != 8:
        print('You\'ve already guessed this letter')
    elif guess in letter_set and guess not in letter_set_new and count == 8:
        print('That letter doesn\'t appear in the word')
        print('You lost!')
        break 
    else:
        if guess in outer_letters and count != 8:
            print('You\'ve already guessed this letter')
        elif guess not in outer_letters and count != 8:    
            print('That letter doesn\'t appear in the word')
            outer_letters.append(guess)
            count += 1
        if count == 8:
            print('That letter doesn\'t appear in the word')
            print('You lost!')
            break        
        
    n += 1

