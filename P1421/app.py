def input():
    return '10 3'


str = input().split()
yuan = int(str[0])
jiao = int(str[1])

amount = yuan * 10 + jiao
price = 10 + 9
print(int(amount/price))