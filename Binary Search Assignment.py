def count_rotations(nums):
    pass





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
test7={'input':{'cards': []}, 'output' :-1}# its better to return -1 or raise an exception to indicate an invalid input
tests.append(test7) 
#edgecase8
test8={'input':{'cards': [1]}, 'output' :0}# not sure on the output
tests.append(test8) 