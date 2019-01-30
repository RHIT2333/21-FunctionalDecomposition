"""
Hangman.

Authors: Hanrui Chen and Yifan Dai.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

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
        if len(aim) > 5:
            break
    return aim

def judge():
    aim = exam_and_store()
    result = []
    check = []
    detect = False
    while True:
        result.append('*')
        if len(result) == len(aim):
            break
    for m in range(len(aim)):
        check.append(aim[m])
    print('The length of the word is:', len(result))
    chance = 15 - int(input("Chose the difficulties from 0 - 10: "))
    if chance > 15:
        print("Read the instruction carefully! Your chances will be 15 times")
        chance = 15
    elif chance < 5:
        print("Read the instruction carefully! Your chances will be 5 times")
        chance = 5
    while True:
        n = 0
        while True:
            if result[n] != '*':
                n = n + 1
            else:
                break
            if n == len(result):
                detect = True
                chance = 0
                break
        for k in range(chance):
            letter = str(input("Enter a letter: "))
            container = []
            for l in range(len(result)):
                container.append(result[l])
            for j in range(len(aim)):
                if letter == aim[j]:
                    result[j] = letter
            if result == container:
                print('Letter no mach : (')
                print(result)
                chance = chance - 1
                print('Remaining Chance(s):', chance)
                print()
                break
            else:
                print('Letter matched!')
                print(result)
                print('Remaining Chance(s):', chance)
                print()
                break
        if chance == 0:
            break
    if detect == True:
        print("You are correct!")
        print("The word is:", aim)
    else:
        print("Out of chance!")
        print('The word is:', aim)

####### Do NOT attempt this assignment before class! #######

def main():
    judge()

main()
