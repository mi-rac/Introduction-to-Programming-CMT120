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
    TENS = {2:'twen', 3:'thir', 4:'for', 5:'fif',
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

    class Position:
        def __init__(self, position_x='a1', position_y=1):
            if type(position_x) == str:
                self.x = ord(position_x[0]) - ord('a')
                self.y = int(position_x[1]) - 1
            elif type(position_x) == int:
                self.x = position_x
                self.y = position_y
            else:
                raise ValueError("Position objects are initialised with one string of the form a2 or two integers.")

        def __str__(self):
            return chr(self.x + ord('a')) + str(self.y + 1)

        def __eq__(self, other):
            return str(self) == str(other)

        def knight_moves(self):
            _nextList = []
            for i in (0, 1):
                for j in (-1, 1):
                    for k in (-1, 1):
                        dx = (1, 2)[i] * j
                        dy = (1, 2)[1-i] * k
                        new_x = self.x + dx
                        new_y = self.y + dy
                        if (0 <= new_x < 8) and (0 <= new_y < 8):
                            _nextList.append(Position(new_x, new_y))
            return _nextList

    class Board:
        def __init__(self):
            self.board = [[None for x in range(8)] for y in range(8)]

        def __str__(self):
            text = ''
            for line in self.board:
                txt_line = ''
                for word in line:
                    txt_line += str(word).center(6)
                text += '[' + txt_line + ']\n'
            return text

        def clear(self):
            self.board = [[None for x in range(8)] for y in range(8)]

        def fill(self, position, text):
            self.board[position.x][position.y] = text

        def get_value(self, position):
            return self.board[position.x][position.y]

        def number_steps(self, start, end):
            def next_step(step=0):
                for x in range(8):
                    for y in range(8):
                        if self.board[x][y] == step:
                            current = Position(x, y)
                            for pos in current.knight_moves():
                                if self.get_value(pos) == None:
                                    self.fill(pos, step + 1)

            self.clear()
            self.fill(start, 0)
            step = 0
            while self.get_value(end) == None:
                next_step(step)
                step += 1
            return self.get_value(end)

    board = Board()
    start = Position(start)
    end = Position(end)

    res = board.number_steps(start, end)

    return res <= moves


# Exercise 10
def warOfSpecies(environment):
    y_max = len(environment)
    x_max = len(environment[0])

    def neighbours_matrix(environment):
        neighbours_matrix = [['' for x in range(x_max)] for y in range(y_max)]
        for j in range(y_max):
            for i in range(x_max):
                for x in [-1, 0 , 1]:
                    for y in [-1, 0 , 1]:
                        if (0 <= (j+y) < y_max) and (0 <= (i+x) < x_max) and not (x == 0 and y == 0):
                            neighbours_matrix[j][i] += environment[j+y][i+x]
                        continue
        return neighbours_matrix

    def rule(item, neighbours):
        num = {}
        num['X'] = num_x = (neighbours.count('X'), 'X')
        num['O'] = num_o = (neighbours.count('O'), 'O')
        num['.'] = num_empty = (neighbours.count('.'), '.')

        if item == ".":
            if (num_x != num_o) and (max(num_x, num_o)[0] >= 2):
                return max(num_x, num_o)[1]
            else:
                return item
        elif num_x[0] + num_o[0] > 6:
            return '.'
        elif num[item][0] < 3:
            return '.'
        elif num[item][0] < num[('O', 'X')[item == 'O']][0]:
            return '.'
        else:
            return item

    def next_frame(environment):
        new_matrix = [[None for x in range(x_max)] for y in range(y_max)]
        neighbours = neighbours_matrix(environment)
        for j in range(y_max):
            for i in range(x_max):
                new_matrix[j][i] = rule(environment[j][i], neighbours[j][i])
            new_matrix[j] = ''.join(new_matrix[j])
        return new_matrix

    return next_frame(environment)



if __name__ == '__main__':

    print(knight('d4', 'h8', 4))
