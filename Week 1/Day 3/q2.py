def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_sums = {0: 1}  # sum: frequency

    for num in nums:
        prefix_sum += num
        if (prefix_sum - k) in prefix_sums:
            count += prefix_sums[prefix_sum - k]
        prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1

    return count
