str = '111'
str2 = '101'

result = 'Error'

n1 = int(str, 2)
n2 = int(str2, 2)

result = "{0:b}".format(n1 * n2)

print(result)

