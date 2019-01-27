"""
Hangman.

Authors: Hanrui Chen and Yifan Dai.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

import random

def get_words():
    with open('words.txt') as lib:
        lib.readline()
        string = lib.read()
        words = string.split()
        r = random.randrange(0, len(words))
        aim = words[r]
    return aim

def exam_and_store():
    while True:
        aim = get_words()
        if len(str(aim)) > 5:
            break
    return aim

def guess():
    chance = 15 - int(input("Chose the difficulties from 0 - 10: "))
    aim = exam_and_store()
    result = []
    for l in range(len(str(aim))):
        result.append('*')
    for k in range(chance):
        letter = str(input("Enter a letter: "))
        for j in range(len(str(aim))):
            if letter == aim[j]:
                result[j] = letter
        if result == result:
            print('Letter no mach : (')
            print(result)
            chance = chance - 1
            print('Remaining Chance(s):', chance)
        else:
            print('You make this !')
            print(result)
            print('Remaining Chance(s):', chance)
    print("Out of chance!")
    print('The word is:', aim)

####### Do NOT attempt this assignment before class! #######

def main():
    guess()

main()
