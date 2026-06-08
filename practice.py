# question=""""
#         Arrays & Lists (1–20)

# Find the largest element in an array
# Find the smallest element
# Reverse an array
# Find sum of all elements
# Find average of array
# Check if array is sorted
# Remove duplicates from array
# Find second largest element
# Count occurrences of an element
# Move all zeros to the end
# Find missing number in range 1–n
# Merge two sorted arrays
# Find the intersection of two arrays
# Rotate array by k steps
# Find duplicates in array
# Kadane’s Algorithm (max subarray sum)
# Find pair with given sum
# Find majority element (n/2 times)
# Rearrange positive and negative numbers
# Find longest increasing subarray


# 🔤 Strings (21–40)

# Reverse a string
# Check palindrome
# Count vowels and consonants
# Remove vowels from string
# Check anagram
# Count character frequency
# First non-repeating character
# Remove duplicates from string
# Convert string to integer (atoi)
# Check substring existence
# Longest common prefix
# Check rotation of string
# Capitalize first letter of each word
# Replace spaces with %20
# Count words in sentence
# Longest substring without repeat characters
# Validate palindrome ignoring symbols
# Compress string (aab → a2b1)
# Check balanced parentheses
# Find all permutations of string


# 🔁 Recursion (41–50)

# Factorial using recursion
# Fibonacci sequence
# Power of number (x^n)
# Sum of digits
# Reverse a string recursively
# Check palindrome recursively
# Find GCD using recursion
# Tower of Hanoi
# Generate all subsets
# Generate all permutations


# 📚 Stack & Queue (51–65)

# Implement stack using list
# Implement queue using list
# Valid parentheses
# Next greater element
# Reverse a stack
# Sort a stack
# Implement circular queue
# Evaluate postfix expression
# Min stack (retrieve min in O(1))
# First non-repeating character in stream
# Implement stack using queues
# Implement queue using stacks
# Sliding window maximum
# Check redundant brackets
# Largest rectangle in histogram


# 🔗 Linked Lists (66–80)

# Create a singly linked list
# Reverse linked list
# Detect loop in linked list
# Find middle of linked list
# Remove nth node from end
# Merge two sorted linked lists
# Check palindrome linked list
# Remove duplicates from sorted list
# Find intersection point of two lists
# Detect and remove loop
# Reverse linked list in groups of k
# Add two numbers using linked list
# Flatten a linked list
# Sort linked list (merge sort)
# Clone linked list with random pointers


# 🌳 Trees (81–90)

# Implement binary tree
# Inorder traversal
# Preorder traversal
# Postorder traversal
# Level order traversal
# Find height of tree
# Count nodes in tree
# Check if BST
# Lowest Common Ancestor
# Diameter of tree


# 🔍 Searching & Sorting (91–100)

# Binary search
# Linear search
# Bubble sort
# Selection sort
# Insertion sort
# Merge sort
# Quick sort
# Find kth smallest element
# Search in rotated sorted array
# Find peak element
# """


##finding largeest number in an array

# arr= [3,2,6,7,7,2,8,1,5]



# print("Highest number in array",sorted(arr)[-1])
# print("lowest number in array",sorted(arr)[0])
# print("Reversed array",arr[::-1])
# print("Sum of array",sum(arr))
# print("avg of array",((sum(arr)/len(arr))))
# print("len of array",len(arr))

########================================================================================================================================================================================================
# def is_sorted(arr):
#     for i in range(len(arr)-1):
#         if arr[i]>arr[i+1]:
#              return "this is not a sorted array"
#     return "this is a sorted array"
########================================================================================================================================================================================================
# print(is_sorted(arr))
########================================================================================================================================================================================================
# def remove_duplicates(arr):
#     seen=[] #using list for ordered output
#     duplicates=[]
#     for i in arr:
#         if i in seen:
#             duplicates.append(i)
#         else:
#             seen.append(i)
#     return "removed Duplicates",seen , "duplicates",duplicates


