import string

do_op = {'+': (lambda a, b: a + b),
         '*': (lambda a, b: a * b)}


def evaluate(expr):
    prev_value = 0
    prev_op = '+'
    end = 0
    while end < len(expr):
        beg = end
        if expr[beg] == '(':
            level = 1
            while level:
                end += 1
                if expr[end] in '()':
                    level += {'(':1, ')':-1}[expr[end]]
            value = evaluate(expr[beg + 1:end])
            end += 1
        else:
            while end < len(expr) and expr[end] in string.digits:
                end += 1
            value = int(expr[beg:end])
        prev_value = do_op[prev_op](prev_value, value)
        while end < len(expr) and expr[end] not in '+*':
            end += 1
        if end == len(expr):
            break
        prev_op = expr[end]
        end += 1
        while end < len(expr) and expr[end] == ' ':
            end += 1
    return prev_value

answer = 0
while True:
    try:
        line = input()
    except:
        break
    answer += evaluate(line)

print(answer)
