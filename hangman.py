import requests
import random
from time import sleep

DIFFICULTY = 6

FREQ = 100/DIFFICULTY
DISABLE_ANIMATION = False
WPM = 300

def get_a_word(length):
    url = f"https://api.datamuse.com/words?sp={'?'*length}&md=f&max=1000"
    response = requests.get(url)

    if response.status_code == 200 and response.json():
        words = response.json()
        new_words = []
        for word in words:
            if word['tags'] and float(word['tags'][0].split(":")[1]) > FREQ:
                new_words.append(word['word'])
        return random.choice(new_words)
    return "ERRORS" #Even after error still give a word :)


def char_animation(msg, end = "\n"):
    for char in msg:
        print(char, end = "", flush = True)
        sleep(10/WPM)
    print(end, end = "")

def char_animation_in(msg):
    char_animation(msg, end = "")
    return input()

if DISABLE_ANIMATION:
    char_animation = print
    char_animation_in = input

WORD_LENGTH = [i for i in range(max(DIFFICULTY - 4,2), min(DIFFICULTY + 4,12))]

WORD_LENGTH_WEIGHTED = []
for i,x in enumerate(WORD_LENGTH):
    for j in range(16 - (4-i)**2):
        WORD_LENGTH_WEIGHTED.append(x)

while True:
    length = random.choice(WORD_LENGTH_WEIGHTED)
    word = get_a_word(length)
    if word == "ERRORS":
        raise Exception("Error in fetching word sorry :(")
    char_animation(f"Word is of length {length}\n")
    char_animation(f"Word is: {word}\n")
    #Actual logic of the game