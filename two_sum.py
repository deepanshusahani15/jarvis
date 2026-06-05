def twoSum(nums,target):

    mp={}

    for i,num in enumerate(nums):

        need=target-num

        if need in mp:
            return [mp[need],i]

        mp[num]=i

if __name__ == "__main__":
	nums = [2,7,11,15]
	target = 9
	result = twoSum(nums,target)
	print(result)
