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

# # Test 1
# print("Running Test 1...")
# nums1, output1 = test1['input']['nums'], test1['output']
# print('Input:', nums1)
# print('Expected output:', output1)
# result1 = bubble_sort(nums1)
# print('Actual output:', result1)
# print('Match:', result1 == output1)
# print()

# # Test 2
# print("Running Test 2...")
# nums2, output2 = test2['input']['nums'], test2['output']
# print('Input:', nums2)
# print('Expected output:', output2)
# result2 = bubble_sort(nums2)
# print('Actual output:', result2)
# print('Match:', result2 == output2)
# print()

# # Test 3
# print("Running Test 3...")
# nums3, output3 = test3['input']['nums'], test3['output']
# print('Input:', nums3)
# print('Expected output:', output3)
# result3 = bubble_sort(nums3)
# print('Actual output:', result3)
# print('Match:', result3 == output3)
# print()

# # Test 4
# print("Running Test 4...")
# nums4, output4 = test4['input']['nums'], test4['output']
# print('Input:', nums4)
# print('Expected output:', output4)
# result4 = bubble_sort(nums4)
# print('Actual output:', result4)
# print('Match:', result4 == output4)
# print()

# # Test 5
# print("Running Test 5...")
# nums5, output5 = test5['input']['nums'], test5['output']
# print('Input:', nums5)
# print('Expected output:', output5)
# result5 = bubble_sort(nums5)
# print('Actual output:', result5)
# print('Match:', result5 == output5)
# print()

# # Test 6
# print("Running Test 6...")
# nums6, output6 = test6['input']['nums'], test6['output']
# print('Input:', nums6)
# print('Expected output:', output6)
# result6 = bubble_sort(nums6)
# print('Actual output:', result6)
# print('Match:', result6 == output6)
# print()

# # Test 7
# print("Running Test 7...")
# nums7, output7 = test7['input']['nums'], test7['output']
# print('Input:', nums7)
# print('Expected output:', output7)
# result7 = bubble_sort(nums7)
# print('Actual output:', result7)
# print('Match:', result7 == output7)
# print()

# # Test 8
# print("Running Test 8...")
# nums8, output8 = test8['input']['nums'], test8['output']
# print('Input:', nums8)
# print('Expected output:', output8)
# result8 = bubble_sort(nums8)
# print('Actual output:', result8)
# print('Match:', result8 == output8)
# print()

# Test 9
# nums9, output9 = test9['input']['nums'], test9['output']
# print('Input:', nums9)
# print('Expected output:', output9)
# result9 = bubble_sort(nums9)
# print('Actual output:', result9)
# print('Match:', result9 == output9)


#insertion sort
def insertion_sort(nums):
    nums= list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >=0 and nums[j] > cur:
            j-=1
        nums.insert(j+1, cur)
    return nums

# # Test 1
# print("Running Test 1...")
# nums1, output1 = test1['input']['nums'], test1['output']
# print('Input:', nums1)
# print('Expected output:', output1)
# result1 = bubble_sort(nums1)
# print('Actual output:', result1)
# print('Match:', result1 == output1)
# print()

# # Test 2
# print("Running Test 2...")
# nums2, output2 = test2['input']['nums'], test2['output']
# print('Input:', nums2)
# print('Expected output:', output2)
# result2 = bubble_sort(nums2)
# print('Actual output:', result2)
# print('Match:', result2 == output2)
# print()

# # Test 3
# print("Running Test 3...")
# nums3, output3 = test3['input']['nums'], test3['output']
# print('Input:', nums3)
# print('Expected output:', output3)
# result3 = bubble_sort(nums3)
# print('Actual output:', result3)
# print('Match:', result3 == output3)
# print()

# # Test 4
# print("Running Test 4...")
# nums4, output4 = test4['input']['nums'], test4['output']
# print('Input:', nums4)
# print('Expected output:', output4)
# result4 = bubble_sort(nums4)
# print('Actual output:', result4)
# print('Match:', result4 == output4)
# print()

# # Test 5
# print("Running Test 5...")
# nums5, output5 = test5['input']['nums'], test5['output']
# print('Input:', nums5)
# print('Expected output:', output5)
# result5 = bubble_sort(nums5)
# print('Actual output:', result5)
# print('Match:', result5 == output5)
# print()

# # Test 6
# print("Running Test 6...")
# nums6, output6 = test6['input']['nums'], test6['output']
# print('Input:', nums6)
# print('Expected output:', output6)
# result6 = bubble_sort(nums6)
# print('Actual output:', result6)
# print('Match:', result6 == output6)
# print()

# # Test 7
# print("Running Test 7...")
# nums7, output7 = test7['input']['nums'], test7['output']
# print('Input:', nums7)
# print('Expected output:', output7)
# result7 = bubble_sort(nums7)
# print('Actual output:', result7)
# print('Match:', result7 == output7)
# print()

# # Test 8
# print("Running Test 8...")
# nums8, output8 = test8['input']['nums'], test8['output']
# print('Input:', nums8)
# print('Expected output:', output8)
# result8 = bubble_sort(nums8)
# print('Actual output:', result8)
# print('Match:', result8 == output8)
# print()


def merge(nums1, nums2, depth=0):
    print('  '*depth, 'merge:', nums1, nums2)
    i, j, merged = 0, 0, []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    return merged + nums1[i:] + nums2[j:]
        
def merge_sort(nums, depth=0):
    print('  '*depth, 'merge_sort:', nums)
    if len(nums) < 2: 
        return nums
    mid = len(nums) // 2
    return merge(merge_sort(nums[:mid], depth+1), merge_sort(nums[mid:], depth+1),depth+1)


#Question1Answer
class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes  
    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)

nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]

def compare_likes(nb1, nb2):
    if nb1.likes < nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    else:
        return 'greater'

def compare_titles(nb1, nb2):
    if nb1.title < nb2.title:
        return 'lesser'
    elif nb1.title == nb2.title:
        return 'equal'
    else:
        return 'greater'

def merge_sort(objs, compare=compare_titles):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge(
        merge_sort(objs[:mid], compare), 
        merge_sort(objs[mid:], compare), 
        compare
    )

def merge(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result in ('lesser', 'equal'):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]

# Sort by title
sorted_by_title = merge_sort(notebooks, compare_titles)
print("Sorted by Title:", sorted_by_title)

# Sort by likes
sorted_by_likes = merge_sort(notebooks, compare_likes)
print("Sorted by Likes:", sorted_by_likes)
