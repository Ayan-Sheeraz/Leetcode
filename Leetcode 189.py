# 11/16/25 ==> 6:38 pm
# leetcode 189 : Rotate array

def rotate(nums,k):
    
    """  GOTTA DO THIS **INPLACE** """
    
    for loop in range(k):
        
        max = len(nums) - 1
        temp = nums[max]
      
        for index in range(max-1,-1,-1):
            
            nums[index + 1] = nums[index]
            
        nums[0] = temp
     
    
    print(nums)   
    
rotate([1,2,3,4,5,6,7],3)
            
        
        
    
    