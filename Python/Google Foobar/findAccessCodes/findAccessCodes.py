def answer(l):    
        fwd, rev = [], []
        for i in range(1, len(l)):
            fwd.append(sum([1 if (l[i]%l[q]==0) else 0 for q in range(i)]))
            # fwd lists potential lucky triples going left to right
            rev.append(sum([1 if (l[q]%l[i]==0) else 0 for q in range(i+1, len(l))]))
            # rev lists potential lucky triples going from right to left

        print(sum([a*b for a,b in zip(fwd, rev)]))
        return sum([a*b for a,b in zip(fwd, rev)])
        # the corresponding values from col and row are multiplied to see
        # if there are any true lucky triples. false lucky triples will
        # have 0 values going in one direction and multiplication will cancel
        # out those values. multiplication accounts for the different
        # combinations of numbers that arise when considering both the pairs
        # in the triple.


answer([1,1,1])
answer([1,2,3,4,5,6])
answer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
answer([1] * 2000)
