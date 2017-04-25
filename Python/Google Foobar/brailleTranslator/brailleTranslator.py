def answer(plaintext):
    MAX_STR = 50  # max symbols in Braille's line
    H, W = 1, 6   # height and width of Braille character

    # create Braille alphabet
    # the alphabet is written in 1x6 dimensions even though Braille is read in 3x2 dimensions
    pattern = ['100000110000100100100110100010110100110110110010010100010110101000111000101100101110101010111100111110111010011100011110101001111001010111101101101111101011000000000001']
    letters = [[pattern[i][j:j+W] for i in range(H)] for j in range(0, len(pattern[0]), W)]
    BRAILLE = dict(zip('abcdefghijklmnopqrstuvwxyz ^', letters))

    # formatting marks: '#' for number, '^' for capital
    # the part below for digits is vestigial
    prefix = lambda ch: '#' if ch.isdigit() else '^' if ch.isupper() else ''
    
    # prepare text before converting to Braille
    text_out = ''.join(prefix(char) + char.lower() for char in plaintext)
    text_out = [text_out[i:i+MAX_STR] for i in range(0, len(text_out), MAX_STR)]

    # format Braille output
    braille_out = []
    for s in text_out:
        for i in range(H):
            braille_out.append(''.join(BRAILLE[char][i] for char in s))
        braille_out.append('0' * len(braille_out[0]))
    braille_out = braille_out[:-1]
    print(''.join(braille_out))

answer("code")
answer("Braille")
answer("The quick brown fox jumped over the lazy dog")
