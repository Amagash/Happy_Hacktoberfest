import random
import json
import pkgutil


def happy_hacktoberfest():
    test = pkgutil.get_data(__name__, "data/contributors.json")
    data = json.loads(test)
    pick = random.choice(data)
    return "{} wishes you {}".format(pick["author"], pick["wish"])


def main():
    print(happy_hacktoberfest())


if __name__ == "__main__":
    main()
