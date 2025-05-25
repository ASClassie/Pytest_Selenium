'''Leet Code Easy Problem'''
from calendar import firstweekday
from math import remainder

'''Two Sum'''
# class Solution:
#     def twoSum(self, nums, target):
#         seen ={}
#
#         for index,num in enumerate(nums):
#             complement = target- num
#             if complement in seen:
#                 return [seen[complement],index]
#             seen[num]=index
#
#
#
#
# c = Solution()
# print(c.twoSum([2,7,11,15],18))

'''Remove Duplicates from Sorted Array it uses a two pointer approach so it's difficuilt'''

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return
#         i=0
#         for j in range(1,len(nums)):
#             if nums[i]!=nums[j]:
#                 i+=1
#                 nums[i]=nums[j]
#         return i+1
#
# c = Solution()
# print(c.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


'''Pallindrome number'''

# def isPalindrome(x):
#     """
#     :type x: int
#     :rtype: bool
#     """
#
#     num = x
#     reverse_number = ""
#
#     while num > 0:
#         remainder = num % 10
#         reverse_number += str(remainder)
#         num = num // 10
#
#     return reverse_number == str(x) or x==0
#
#
# print(isPalindrome(121))

# def arm_strong_number(number):
#     digit_power = len(str(number))
#     total, last_digit = 0, 0
#     checker = number
#     while checker > 0:
#         last_digit = checker % 10
#         total = total + last_digit ** digit_power
#         checker = checker // 10
#         last_digit = 0
#     return total == number
#
#
# print(arm_strong_number(1634))

# def anagram(arr):
#     groups = {}
#     for s in arr:
#         sorted_s = "".join(sorted(s))
#         if sorted_s in groups:
#             groups[sorted_s].append(s)
#
#         else:
#             groups[sorted_s] = [s]
#
#     return list(groups.values())
#
# print(anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))


# def target_sum(arr, target):
#     seen = {}
#     for index, num in enumerate(arr):
#         compliment = target - num
#         if compliment in seen:
#             return [seen[compliment],index]
#         else:
#             seen[num] = index
#
# print(target_sum([2, 7, 11, 15], 9))


'''Python Coding Problem: First Unique Character in a String'''

# def first_non_repeating_char(s):
#     d = {}
#     for char in s:
#         d[char] = d.get(char,0)+1
#
#     for index,char in enumerate(s):
#         if d[char] == 1:
#             return index
#
#     return -1
#
# print(first_non_repeating_char('lleetcode'))

'''Python Coding Problem: Valid Palindrome'''
#
# def valid_palindrome(sentence):
#     sentence = "".join(s.lower() for s in sentence if s.isalnum())
#     print(sentence)
#     return sentence == sentence[::-1]
#
# print(valid_palindrome("A man, a plan, a canal: Panama"))

'''Python Coding Problem: Missing Number'''

# def missing_number(nums):
#     last = len(nums)
#     seen = set(nums)
#     for i in range(last):
#         if i not in seen:
#             return i
#
#
# print(missing_number([9,6,4,2,3,5,7,0,1]))

# def find_missing_number_math(nums):
#     n = len(nums)
#     expected_sum = n * (n + 1) // 2
#
#     actual_sum = sum(nums)
#     missing_element = expected_sum - actual_sum
#     return missing_element
#
#
# print(find_missing_number_math([9, 6, 4, 2, 3, 5, 7, 0, 1]))


'''Global Logics: Interview Question'''
'''
input = "Robert000Smith000123"
output = { “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }
'''

# def dict_creation(sentence):
#     sentence = sentence.split("000")
#     d = {'first_name': sentence[0],
#          'last_name': sentence[1],
#          'id': sentence[2]}
#
#     return d
# print(dict_creation("Robert000Smith000123"))

'''Write a program to reverse the number without str typecasting'''

# def reverse_number(num):
#     reversed_digit = 0
#     while num > 0:
#         last_digit = num % 10
#         reversed_digit = reversed_digit * 10 + last_digit
#         num = num // 10
#     return reversed_digit
#
#
# print(reverse_number(1234))

'''Deloitte: Interview Question'''

'''Write a program to reverse the string while preserving the spaces'''

