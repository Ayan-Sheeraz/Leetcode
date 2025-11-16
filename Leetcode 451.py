# 16 nov 2025 ==> 6:00 pm
# leetcode 451 : Sort Characters By Frequency

def frequencySort(s):
    
    repeat = []
    for loop in range(len(s)):
        
        char = s[loop]
        repeat.append(char)
     
    # print("repeat: ", repeat)
    
    ArrayStore = []
    # [[a,3,aaa],[y,1,y],[e,2,ee]]
    
    for one in range(len(repeat)):
        
        count = 0
        concat = ""
        first = repeat[one]
        
        for two in range(one,len(repeat)):
            
            second = repeat[two]
            
            if first == second :
                
                count = count + 1
                concat = concat + first
                
                repeat[two] = ''
        
               
        temp = [first,count,concat]
       # print(temp)
        ArrayStore.append(temp)
        
    
    #print("ArrayStore: ", ArrayStore)  # Success
    
    
    
    """ TIME FOR EFFICIENT BUBBLE SORT """
    
    Noswaps = False
    Boundary = len(ArrayStore) - 1
    while Noswaps == False :
        
        Noswaps = True
        for loop in range(Boundary):
           
            if ArrayStore[loop][1] < ArrayStore[loop+1][1] :
                
                temp = ArrayStore[loop]
                ArrayStore[loop] = ArrayStore[loop + 1]      
                ArrayStore[loop + 1] = temp
                Noswaps = False
                
        Boundary = Boundary - 1
        
    """ FINISHED EFFICIENT BUBBLE SORT """
    
    # print("efficient Arraystore: ", ArrayStore)
    
    
    text = ""
    
    for finale in range(len(ArrayStore)):
        
        text = text + ArrayStore[finale][2]
        
    
    print("text: ", text)
        
    
                

        
# frequencySort("ayansheeraz")
frequencySort("tree")
frequencySort("Aabb")
    