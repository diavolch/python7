from fractions import Fraction

def racional_result(data):
    res = 0
    a, b, move = data
    a = Fraction(a.replace(' ', ''))
    b = Fraction(b.replace(' ', ''))
    if move == '+':
        res = a + b
    elif move == '-':
        res = a - b
    elif move == '*':
        res = a * b
    elif move == '/':
        res = a / b
    return res
