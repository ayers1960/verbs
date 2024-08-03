
import csv
import sys

class Tenses():
    def __init__(self,tenses={}):
        self.eu   = tenses["eu"]
        self.tu   = tenses["tu"]
        self.ele  = tenses["ele"]
        self.nós  = tenses["nós"]
        self.eles = tenses["eles"]


class Verbs():
    def __init__(self,English,Portuguese, presentTenses=[]):
        self.English = English
        self.Portuguese = Portuguese
        self.present = Tenses(presentTenses)


def loadVerbs():
    verbs = []
    with open("present.csv") as csvFile: 
        reader = csv.DictReader(csvFile)
        for row in reader:
            v = Verbs(row["English"], row["Portuguese"], row)
            verbs.append(v)
    return verbs

if __name__ == "__main__":
    verbs = loadVerbs()
    print(verbs[0].English)
    sys.exit(99)
    ser = {
        "eu": "sou",
        "tu": "és",
        "ele": "é",
        "nós": "somos",
        "vocês": "são",
    } 
    v = Verbs("To Be", "Ser", ser)
    print(v.present.nós)

