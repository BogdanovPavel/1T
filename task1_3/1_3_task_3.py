abic_roman_hundred = {
    0: '',
    1: "C",
    2: "CC",
    3: "CCC",
    4: "CD",
    5: "D",
    6: "DC",
    7: "DCC",
    8: "DCCC",
    9: "CM",
}
abic_roman_decade = {
    0: '',
    1: "X",
    2: "XX",
    3: "XXX",
    4: "XL",
    5: "L",
    6: "LX",
    7: "LXX",
    8: "LXXX",
    9: "XC",
}

abic_roman_number = {
    0: '',
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
}

n = int(input())
result = ''
m = n // 1000
n = n % 1000

while m > 0:
    result += 'M'
    m -= 1

m = n // 100
n = n % 100

result += abic_roman_hundred[m]

m = n // 10
n = n % 10

result += abic_roman_decade[m]

result += abic_roman_number[n]

print(result)
