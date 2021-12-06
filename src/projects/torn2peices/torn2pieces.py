#Firdavs Atabaev
import sys
from collections import defaultdict

def torn(res, dest, myGraph, v):
        while res and dest != res[0][0]:
            s, r = res.pop(0)
            if s not in v:
                v.add(s)
                for i in myGraph[s] - v: res.append((i, r + [i]))

def main(data):
    myGraph, aList, aLine, res = defaultdict(set), list(), data.readlines(), list()
    for i in aLine: aList.append(i.strip().split())
    number, start, dest = int(aList[0][0]), aList[-1][0], aList[-1][-1]
    aList.pop(0)
    aList.pop(-1)
    for i in range(number):
        for j in aList: 
            for sub in j:    
                myGraph[j[0] ].add(sub)
                myGraph[sub].add(j[0] )
        for i in myGraph[start]: res.append((i, [start,i]))
        torn(res, dest, myGraph, set([start]))
    if res: print(" ".join(res[0][1]))
    else: print("no route found")   
        
if __name__ == "__main__":
    main(sys.stdin)