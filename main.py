import keyboard
import random
import os


with open('ton_english.txt', 'r') as f:
    words = [line.strip() for line in f.readlines()]

with open('generated_phrases_12.txt', 'r') as f:
    phrasesAmount12 = len(f.readlines())

with open('generated_phrases_24.txt', 'r') as f:
    phrasesAmount24 = len(f.readlines())



a=int(input(f'Phrases Amount: {phrasesAmount12} / {phrasesAmount24}\n \n[1] n-amount phrases \n[2] endless amount \n'))
b=int(input(f'Phrases Amount: {phrasesAmount12} / {phrasesAmount24}\n \n[1] 12 sercet words \n[2] 24 sercet words \n'))

count=0

if a==1 and b==1:
    times=int(input('how many phrases?\n'))
    for i in range(times):
        count+=1
        phrase = random.sample(words, 12)
        phrase= ' '.join(phrase)
        phrase=phrase+'\n'

        with open('generated_phrases_12.txt', 'a') as f:
            f.write(phrase)
        print(f'{count} - '+phrase)

elif a==1 and b==2:
    times=int(input('how many phrases?\n'))
    for i in range(times):
        count+=1
        phrase = random.sample(words, 24)
        phrase= ' '.join(phrase)
        phrase=phrase+'\n'

        with open('generated_phrases_24.txt', 'a') as f:
            f.write(phrase)
        print(f'{count} - '+phrase)

elif a==2 and b==1:
    while True: 
        count+=1
        phrase = random.sample(words, 12)
        phrase= ' '.join(phrase)
        phrase=phrase+'\n'

        with open('generated_phrases_12.txt', 'a') as f:
            f.write(phrase)
        
        print(f'{count} - '+phrase)
        
        
        if keyboard.is_pressed("q"):
            break

elif a==2 and b==2:
    while True: 
        count+=1
        phrase = random.sample(words, 24)
        phrase= ' '.join(phrase)
        phrase=phrase+'\n'

        with open('generated_phrases_24.txt', 'a') as f:
            f.write(phrase)
        
        print(f'{count} - '+phrase)
        
        
        if keyboard.is_pressed("q"):
            break

