str_brace = {
    ")": "(",
    "}": "{",
    "]": "[",
}

str = input()

result_str = ""

result = 'false'

i = 1
stack = []

while i < len(str) & len(str) > 1:

    brace = str_brace.get(str[i], '')

    if str[i-1] != brace :
        stack.append(str[i-1])

        print('apend ', stack)

        if stack[-1] == brace:
            stack.pop()


            print('pop', stack[-1], 'pop1')
    else :
        i += 1



    i += 1

    print('while', result_str)

print(result, stack)