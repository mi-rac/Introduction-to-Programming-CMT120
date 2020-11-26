# Exercise 1
def reduceFraction(num, den):
    from math import gcd
    factor = gcd(num, den)
    return (num // factor, den // factor)


# Exercise 2
def isMagicDate(day, month, year):
    return (day * month) == (year % 100)


# Exercise 3
def sublist(l):
    res = [[]]
    for len_sublist in range(1, len(l)+1):
        for i in range(len(l) - len_sublist + 1):
            res.append(l[i:i + len_sublist])
    return res


# Exercise 4
def pigLatin(word):
    from itertools import takewhile

    case = word[0].isupper()
    word = word.lower()
    punct = ''.join(takewhile(lambda x: not x.isalpha(), word[::-1]))[::-1]
    end_slice = (None, -len(punct))[bool(len(punct))]
    cons = ''.join(takewhile(lambda x: x not in 'aeiou', word))

    res = word[len(cons):end_slice] + cons + ('way', 'ay')[bool(len(cons))] + punct
    return (res, res.capitalize())[case]


# Exercise 5
def morseCode(message):
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----'}

    new_message = ''.join(filter(lambda x: x.isalnum(), message)).upper()
    return ' '.join(MORSE_CODE_DICT[_] for _ in new_message)


# Exercise 6
def int2Text(num):
    DIGITS = {0: '', 1:'one', 2:'two', 3:'three', 4: 'four', 5:'five',
              6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
              11:'eleven', 12:'twelve'}
    TENS = {2:'twen', 3:'thir', 4:'four', 5:'fif',
            6:'six' , 7:'seven', 8:'eigh', 9:'nine'}

    def parse_tens(n):
        if n <= 12:
            return DIGITS[n]
        elif n <= 20:
            return TENS[n%10] + 'teen'
        else:
            return (TENS[n//10] + 'ty ' + DIGITS[n%10]).strip()

    if num == 0:
        return 'zero'
    elif num < 100:
        return parse_tens(num)
    else:
        return (DIGITS[num//100] + ' hundred ' + parse_tens(num%100)).strip()


# Exercise 7
def missingComment(filename):
    res = []
    with open(filename, 'r') as file:
        lines = list(enumerate(file))
        for num, line in lines:
            if line[:4] == 'def ' and lines[num-1][1][0] != '#':
                i = line.index('(')
                res.append(line[4:i])
    return res



# Exercise 8
def consistentLineLength(filename, length=20):
    from textwrap import wrap
    with open(filename, 'r') as file:
        lines = file.read()
    return wrap(lines, length)

# Exercise 9
def knight(start, end, moves):
    return None


# Exercise 10
def warOfSpecies(environment):
    return None

if __name__ == '__main__':
    print(consistentLineLength("test_data/text1.txt"))
