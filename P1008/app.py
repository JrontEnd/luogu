# validate three numbers is pass or not?
def validate_result(num_a, num_b, num_c):
    list_a = map(int, str(num_a))
    list_b = map(int, str(num_b))
    list_c = map(int, str(num_c))
    total_list = list(set(list_a + list_b + list_c))
    try:
        if total_list.index(0) > 0:
            return False
    except ValueError:
        return len(total_list) == 9



i = 300
result = ''
while i <= 999:
    num_a = i
    num_b = i * 2/3
    num_c = i * 1/3
    if validate_result(num_a, num_b, num_c):
        result += str(num_c) + ' ' + str(num_b) + ' ' + str(num_a) + '\n'
    i = i + 3

print(result)