# print(remove_duplicates(arr))
########================================================================================================================================================================================================

# print(sorted(arr).pop(-2))
########================================================================================================================================================================================================
#count occurance


# from collections import Counter

# def count_ocr(arr,target):
#     Count = Counter(arr)
#     return Count[target]

# print(count_ocr(arr,2))

########================================================================================================================================================================================================
# def remove_and_to_end(arr,taget):
#     tar= taget
#     zeroes= [x for x in arr if x==tar]
#     non_zeroes= [x for x in arr if x!=tar]
#     result=non_zeroes+zeroes
#     return result

# print(remove_and_to_end(arr,7))
########================================================================================================================================================================================================

# missing= [1,2,3,5,7]
# def find_missing(arr):
#     arr=set(arr)
#     n= len(arr)
#     maximum= max(arr)
#     full= set([i for i in range(1,maximum+1)])
   
#     return  list(full-arr)

# print(find_missing(missing))
########================================================================================================================================================================================================
# unsorted_arr2= [1,3,5]
# unsorted_arr1= [2,4,6]

# def merge_unsorted_array(arr1,arr2):
#     result= []
#     i=0
#     j=0
#     while i<len(arr1) and j<len(arr2):
#         if arr1[i]<=arr2[j]:
#             result.append(arr1[i])
#             # print("i",arr1[i])
#             i+=1
#             print("\n\t\ti - result ",result)
        
#         else:
#             result.append(arr2[j])
#             # print("j",arr2[j])
#             j+=1
#             print("\nJ - Result",result)
          
            
#     result.extend(arr1[i:])
#     result.extend(arr2[j:])
#     return result

# print(merge_unsorted_array(unsorted_arr1,unsorted_arr2))
########================================================================================================================================================================================================
#### find the intersection of two arrays
# arr1= [1,2,3,5]
# arr2= [1,5,7,8]

### def intersection(arr1, arr2):
# ##    return 

# ###print(intersection(arr1,arr2))

# def intersection(arr1, arr2):
#     from collections import Counter
#     count= Counter(arr1)
#     result=[]                                                                                                       #need to understand this 
#     for num in arr2:
#         if count[num]>0:
#             result.append(num)
#             count[num] -= 1
#     return result

# print(intersection(arr1,arr2))

########================================================================================================================================================================================================
## Rotate array by K Steps

# def rotate_array(nums, k):
#     k= k%len(arr)
#     nums[:]=nums[-k:]+nums[:-k]

# # Example
# arr = [1, 2, 3, 4, 5, 6, 7]
# rotate_array(arr, 3)
# print(arr)  # [5, 6, 7, 1, 2, 3, 4]

########================================================================================================================================================================================================
# array1= [1,2,3,2,4,3,5]

# def find_duplicates(arr):
#     seen= set()
#     duplicate= set()
#     for num in arr:
#         if num in seen:
#             duplicate.add(num)
#         else:
#             seen.add(num)
#     return list(duplicate)

# print(find_duplicates(array1))
########================================================================================================================================================================================================
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# def kadane(nums):
#     # Start with first number
#     current_sum = nums[0]
#     max_sum = nums[0]
    
#     # Walk through the rest
#     for i in range(1, len(nums)):
#         # Decision: continue or start fresh?
#         current_sum = max(nums[i], current_sum + nums[i])
        
#         # Update best ever
#         max_sum = max(max_sum, current_sum)
    
#     return max_sum


# # Example
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(kadane(nums))  # Output: 6 [web:83][web:88]

# print(max_subarray(nums))
########================================================================================================================================================================================================
# #find a pair with given sum

# def find_pair(arr, target):
#     seen = set()  # Empty set
    
#     for num in arr:
#         need = target - num  # What number we need
        
#         if need in seen:     # Did we see it before?
#             return (need, num)
#         #                                                                                   #need to practice this
#         seen.add(num)        # Add current number
    
#     return None  # No pair found


# # Test
# arr = [2, 7, 3, 8, 5, 1]
# print(find_pair(arr, 10))  # (3, 7)

