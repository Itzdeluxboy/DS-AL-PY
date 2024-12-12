#QUESTION 1: You're working on a new feature on Jovian called "Top Notebooks of the Week". Write a function to sort a list of notebooks in decreasing order of likes.
# Keep in mind that up to millions of notebooks can be created every week, so your function needs to be as efficient as possible
'''To solve the above problem, we simplify the problem into a smaller problem'''
#Write a function to sort a list of numbers in increasing order
def sort(nums):
    pass

#lists of numbers in random order.
test1={'input':{'nums':[4,2,6,3,4,6,2,1]}, 'output':[1,2,2,3,4,4,6,6]}
#List of numbers in random order
test2={'input':{'nums':[5, 2, 6, 1, 23, 7, -12, 12, -243, 0]}, 'output':[-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]}
#A list that's already sorted
test3={'input':{'nums':[3, 5, 6, 8, 9, 10, 99]}, 'output':[3, 5, 6, 8, 9, 10, 99]}
#A list that's sorted in descending order
test4={'input':{'nums':[99, 10, 9, 8, 6, 5, 3]}, 'output':[3, 5, 6, 8, 9, 10, 99]}
#A list containing repeating elements
test5={'input':{'nums':[5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]}, 'output':[-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]}
#An empty list
test6={'input':{'nums':[]}, 'output':[]}
#A list containing just one element
test7={'input':{'nums':[23]}, 'output':[23]}
#A list containing one element repeated many times
test8={'input':{'nums':[42,42,42,42,42,42,42]}, 'output':[42,42,42,42,42,42,42]}

import random

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test9={'input':{'nums':in_list}, 'output':out_list}
tests=[test1,test2,test3,test4,test5,test6,test7,test8,test9]

#bubble sort
def bubble_sort(nums):
    nums = list(nums)

    for _ in range(len(nums)-1):

        for i in range(len(nums)-1):
            if nums[i]> nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

    return nums

#test1
nums1, output1 = test1['input']['nums'], test1['output']
print('Input:', nums1)
print('Expected output:', output1)
result1= bubble_sort(nums1)
print('Actual output:', result1)
print('Match:', result1 == output1)

# Test 2
nums2, output2 = test2['input']['nums'], test2['output']
print('Input:', nums2)
print('Expected output:', output2)
result2 = bubble_sort(nums2)
print('Actual output:', result2)
print('Match:', result2 == output2)

# Test 3
nums3, output3 = test3['input']['nums'], test3['output']
print('Input:', nums3)
print('Expected output:', output3)
result3 = bubble_sort(nums3)
print('Actual output:', result3)
print('Match:', result3 == output3)

# Test 4
nums4, output4 = test4['input']['nums'], test4['output']
print('Input:', nums4)
print('Expected output:', output4)
result4 = bubble_sort(nums4)
print('Actual output:', result4)
print('Match:', result4 == output4)

# Test 5
nums5, output5 = test5['input']['nums'], test5['output']
print('Input:', nums5)
print('Expected output:', output5)
result5 = bubble_sort(nums5)
print('Actual output:', result5)
print('Match:', result5 == output5)

# Test 6
nums6, output6 = test6['input']['nums'], test6['output']
print('Input:', nums6)
print('Expected output:', output6)
result6 = bubble_sort(nums6)
print('Actual output:', result6)
print('Match:', result6 == output6)

# Test 7
nums7, output7 = test7['input']['nums'], test7['output']
print('Input:', nums7)
print('Expected output:', output7)
result7 = bubble_sort(nums7)
print('Actual output:', result7)
print('Match:', result7 == output7)

# Test 8
nums8, output8 = test8['input']['nums'], test8['output']
print('Input:', nums8)
print('Expected output:', output8)
result8 = bubble_sort(nums8)
print('Actual output:', result8)
print('Match:', result8 == output8)

# Test 9
# nums9, output9 = test9['input']['nums'], test9['output']
# print('Input:', nums9)
# print('Expected output:', output9)
# result9 = bubble_sort(nums9)
# print('Actual output:', result9)
# print('Match:', result9 == output9)
