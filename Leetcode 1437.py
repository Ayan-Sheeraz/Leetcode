# 11/17/2025 : 17 nov 25 =>6:03pm
# 1437. Check If All 1's Are at Least Length K Places Away : EASY
# daily challenge

def seperate(nums , k):
    
    storer = []
    for loop in range(len(nums)):
        
        if nums[loop] == 1 :
            
            storer.append(loop)
    
    flag = True    
    for index in range(len(storer) - 1):
        
        diff = storer[index + 1] - storer[index] - 1
        
        if diff < k :
            flag = False
            
    print(flag)
            
        
        
seperate([1,0,0,0,1,0,0,1],2)
seperate([1,0,0,1,0,1], 2)
