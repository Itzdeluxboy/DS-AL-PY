def find_given_number(cards, given_number):
    pass

test = {'input':{'cards': [13,12,11,7,4,1,0], 'given_number': 7}, 'output' : 3}
result = find_given_number(**test['input']) == test['output']
print(result)


if result == test['output']:
    print(True)
else:
    print(False)
# cards = [13,12,11,7,4,1,0]
# given_number = 7
# output = 3

