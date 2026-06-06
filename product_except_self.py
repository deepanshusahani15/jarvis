def product_except_self(nums):
    total = 1

    for num in nums:
        total *= num

    #return [total // num for num in nums]
    result = []
    for num in nums:
    	result.append(total//num)
    return result

nums=[1,2,3,4]
print(product_except_self(nums))
