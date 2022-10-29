fruit = dict() #초기화
fruit['사과'] = 'apple'
fruit['바나나'] = 'banana'
fruit['오렌지'] = 'orange'

key_list = fruit.keys()
print(key_list) #dict_keys(['사과', '바나나', '오렌지'])

value_list = fruit.values()
print(list(value_list)) #dict_values(['apple', 'banana', 'orange'])

for key in key_list:
    print(key)
    #사과
    #바나나
    #오렌지

b = {
    'gildong':97,
    '순신':98
}

print(b)