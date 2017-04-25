def answer(start, length):
    libs = list(range(start, length * length))
    it = [iter(libs)] * length
    tng = length
    spt = []

    fdr = zip(*it)
    
    for i in fdr:
        print(i)

    for index, item in enumerate(fdr):
        spt.append(index)
    
    print(spt)

answer(0, 3)
#answer(17, 4)
