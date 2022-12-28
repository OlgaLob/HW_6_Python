# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*
# c возможностью использования скобок, меняющих приоритет операций.
file_name = 'op.txt'
def Get_expression(file_name):
    expression = Convert(file_name)
    while '(' in expression:
        expression = Brackets(expression, 0, len(expression))
    expression = Mult_div(expression, 0, len(expression))
    expression = Sum_sub(expression, 0, len(expression))
    return expression


def Convert(file_name):
    file = open(file_name, 'r')
    text = file.readline()
    print(text)
    expression =[]
    sign = '+-*/()'
    num = ""
    for i in text:
        if i in (sign):
            if num != "":
                expression.append(int(num))
                num = ''
            expression.append(i)
        else:
            num += i
    if num != '':
        expression.append(int(num))
    return expression


def Brackets(expression, start, end):
    i = start
    count = 0
    while i < end:
        if expression[i] == '(':
            start = i
        if expression[i] == ')':
            end = i
            expression.pop(end)
            expression.pop(start)
            expression = Mult_div(expression, start, end - 2)
            expression = Sum_sub(expression, start, end - 2)
            return expression
        i += 1


def Mult_div(expression, start, end):
    i = start
    while i < end:
        if expression[i] == '*':
            expression[i - 1] *= expression[i + 1]
            expression.pop(i)
            expression.pop(i)
            end -= 2
            i -= 1
        elif expression[i] == '/':
            expression[i - 1] /= expression[i + 1]
            expression.pop(i)
            expression.pop(i)
            end -= 2
            i -= 1
        i += 1
    return expression


def Sum_sub(expression, start, end):
    i = start
    while i < end:
        if expression[i] == '+':
            expression[i - 1] += expression[i + 1]
            expression.pop(i)
            expression.pop(i)
            end -= 2
        elif expression[i] == '-':
            expression[i - 1] -= expression[i + 1]
            expression.pop(i)
            expression.pop(i)
            end -= 2
        i += 1
    return expression


print(Get_expression(file_name))