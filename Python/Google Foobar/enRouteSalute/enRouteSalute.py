def answer(s):
    bmps = 0
    ris = [i for i, x in enumerate(s,0) if x == '>']
    bis = [i for i, x in enumerate(s,0) if x == '<']
    while ris[0] < len(s) and bis[-1] > 0:
        for i in ris:
            for o in bis:
                if (i + 1) == o or i == o:
                    bmps += 1
        ris = [x + 1 for x in ris if ris[0] < len(s)]
        bis = [x - 1 for x in bis if bis[-1] > 0]
    print("final bmps: " + str(2 * bmps))
    return 2 * bmps
    
answer('--->-><-><-->-')
answer('>----<')
answer('<<>><')
