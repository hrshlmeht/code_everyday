# print('Enter the size of the array')
# arr_size = int(input())
# nums =[]
# for j in range(arr_size):
#     print('Enter the element')
#     nums.append(input())
#
#
# print (nums)
# robber_1 = 0
# robber_2 = 0
# for i in nums:
#     temp = max(robber_1 + int(i) , robber_2)
#     robber_1 = robber_2
#     robber_2 = temp
# # return robber_2
# print (robber_2)

print('Enter the string to check the palindrome')
x = input()

reverse_x = x[::-1]
print(reverse_x)
if reverse_x == x:
    print('The entered string is a palindrome')
else:
    print('The entered string is not a paindrome')


