import random
import json

def happy_hacktoberfest():
    with open('data/contributors.json') as f:
        data = json.load(f)
    pick = random.choice(data)
    sentence = "{} wishes you {}".format(pick["author"], pick["wish"])
    return sentence

def main():
    print(happy_hacktoberfest())

if __name__ == "__main__":
    main()