########================================================================================================================================================================================================
### Find majority element (n/2 times)
# def find_majority(arr):
#     counts = {}
    
#     # Count how many times each number appears
#     for num in arr:
#         counts[num] = counts.get(num, 0) + 1
    
#     # Find the one that appears more than half
#     for num, count in counts.items():
#         if count > len(arr) // 2:
#             return num
#                                                                                                     #### Need to practice
#     return None


# # Example
# arr = [3, 3, 4, 2, 3, 3, 3]
# print(find_majority(arr))  # Output: 3




########================================================================================================================================================================================================
###Rearrange positive and negative numbers

# def rearrange(arr):
#     pos= [x for x in arr if x>0]
#     neg= [x for x in arr if x<0]
   

#     result=[]

#     i=0
#     j=0
# #                                                                                                     #### Need to practice
#     while i<len(pos) and j<len(neg):
#         result.append(pos[i])
#         i+=1
#         result.append(neg[j])
#         j+=1

#     result.extend(pos[i:])
#     result.extend(neg[j:])
#     return result

# arr = [3, -2, 4, -1, -5, 2]
# print(rearrange(arr))


########================================================================================================================================================================================================
### Find longest increasing subarray

# arr= [1,2,6,0,7]
# def longest_increasing_subarray(arr):
#     if len(arr)==0:
#         return 0
#     max_length= 1
#     curren_lenght= 1

#     for i in range(1,len(arr)):
#         if arr[i]>arr[i-1]:
#             curren_lenght+=1
#             max_length= max(max_length,curren_lenght)
#         else:
#             curren_lenght=1
#     return max_length


# """
# explaination

# arr = [1, 2, 6, 0, 7]

# i=1: arr[1]=2 > arr[0]=1 → current=2, max=2
# i=2: arr[2]=6 > arr[1]=2 → current=3, max=3
# i=3: arr[3]=0 < arr[2]=6 → current=1 (RESET!)
# i=4: arr[4]=7 > arr[3]=0 → current=2, max=3

# Result: 3 ✓
# """

# print(longest_increasing_subarray(arr))
########================================================================================================================================================================================================

                                                                            ###***string***

##Reverse a string
# string= "Avinash"
# def reverse_string(sting):
#     result=""
#     for i in string:
#         result= i+ " "+ result
#     return result

# print(reverse_string(string))
########================================================================================================================================================================================================
# palin= "madam"

# def check_palindrome(strings):
#     if strings == strings[::-1]:
#         return "its a palindrome string"
#     return "its not a palindrome string"

# print(check_palindrome(palin))

########================================================================================================================================================================================================
#Count vowels and consonants

# def count_vowels(text):
#     text= text.lower()
#     vowels= "aeiou"
#     vowel_count= 0
#     consontant_count=0
#     for char in text:
#         if char in vowels:
#             vowel_count+=1
#         else:
#             consontant_count+=1
#     return f"vowel Count:{vowel_count},\ncounsonatant count:{consontant_count}"

# text= "Hello"
# print(count_vowels(text))

########================================================================================================================================================================================================
# def remove_vowels(text):
#     text=text.lower()
#     vowels= "aeiou"
#     removed= ""
#     for char in text:
#         if char not in vowels:
#             removed+=char
#     return removed

# text="Hello"
# print(remove_vowels(text))

    
########================================================================================================================================================================================================
##check nagaram

# def check_anagram(string1,string2):
#     from collections import Counter
#     if Counter(string1.replace(" ","").lower())==Counter(string2.replace(" ","").lower()):
#         return "this is an anagram"
#     return " this is not an anagram"

# print(check_anagram("listen","silent"))
########================================================================================================================================================================================================
## Count Character Frequency

# def count_char_frquency(text):
#     freq={}
#     for char in text:
#         if char in freq:
#             freq[char]+=1
#         else:
#             freq[char]=1
#     return freq

