#!/usr/bin/env python3
"""
`anomalycounter` implementation

@authors: Roman Yasinovskyy
@version: 2021.10
"""

from pathlib import Path


def count(filename: str) -> int:
    """Count number of anomalies/blobs in an image

    :param filename: name of the file to process
    :return: number of anomalies/blobs in the file
    """
    # TODO: Implement this function
    # NOTE: You may define an auxillary function to implement the algorithm
    myList = []
    f = open(filename, "r")
    for x in f: myList.append(list(x.replace("\n","")))

    counter = 0
    for i in range(len(myList)):
        for j in range(len(myList[0])):
            if myList[i][j] == "*":
                counter += 1
                helper(myList,i, j)
    return counter


def helper(myList,i, j):
  # Base case
  if 0<=i<len(myList) and 0<=j<len(myList[0]) and myList[i][j] == "*":
    myList[i][j] = 7
    helper(myList, i, j+1) # Right
    helper(myList, i, j-1) # Left
    helper(myList, i+1, j) # Up
    helper(myList, i-1, j) # Down 



def main():
    """Entry point"""
    data_dir = "data/projects/anomalycounter/"
    for f in Path(data_dir).glob("*.in"):
        print(f"{f.name}: {count(f)}")


if __name__ == "__main__":
    main()
