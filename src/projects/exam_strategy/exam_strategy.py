#!/usr/bin/env python3
"""
`exam_strategy` implementation and driver

@authors: Roman Yasinovskyy
@version: 2021.10
"""

from collections import namedtuple

Item = namedtuple("Item", ["value", "weight"])


def knapsack(capacity: int, items: list[Item]) -> list[int]:
    """
    General Knapsack solution.

    :param capacity: total knapsack capacity
    :param items: the list of items (named tuples) to consider
    :return: a list of chosen indices
    """
    # TODO: Implement this function
    # Get all the weights and values
    value, weight, theMatrix = [], [], []
    for i in items: value.append(i[0])
    for i in items: weight.append(i[1])
    row = weight[0]
    # Create all 0s following the first law
    theMatrix = [[0 for i in range(capacity+1)] for i in range(row+1)]
    # Add second and third law
    value.pop(0)
    weight.pop(0)
    for i in range(row + 1): 
        for j in range(capacity + 1): 
            if i == 0 or j == 0:  theMatrix[i][j] = 0
            # Third law
            elif weight[i-1] <= j: theMatrix[i][j] = max(value[i-1] + theMatrix[i-1][j-weight[i-1]],  theMatrix[i-1][j]) 
            # Second law
            else: theMatrix[i][j] = theMatrix[i-1][j] 
    
    
    # Getting  the last item of the matrix  
    c, w, res = theMatrix[row][capacity], capacity, list()
    cond = True
    for i in range(row, 0, -1): 
        if theMatrix[row][capacity] <= 0: cond is False
        elif theMatrix[row][capacity] == theMatrix[i - 1][w] and cond is True: continue
        else: 
            res.append([i-1])
            res.append(weight[i - 1]) 
            theMatrix[row][capacity] -= value[i - 1] 
            w -= weight[i - 1] 
    final=[j for i in res[::2] for j in i]
    final.reverse()
    return [final, c]


def pick_questions_to_answer(filename: str) -> tuple[list[int], int]:
    """
    Main selection function

    :param filename: file to process
    :return: the list of chosen indices and total point value of all selected questions
    """
    # TODO: Implement this function
    myList = []
    with open(filename) as f:
        for aline in f:
            aline = aline.split()
            if aline:          
                aline = [int(float(i)) for i in aline]
                myList.append(aline)
    return (knapsack(myList[0][0], myList))


def main():
    """Entry point"""
    for i in range(1, 6):
        filename = f"data/projects/exam_strategy/questions{i}.in"
        selection = pick_questions_to_answer(filename)
        print(
            f"Case {i}: Items {sorted(selection[0])} sum up to {selection[1]}"
        )


if __name__ == "__main__":
    main()
