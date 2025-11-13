## Leetcide 318 Maximum Product Of a Word Length : MEDIUM 
### 4 Oct 2025 3:43 pm --> AYAN SHEERAZ

def Max_Product(words):
    
    Array = []
    NumBase = [0] ## putting in zero because if no word get into it then output 0 [requiremnett]
        
    for upper in range(len(words)):
        
        st = upper
        for lower in range(st,len(words)):
            
            string = words[upper] + "*" + words[lower]
            Array.append(string) 
            
    # print(Array)
    
    for access in range(len(Array)):
        
        HP = 0
        TP = 0
        Full = Array[access]
        ##
        for loop in range(len(Full)):
            
            if Full[HP:HP+1] == "*" :
                
                firstWord = Full[TP:HP]
                secondWord = Full[HP+1:len(Full)]
                
                break
            HP = HP + 1
                
        ## 
        flag = True       
            
        for firstcheck in range(len(firstWord)):
            
            compare = firstWord[firstcheck:firstcheck+1]
            
            for deepX in range(len(secondWord)):
                
                other = secondWord[deepX:deepX+1]
                
                if other == compare :
                    
                    flag = False
                    break
            if flag == False:
                break
               
        
        if flag == True :
            
            calc = len(firstWord) * len(secondWord)
            NumBase.append(calc)           
                
    max = -123456789 
    for raid in range(len(NumBase)):
        
        if NumBase[raid] > max:
            max = NumBase[raid]
            
    
    print(max)
        
                   
            
            
            
    
  
             
             
Max_Product(["abcw","baz","foo","bar","xtfn","abcdef"])
Max_Product(["a","ab","abc","d","cd","bcd","abcd"])
Max_Product(["a","aa","aaa","aaaa"])
