# # arr =[1,4,7,5,9,70]

# #largeest
# print(sorted(arr)[-1])
# print(sorted(arr)[0])
# print(arr[::-1])
# print(sum(arr))
# print(sum(arr)//(len(arr)))

#sorted array

# arr= [7,1,5,9,2,3]
# arr= sorted(arr)

# def is_sorted(arr):
#     for i in range(len(arr)-1):
#         if arr[i]>arr[i+1]:
#             return "its not sorted array"
#     return "its sorted array"

# print(is_sorted(arr))

# arr= [1,1,2,3,3,5,7]
# def remove_duplicates(arr=arr):
#     seen=[]
#     duplicates=[]
#     for i in arr:
#         if i in seen:
#             duplicates.append(i)
#         else:
#             seen.append(i)

#     return seen

# print(remove_duplicates(arr))

#secondlargest
# def select_secondlargest(arr):
#    if len(arr)<2:
#       return None
#    max_no= max(arr)
#    wihout_max= [x for x in arr if x!= max_no]
#    return max(wihout_max)

# arr = [7, 1, 5, 9, 2, 3]
# print(select_secondlargest(arr))  # 7

#count occurance of element

# arr= [1,1,2,3,3,5,7]
# def count_ocuurance(arr):
#     count={}
#     for i in arr:
#         if i in count:
#             count[i]+=1
#         else:
#             count[i]=1
#     return count

# print(count_ocuurance(arr))

#zero at the end

# zeros= [1,1,0,5,0,0,0,67,5]
# # def move_all_zeroes(arr):
# #     return [x for x in arr if x!=0]+ [0]*arr.count(0)

# def move_all_zeroes(arr):
#     nonzeroes= [x for x in arr if x!=0]
#     zero= [x for x in arr if x==0]
#     return nonzeroes+zero
# print(move_all_zeroes(zeros))


# missing= [1,2,5,7,8]

# def missing_ele(arr):
#     missing= set(arr)
#     full= set([x for x in range(1,max(arr))])
#     result= full-missing
#     return result

# print(missing_ele(missing))

#merger two sorted arrays

# arr1= [1,3,5]
# arr2=[4,2,6]

# def merge_sorted_arrays(arr1,arr2):
#     merged= []
#     i=0
#     j=0
#     while i<len(arr1) and j<len(arr2):
#         if arr1[i]<=arr2[j]:
#             merged.append(arr1[i])
#             i+=1
#         else:
#             merged.append(arr2[j])
#             j+=1
#     merged.extend(arr1[i:])
#     merged.extend(arr2[j:])
#     return merged

# print(merge_sorted_arrays(arr1,arr2))

#find intersections of two arrays
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [3, 4, 5, 6, 7]
# def finding_intersection(arr1,arr2):
#     intersected=[]
#     seen=set()

#     for i in arr1:
#         if i in arr2:
#             if i not in seen:
#                 intersected.append(i)
#             else:
#                 seen.add(i)
#     return intersected

# print(finding_intersection(arr1,arr2))


# arr= [1,5,6,8,4,8]

# def roatate_array(arr,steps):
#     n= len(arr)
#     #normalise
#     k=steps%n

#     arr[:]=arr[-k:]+arr[:-k]
#     return arr

# print(roatate_array(arr,2))


# Find duplicates in array

# arr1 = [1, 2, 3,3,1,2, 4, 5]

# def find_duplicates(arr):
#     seen=set()
#     duplicates=set()
#     for i in arr:
#         if i in seen:
#             duplicates.add(i)
#         else:
#             seen.add(i)
#     return duplicates

# print(find_duplicates(arr1))


#kadanse lagorithm

# def kadane(arr):
#     current_sum=arr[0]
#     max_sum=arr[0]
#     for i in range(1,len(arr)):
#         current_sum= max(arr[i],current_sum+arr[i])
#         max_sum=max(max_sum,current_sum)
#     return max_sum
# arr = [-2, 1, -3, 4, -1, -2, 1, -5, 4]
# print(kadane(arr))


# find= [7,2,9,13,5]

# def find_pair(arr,target):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             sum= arr[i]+arr[j]
#             if sum==target:
#                 return [i,j]
#     return None
# print(find_pair(find,18))

# rearrange= [1, -2, 3, -4, 5, -6]

# def positive_neg(arr):
    
#     neg= [x for x in arr if x<0]
#     postive= [x for x in arr if x>=0]
#     liste=postive+neg
#     # for i in range(len(postive)):
#     #     liste.append(postive[i])
#     #     liste.append(neg[i])

#     return liste

# print(positive_neg(rearrange))
