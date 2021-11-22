#!/usr/bin/env python3
"""
Convex Hull

@authors: Roman Yasinovskyy
@version: 2021.11
"""
import math

def get_convex(filename: str) -> list:
    """
    Find points on the convex hull

    Calculate the result with p0 as the lowest-rightmost

    :param filename: name of a file with all all points
    :return: list of point in the correct order (starting with the rightmost-lowest)
    """
    #Returning list of tuples holding all points in the file
    listofAllPoints = []
    with open(filename) as f:
        for rows in f:
            rows = rows.split()
            if rows:          
                rows = [((i)) for i in rows]
                if rows[2] == "Y":
                    listofAllPoints.append((float(rows[0]), float(rows[1])))

    xx, yy = min(listofAllPoints, key=lambda x: (x[0], x[1])) 
        
    mp = {}
    for x, y in listofAllPoints: mp.setdefault(math.atan2(y-yy, x-xx), []).append([x, y])
        
    hull = []
    m = max(mp)
    for k in sorted(mp): 
        mp[k].sort(key=lambda p: abs(p[0]-xx)+abs(p[1]-yy))
        if k == m and hull: mp[k].reverse()
        hull.extend(mp[k])
    return hull

def measureTheDistance(x1, y1, x2, y2):
    distance = math.hypot(x2 - x1, y2 - y1)
    return distance

def total_dist(ml):  
    n = len(ml)
    total = 0.0
    for i in range (n):
        x1 = ml[i][0]
        y1 = ml[i][1]
        if i < n-1:
            x2 = ml[i+1][0]
            y2 = ml[i+1][1]
        else:
            x2 = ml[0][0]
            y2 = ml[0][1]
        dist = measureTheDistance(x1,y1,x2,y2)
        total += dist
    return total

def measure_convex(hull_points: list) -> float:
    """
    Calculate the length of the convex hull

    :param hull_points: all points on the convex hull in counter-clockwise order
    :return: length of the convex hull
    """
    stack = []
    for x, y in hull_points: 
        while len(stack) >= 2: 
            x0, y0 = stack[-1]
            x1, y1 = stack[-2]
            if (x0-x1)*(y-y0) - (x-x0)*(y0-y1) >= 0: break
            else: stack.pop()
        stack.append([x, y])
    return total_dist(stack)

numbers = [21,14,3,15,16,25,18,9,7,8,20,1,2,12,5,19]
print(sorted(numbers))


def main():
    """Entry point"""
    print(f"{'file':20s}{'points':10s}{'length'}")
    for i in [1, 2, 3]:
        filename = f"convexhull{i}.in"
        hull_points = get_convex("data/projects/convexhull/" + filename)
        hull_length = measure_convex(hull_points)
        print(f"{filename:20s}{len(hull_points):<10d}{hull_length}")


if __name__ == "__main__":
    main()

