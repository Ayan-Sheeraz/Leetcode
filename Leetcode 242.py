# after doing leetcode 49 this is a piecfe of cake
# 3 jan 2026 => 3:49pm

    
def BubbleSort(Arr):
    
    Boundary = len(Arr) - 1
    for loop in range(len(Arr)):
        flag = True
        for index in range(Boundary):
            
            if Arr[index] > Arr[index + 1]:
                
                temp = Arr[index + 1]
                Arr[index + 1] = Arr[index]
                Arr[index] = temp
                flag = False
                
        if flag == True:
            break
                
    return Arr
            
            
def isAnagram(s, t):
    
    if len(s) != len(t):
        return False
    
    ArrayS = []
    for index in range(len(s)):
        
        element = s[index]
        ArrayS.append(element)
    
    CheckS = BubbleSort(ArrayS)
    
    ArrayT = []
    for index in range(len(t)):
        
        element = t[index]
        ArrayT.append(element)
    
    CheckT = BubbleSort(ArrayT)
    
    if CheckS == CheckT :
        return True
    else:
        return False
    
    
    
        
        
        
    