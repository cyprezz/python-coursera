def to_string(num: int) -> str:
    return str(num)


print(list(map(to_string, [1, 2, 3, 4])))
test1 = {
    'key1': 'val1',
    'key2': ['val2', 'val3']
}

test1['key2'].append('test1')

key = 'key3'
if key in test1.keys():
    print(test1[key])
else:
    print('error')

# print(test1[key])
