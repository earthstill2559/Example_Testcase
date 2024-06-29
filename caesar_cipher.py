def create_caesar_cipher(a, b):
    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
    capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
    chars = list(a)
    output = ''
    if len(a) >= 1 and len(a) <= 100 and b >= 0 and b <= 100:
        for ch in chars:
            if ch in small:
                index = small.index(ch) + b
                n = len(small)
                while index >= n:
                    index = index - n
                ch = small[index]
            elif ch in capital:
                index = capital.index(ch) + b
                n = len(capital)
                while index >= n:
                    index = index - n
                ch = capital[index]
            output += ch
        return output
    else:
        return 'Error'