# text= "Hello world".replace(" ","").lower()
# print(count_char_frquency(text))


########================================================================================================================================================================================================
##non repeating charcter

# def count_char_frquency(text):
#     freq={}
#     non_repeat=[]
#     for char in text:
#         if char in freq:
#             freq[char]+=1
#         else:
#             freq[char]=1
    
#     for chr in text:
#         if freq[chr]==1:
#             non_repeat.append(chr)
#     return non_repeat[0]
# text= "Hello world".replace(" ","").lower()
# print(count_char_frquency(text))

########================================================================================================================================================================================================
## remove duplicates from string

# def remove_duplicates(s):
#     s=s.replace(" ","").lower()
#     seen= ""
#     duplicates=""
#     for char in s:
#         if char in seen:
#             duplicates+= char 
#         else:
#             seen+=char
#     return seen

# text= "hellow world"
# print(remove_duplicates(text))

########================================================================================================================================================================================================
## converting a string to integer

# def my_atoi(s):
#     s = s.strip()  # Remove leading whitespace
    
#     if not s:
#         return 0
    
#     # Handle sign
#     sign = 1
#     index = 0
    
#     if s[0] == '-':
#         sign = -1
#         index = 1
#     elif s[0] == '+':
#         index = 1
    
#     # Build number from digits
#     result = 0
#     INT_MAX = 2**31 - 1   # 2147483647
#     INT_MIN = -2**31      # -2147483648
    
#     for i in range(index, len(s)):
#         if s[i].isdigit():
#             result = result * 10 + int(s[i])
#         else:
#             break  # Stop at non-digit
    
#     # Apply sign
#     result *= sign
    
#     # Clamp to 32-bit range
#     if result < INT_MIN:
#         return INT_MIN
#     if result > INT_MAX:
#         return INT_MAX
    
#     return result


# # Test
# print(my_atoi("42"))                  # Output: 42
# print(my_atoi("  -42"))               # Output: -42
# print(my_atoi("4193 with words"))     # Output: 4193 [web:236]
# print(my_atoi("-91283472332"))        # Output: -2147483648 (clamped)
# print(my_atoi("words and 987"))       # Output: 0



""""
s = "  -42"

Step 1: s = s.strip() → "-42"

Step 2: Check sign
        s[0] = '-' → sign = -1, index = 1

Step 3: Build number (loop from index 1)
        i=1: s[1]='4' → result = 0*10 + 4 = 4
        i=2: s[2]='2' → result = 4*10 + 2 = 42

Step 4: Apply sign
        result = 42 * (-1) = -42

Step 5: Clamp (not needed)
        -42 is in range [-2147483648, 2147483647]

Result: -42
"""
########================================================================================================================================================================================================
#finding substring or text in text or sentence
# s= "hello world"
# ss= "world"
# def find_subtring(s,sub):
#     return sub in s
# print(find_subtring(s,ss))

########================================================================================================================================================================================================
## longest common prefix

# def longest_common_prefix(strings):
#     if not strings:
#         return ""
    
#     prefix= strings[0]
    
#     for i in range(1,len(strings)):
#         while not strings[i].startswith(prefix):
#             prefix= prefix[:-1]
#             if not prefix:
#                 return ""
#     return prefix

# print(longest_common_prefix(["apple", "app", "application"]))  # "app"
# print(longest_common_prefix(["hello", "hell", "help"]))        # "hel"
# print(longest_common_prefix(["cat", "dog", "bird"]))           # ""
# print(longest_common_prefix(["single"]))                       # "single"
########================================================================================================================================================================================================
##check rotating string

# def is_rotation(s1,s2):
#     if len(s1)!=len(s2) and len(s1)==0:
#         return False
    
#     return s2 in (s1+s1)

# print(is_rotation("abc", "cab"))        # True
# print(is_rotation("abc", "acb"))        # False
# print(is_rotation("", ""))              # False (empty strings)
# print(is_rotation("a", "a"))    

########================================================================================================================================================================================================
###capitalize first letter of each workd

