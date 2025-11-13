# Leetcode 14, common prefix, level: easy

def common_prefix(strs):
    
    if strs == "":
        return ""
    
    else:
        Min = 2000 # 200 in the max lenght in question
        
        for loop in range(len(strs)):
            word = strs[loop]
            if len(word) < Min :
                
                Min_word = word
                
        concat = ""
        for index in range(len(Min_word)):
            
            alp = Min_word[index:index+1]
            count = 0
            for goall in range(len(strs)):
                
                their_alp = (strs[goall])[index:index+1]
                
                if their_alp == alp:
                    count = count + 1
                    
            
            if count == len(strs):
                concat = concat + alp  
            else:
                print(concat)
                break   
        
        
        print(concat) #### special case if all the words in strs are same then we need to output concat the aboive only does that when all words havea limites number of same prefix   
        
#a = ["flow","flower","flight"]
#a = ["ayan","aswad","ali","percy"]
a = ["a"]
common_prefix(a)