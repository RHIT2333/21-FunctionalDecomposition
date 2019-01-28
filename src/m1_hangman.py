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
        if len(aim) < 5:
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
    print('The lenth of the word is:', len(result))
    chance = 15 - int(input("Chose the difficulties from 0 - 10: "))
    print(str(check))
    while True:
        for n in range(len(result)):
            if result[n] == "*":
                break
            else:
                detect = True
                chance = 0
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
                break
            else:
                print('You make this !')
                print(result)
                print('Remaining Chance(s):', chance)
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
