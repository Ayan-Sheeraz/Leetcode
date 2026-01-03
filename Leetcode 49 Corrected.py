# Second ttimes the charm lets bring this anagram nonsense to an end
# 3 jan 2026 => 2:27pm

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
            
   
    
    
    
    
def groupAnagram(strs):
    
    # Stage 1: Make Array Caliph
    
    ArrayCaliph = [[""] * 2 for i in range(len(strs))]
    
    for loop in range(len(strs)):
        ArrayCaliph[loop][0] = strs[loop]
        
    
    for index in range(len(strs)):
        
        element = strs[index]
        ArrayBubble = []
        
        for breaking in range(len(element)):
            ArrayBubble.append(element[breaking])
        
        sorted = BubbleSort(ArrayBubble)
        concat = ""
        for combine in range(len(sorted)):
            concat = concat + sorted[combine]
        
        
        ArrayCaliph[index][1] = concat
        
    print("ArrayCaliph: ", ArrayCaliph)
        
        
    """ ** ArrayCaliph in the position i wanted it to be ** """
    ArrayAmeer = []
    
    for outer in range(len(ArrayCaliph)):
        
        element = ArrayCaliph[outer][1]
        ArrayQazi = []
        
        if element != "$" :
            
            for inner in range(outer, len(ArrayCaliph)):
                
                if element == ArrayCaliph[inner][1] :
                    
                    ArrayQazi.append(ArrayCaliph[inner][0])
                    ArrayCaliph[inner][1] = "$"
                    
            
            ArrayAmeer.append(ArrayQazi)
        
    
    print("ArrayAmeer: ", ArrayAmeer)
            
        
        
groupAnagram(["eat","tea","tan","ate","nat","bat"])
groupAnagram([""])
groupAnagram(["a"])
                    
    
    
    