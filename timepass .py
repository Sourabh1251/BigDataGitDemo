
def maxSubArrayWithXdiff(nums: list[int], x:int):
        
    currentMax = 0
    globalMax = 0
        
    start = 0

    globalStart = len(nums)-1
    globalEnd = 0
        
    for i in range(0, len(nums)-1):
        if(abs(nums[i]-nums[i+1]) <= x):
            currentMax += 1
            if(currentMax == 1):
                start = i
        else:
            currentMax = 0
    
        if(currentMax > globalMax):
            globalMax = currentMax
            globalStart = start
            globalEnd = i    

    for j in range(globalStart,globalEnd+2):
        print(nums[j], end = ",")
            

maxSubArrayWithXdiff([1,1,1,1,2,2,2,4,4,4,4,4,4,4,4,2,3,3,3,3,3], 0)