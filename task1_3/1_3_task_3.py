n = int(input())
result = ''
m = n // 1000

while m > 0:
    result += 'M'
    m -= 1
n = n - m * 1000



print(result)