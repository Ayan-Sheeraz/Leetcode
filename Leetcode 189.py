# 11/16/25 ==> 6:38 pm
# leetcode 189 : Rotate array

def rotate(nums,k):
    
    """  GOTTA DO THIS **INPLACE** """
    
    for loop in range(len(nums)-1,len(nums)-k-1,-1):
        print(loop)
        temp = nums[loop]
        print("temp ; ", temp)
        for index in range(loop-1,-1,-1):
            
            nums[index + 1] = nums[index]
            
        nums[0] = temp
     
    
    print(nums)   
    
rotate([1,2,3,4,5,6,7],3)
            
        
        
    
    