# print("helo world".title())
########================================================================================================================================================================================================
### Replace Spaces with %20
# def replace_spaces(text):
#     return text.replace(" ", "%20")


# # Test
# print(replace_spaces("hello world"))              # Output: "hello%20world"
# print(replace_spaces("python programming"))       # Output: "python%20programming"
# print(replace_spaces("hello   world"))            # Output: "hello%20%20%20world"

########================================================================================================================================================================================================
### word in sentence
# def count_words(sentence):
#     return len(sentence.split())


# # Test
# print(count_words("hello world"))                     # Output: 2
# print(count_words("python is fun"))                   # Output: 3
# print(count_words("hello   world"))                   # Output: 2
# print(count_words("Learning Python step by step"))    # Output: 5 [web:297]
########================================================================================================================================================================================================
### longest substring in without repeat characters
# def longest_unique_substring(s):
#     char_set=set()
#     left=0
#     max_length=0

#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left+=1

#         char_set.add(s[right])

#         max_length= max(max_length,right-left+1)
#     return max_length

# # Test
# print(longest_unique_substring("abcabcbb"))  # Output: 3 [web:306]
# print(longest_unique_substring("bbbbb"))     # Output: 1
# print(longest_unique_substring("pwwkew")) 

########================================================================================================================================================================================================
##Validate palindrome ignoring symbols

# s= "A man, a plan, a canal: Panama"
# def is_valid_palindrome(s):
#     filtered= "".join(char.lower() for char in s if char.isalnum())
#     # print(filtered)
#     return filtered==filtered[::-1]

# print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # True [web:312]
# print(is_valid_palindrome("race a car"))                        # True
# print(is_valid_palindrome("hello"))                             # False
# print(is_valid_palindrome("Mr. Owl ate my metal worm"))  
########================================================================================================================================================================================================
### Compress string (aab → a2b1)

# def compress_string(s):
#     if not s:
#         return ""
    
#     compressed=""
#     count=1
#     for i in range(1,len(s)):
#         if s[i]== s[i-1]:
#             count+= 1
#         else:
#             compressed+= s[i-1]+str(count)
#             count=1
#     compressed += s[-1] + str(count)
#     return compressed

# print(compress_string("aab"))              # Output: "a2b1"
# print(compress_string("aaabbbaac"))        # Output: "a3b3a2c1"
# print(compress_string("abcdef")) 


# """
# s = "aab"

# count = 1
# compressed = ""

# i=1: s[1]='a' == s[0]='a' → count = 2
# i=2: s[2]='b' != s[1]='a' → compressed = "a2", count = 1

# End loop: compressed = compressed + s[-1] + str(count)
#         = "a2" + "b" + "1" = "a2b1" ✓
# """

########================================================================================================================================================================================================
###Check balanced parentheses

# def is_balanced(s):
#     stack=[]
#     pairs={')':'(',
#            '}':'{',
#            ']':'['}
    
#     for char in s:
#         if char in '({[':
#             stack.append(char)
#         elif char in ']})':
#             if not stack or stack[-1]!=pairs[char]:
#                 return False
#             stack.pop()
#     return len(stack)==0

# print(is_balanced("()"))              # True
# print(is_balanced("{[]}"))            # True
# print(is_balanced("([{}])"))          # True
# print(is_balanced("([)]"))            # False [web:332][web:336]
# print(is_balanced("(")) 


# """
# s = "([{}])"

# stack = []

# i=0: char='(' → push → stack=['(']
# i=1: char='[' → push → stack=['(', '[']
# i=2: char='{' → push → stack=['(', '[', '{']
# i=3: char='}' → closing → check stack[-1]='{' matches → pop → stack=['(', '[']
# i=4: char=']' → closing → check stack[-1]='[' matches → pop → stack=['(']
# i=5: char=')' → closing → check stack[-1]='(' matches → pop → stack=[]

# End: stack is empty → True ✓
# """

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

########================================================================================================================================================================================================

