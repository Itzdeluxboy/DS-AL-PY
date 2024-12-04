def find_given_number(cards, given_number):

    '''1)Create a variable position with the value 0.
       2)Check whether the number at index position in card equals query.
       3)If it does, position is the answer and can be returned from the function
       4)If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
       5)If the number was not found, return -1.'''

    position=0

    while True:
        if cards[position]==given_number:
            return position
        position+=1

        if position ==len(cards):
            return -1 #number not found the in the list


tests=[]
test = {'input':{'cards': [13,12,11,7,4,1,0], 'given_number': 7}, 'output' : 3}
tests.append(test)
#edgecase2
test2={'input':{'cards': [13,12,11,7,4,1,0], 'given_number': 13}, 'output' : 0}
tests.append(test2)
#edgecase3
test3={'input':{'cards': [13,12,11,7,4,1,0], 'given_number': 0}, 'output' : 6}
tests.append(test3)
#edgecase4
test4={'input':{'cards': [7], 'given_number': 7}, 'output' : 0}
tests.append(test4)
#edgecase5
test5={'input':{'cards': [13,12,11,7,4,1,0], 'given_number': 12}, 'output' : -1}
tests.append(test5)
#edgecase6
test6={'input':{'cards': [], 'given_number': 7}, 'output' : -1}
tests.append(test6)
#edgecase7
test7={'input':{'cards': [13,13,13,12,11,11,11,7,4,1,0,0,0,0], 'given_number': 7}, 'output' : 7}
tests.append(test7) 
#edegcase8
test8={'input':{'cards': [13,13,13,12,11,11,11,7,7,7,7,7,7,4,1,0,0,0,0], 'given_number': 7}, 'output' : 7}
tests.append(test8)#for this case, we are assuming that the fn returns the first occurence of the 'given_number'
#if the list doesn't contain the given_number
test9={'input':{'cards': [13,12,11,7,4,1,0], 'given_number': 5}, 'output' : -1}
tests.append(test9)

print(tests)

#To check through the edge cases and print results
for i, test in enumerate(tests):
    try:
        result = find_given_number(**test['input'])
        print(f"Test case {i+1}: Result = {result}, Output = {test['output']}")
        print(f"Match: {result== test['output']}")
    except TypeError:
        print(f"Test Case {i+1}: Function isn't implemented(?)")






