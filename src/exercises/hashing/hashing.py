#!/usr/bin/env python3
"""Hashing functions"""


def hash_remainder(key: int, size: int) -> int:
    """Find hash using remainder"""
    return key%size 

# print(hash_remainder(13,3))

def hash_mid_sqr(key: int, size: int) -> int:
    """Find hash using mid-square method"""
    return int(str(key * key) \
        [len(str(key * key)) // 2-1:len(str(key * key)) // 2+1]) % size


def hash_folding(key: str, size: int) -> int:
    """Find hash using folding method"""
    # if (len(key))%2 == 0:
    #     firstHalf = key[:len(key) // 2]
    #     secondHalf = key[firstHalf: ]
    #     for x in firstHalf:
    #         first = x%size
    #     for y in secondHalf:
    #         second = y%size
    #     return (first + second)/size
    return NotImplemented
    


        

    


    
print(hash_folding(123,3))

def hash_str(key: str, size: int) -> int:
    """Find string hash using simple sum-of-values method"""
    num = 0
    for i in range(len(key)):
        num += ord(key[i])
    return (num % size)


def hash_str_weighted(key: str, size: int) -> int:
    """Find string hash using character positions as weights"""
    num = 0
    for i in range(len(key)):
        num += ord(key[i])*i
    return (num % size)



