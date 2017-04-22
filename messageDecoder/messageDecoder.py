def answer(l,t):
    for i, v in enumerate(l):
        for i2, v2 in enumerate(l):
            print("v: " + str(v) + " v2: " + str(v2))
            if sum(l[i:i2]) == t:
                print([i, i2])
                return [i, i2 - 1]
            elif sum(l[i:i2 + 1]) == t:
                print([0, i2])
                return [i, i2]
    print([-1, -1])
    return [-1, -1]


answer([1,2,3], 6)
answer([1,2,3,4], 10)
#answer([4,3,5,7,8], 12)
#answer([4,3,10,2,8], 12)
#answer([1,2,3,4], 15)
#answer([4,3,5,7,8,4,3,10,2,8], 12)
#answer([123,34,656,66,43,78,34,675,23,4,6,2,342,6,4,24,34,1,2,1,1,1], 200)
#answer([1,4,2,1,5,2,4,2,34,1,1,3,9,17], 65)
#answer([34,1,1,3,9,17], 65)
#answer([10, 45, 31, 45, 12, 34, 3, 1, 1, 1, 1, 4], 7)
#answer([1,2], 3)
#answer([1,4], 3)
#answer([1], 1)
#answer([4], 1)
#answer([1,-2,3], -4)
