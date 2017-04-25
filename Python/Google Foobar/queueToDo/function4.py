import operator

def answer(start, length):
    checksum = 0
    for i, begin in enumerate(xrange(start, start + length * length, length)):
        checksum ^= reduce(operator.xor, xrange(begin, begin + length - i), 0)
    
    print(checksum)
    return checksum


answer(0, 3)
answer(17, 4)
answer(17, 6)
answer(17, 8)
answer(17, 5)
answer(2, 6)
answer(2, 5)
