# #!/usr/bin/env python3
# """
# A Classy Problem
# """

from typing import Dict, List


def classify(people: dict) -> List[str]:
     # class_rank = {"upper":5,"middle":4,"lower":3}
    myDict = {}
    for aKey, aValue in people.items():
        myString = ''
        valueList = aValue.split("-")
        valueList = valueList[::-1]
        print(valueList)
        for i in valueList:
            if i == "upper" or i == " upper" or i == "upper ":
                myString+= "5"
            if i == "middle" or i == " middle" or i == "middle ":
                myString += "4"
            if i == "lower" or i == "lower " or i == " lower":
                myString += "3"
        myDict[aKey] = myString
    res = list(myDict.values())[0]
    for aKey, aValue in myDict.items():
        if len(aValue) > len(res):
            res = aValue
    almostFinal = {}
    
    for aKey, aValue in myDict.items():
        if len(aValue) != len(res):
            a = len(res) - len(aValue)
            b = a * '4'
            c = str(aValue) + str(b)
            almostFinal[aKey] = c
        else:
            almostFinal[aKey] = aValue
    # print(almostFinal)
    flipped = {}
    for key, value in almostFinal.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
   
    for key, value in flipped.items():
        value.sort()
        flipped[key] = value
       
    dictionary_items = flipped.items()
    sorted_items = sorted(dictionary_items)
    final = []
    for key, value in sorted_items:
        final.append(value)
    final = final[::-1]
    flattened = [val for sublist in final for val in sublist]
    return flattened
def read_file(filename: str) -> Dict[str, str]:

    f = open(filename, "r")
    myDictionary = dict()
    for x in f: 
        myDictionary[x[0: x.find(':')]] = x[x.find(':') + 1 : x.find('class')]
    return myDictionary
    
def main():

    people = read_file("data/projects/classy/classy01.txt")
    print(classify(people))


if __name__ == "__main__":
    main()