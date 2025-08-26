# Two sum 01 easy
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Test
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))

# [0, 1]


# 02 Best Time to Buy and Sell Stock (LC 121)
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

# Test
prices = [7,1,5,3,6,4]
print(maxProfit(prices))
# output ---- 5


# 03 Maximum Subarray (Kadane’s Algorithm) (LC 53)
def maxSubArray(nums):
    max_sum = nums[0]
    curr_sum = 0
    
    for num in nums:
        curr_sum += num
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum

# Test
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
#output ----- 6

