# def reverse_string_with_spaces(s):
#     sorted_char = "".join([char for char in s if char != " "])[::-1]
#     s = list(s)
#     j = 0
#     for i in range(len(s)):
#         if s[i] != " ":
#             s[i] = sorted_char[j]
#             j += 1
#     return "".join(s)
#
#
# print(reverse_string_with_spaces('a b c d'))

'''Input: "Hello, World,  python3,  Hello, CODING123"
Output: ['coding', 'hello', 'python', 'world']'''
'''Write a function that takes a comma-separated string of words (with possible extra spaces),
 and returns a list of unique words in alphabetical order, with all letters converted to lowercase
  and any digits removed.'''


# def task1(s):
#     cleaned_words =[''.join(c for c in word.strip().lower() if not c.isdigit()) for word in s.split(',')]
#
#     return sorted(set(cleaned_words))
#
#
# print(task1("Hello, World,  python3,  Hello, CODING123"))

'''Exercise 2: Dictionary Manipulation and Lambda Functions
Write a function that takes a dictionary and a threshold value, and returns a new dictionary containing
only key-value pairs where the value is greater than the threshold. Implement this in two '''
'''Using a dictionary comprehension
Using the filter() function with a lambda expression'''

'''Input: {'a': 5, 'b': 2, 'c': 8, 'd': 1}, threshold=3
Output: {'a': 5, 'c': 8}'''


# def task2(d, threshold):
#     '''First Method'''
#     result = {key: value for key, value in d.items() if value > threshold}
#     print(result)
#     '''Second method'''
#     a = dict(filter(lambda value: value[1] > threshold, d.items()))
#     print(a)
#
#
# task2({'a': 5, 'b': 2, 'c': 8, 'd': 1}, threshold=3)

'''Exercise 3: Working with Sets and List Operations
You are given two lists of integers. Write a function that returns:

A list of integers that appear in both lists (intersection)
A list of integers that appear in either list, but not both (symmetric difference)
A list of integers that appear in the first list but not the second (difference)

Implement this using Python's set operations and list methods. Also, ensure your final output lists are sorted in ascending order.'''

'''Input: list1 = [1, 2, 3, 4, 5], list2 = [3, 4, 5, 6, 7]
Output: 
- Intersection: [3, 4, 5]
- Symmetric difference: [1, 2, 6, 7]
- Difference (list1 - list2): [1, 2]'''

# def task_sets_list_operations(l1,l2):
#     s1= set(l1)
#     s2 =set(l2)
#     print(s1.intersection(s2))
#     print(s1.symmetric_difference(s2))
#     print(s1-s2)
#
# task_sets_list_operations([1, 2, 3, 4, 5],[3, 4, 5, 6, 7])

'''Exercise 4: Generator Functions and File Processing
Write a function called process_log that simulates processing a log file. Your function should:'''

logs = """[INFO] 2023-05-10 10:15:32 - User login successful
[ERROR] 2023-05-10 10:16:43 - Database connection failed
[WARNING] 2023-05-10 10:17:15 - High memory usage detected"""
#
# def process_log(entry_logs,level_filter=None):
#      overall_logs= entry_logs.strip().split('\n')
#      for line in overall_logs:
#          level = line[1:line.index(']')]
#
#          rest = line[line.index(']')+2:]
#
#          time_stamp,message= rest.split(' - ',1)
#
#          log_entry = {'level':level,'timestamp':time_stamp,'message':message}
#
#          if level_filter is None or level == level_filter:
#              yield log_entry
#
# for entry in process_log(logs,level_filter="ERROR"):
#     print(entry)


'''Exercise 5: Functional Programming with map() and filter()'''
'''Write a function called process_names that takes a list of full names (first and last name) and performs the following operations:

Filter out any names where the first name or last name is shorter than 3 characters
Convert all names to title case (first letter of each word capitalized)
Create a new list where each entry is formatted as "Last, First"

Use the map() and filter() functions (no list comprehensions) to implement this functionality.'''

'''Example:
Input: ["john doe", "bo jackson", "JANE SMITH", "robert j williams"]
Output: ["Doe, John", "Jackson, Bo", "Smith, Jane"]
Note that "robert j williams" was filtered out because the middle initial "j" is considered a separate word and is less than 3 characters.
Try implementing this using functional programming concepts!'''


def process_names(names):
    filtered_names = list(filter(lambda name:all((len(word)>=3 for word in name.split())),names))
    print(filtered_names)

process_names(["john doe", "bo jackson", "JANE SMITH", "robert j williams"])



