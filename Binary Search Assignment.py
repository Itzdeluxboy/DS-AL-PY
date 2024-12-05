def count_rotations_linear(nums):
    #linear search
    '''Create a variable position with the initial value 0. This variable will track the current index in the list.
       Iterate through the list using a while loop as long as position is less than the length of the list.
       Compare the number at the current position with the smallest number in the list (min(nums)). If they match, return the current position.
       If the loop completes without finding the minimum, return 0 as a default value (this happens when the list is empty).  '''
    
    position=0

    while position < len(nums):
        if nums[position]==min(nums):
            return position
        position+=1

    else:
        return 0

def count_rotations_binary(nums):
    #binary search
    '''Find the middle element of the list
       If the middle element of the list is the smallest element of the list, count the number of elements to the left of the list
       If the middle element of the list is greater than the last element of the list then the smallest number of the list lies to the left of the list.
       If the middle element of the list is smaller than the last element of the list then the smallest number of the list lies to the right of the list
       If there are no elements or if there is only one element, return 0'''
    


tests=[]
test1 = {'input':{'nums': [7,8,9,0,1,2,3,4,5,6]}, 'output' : 3}
tests.append(test1)
#edgecase2
test2={'input':{'nums': [4,5,6,7,8,1,2,3]}, 'output' : 5}
tests.append(test2)
#edgecase3
test3={'input':{'nums': [0,1,2,3,4,5,6,7,8,9]}, 'output' : 0}
tests.append(test3)
#edgecase4
test4={'input':{'nums': [9,0,1,2,3,4,5,6,7,8]}, 'output' : 1}
tests.append(test4)
#edgecase5
test5={'input':{'nums': [1,2,3,4,5,6,7,8,9,0]}, 'output' : 9}# a list that was rotated n-1 times, where n is the size of the list.
tests.append(test5)
#edgecase6
test6={'input':{'nums': [0,1,2,3,4,5,6,7,8,9]}, 'output' : 0}# a list that was rotated n times.
tests.append(test6)
#edgecase7
test7={'input':{'nums': []}, 'output' :-1}# its better to return -1 or raise an exception to indicate an invalid input
tests.append(test7) 
#edgecase8
test8={'input':{'nums': [1]}, 'output' :0}# not sure on the output
tests.append(test8) 



#To check through the edge cases and print results
for i, test in enumerate(tests):
    try:
        result = count_rotations_linear(**test['input'])
        print(f"Test case {i+1}: Result = {result}, Output = {test['output']}")
        print(f"Match: {result== test['output']}")
    except:
        print(f"Test Case {i+1}: Function isn't implemented(?)")