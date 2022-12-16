def complex_result(data):
    res = 0
    a, b, move = data
    a = complex(a.replace(' ', ''))
    b = complex(b.replace(' ', ''))
    if move == '+':
        res = a + b
    elif move == '-':
        res = a - b
    elif move == '*':
        res = a * b
    elif move == '/':
        res = a / b
    return res