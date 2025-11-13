# 11/12/2025 ==> 3:25
###  HAPPY BIRTHDAY TO ME !=! ###


def ArrangeWords(text):
    
    # text : today is my bday the cake was awesome
    #        0    5                               
    
    text = text + " " # for last words to be included 
    
    c = 0
    HP = 0
    TP = 0
    ArrayExt = []
    ArrayLen = []
    
    while HP != len(text) :
        
        TP = TP + 1
        
        if text[TP:TP+1] == " " :
            
            extract = text[HP:TP] # extraction without spacee
            HP = TP +1
            ArrayExt.append(extract.lower())
            nums = len(extract)
            ArrayLen.append(nums) 
         
            c = c + 1
            
    print("arraylen : ", ArrayLen) 
    AllOut = []       
            
    for one in range(len(ArrayLen)):
        
        first = ArrayLen[one]
        singleloop = [first]
        
        for two in range(one,len(ArrayLen)):
            
            second = ArrayLen[two]
            
            if first == second :
                
                singleloop.append(two)
                ArrayLen[two] = ""
        
        AllOut.append(singleloop)
    
        for corect in range(len(AllOut)):
            if AllOut[corect][0] == "" :
                AllOut.remove(AllOut[corect])        
        
    print(AllOut)
        
            
    
    
   
    
        
    """ TIME FOR EFFICIENT BUBBLE SORT """
    
    Noswaps = False
    Boundary = len(AllOut) - 1
    while Noswaps == False :
        
        Noswaps = True
        for loop in range(Boundary):
            print(loop)
            if AllOut[loop][0] > AllOut[loop+1][0] :
                
                temp = AllOut[loop]
                AllOut[loop] = AllOut[loop + 1]      
                AllOut[loop + 1] = temp
                Noswaps = False
                
        Boundary = Boundary - 1
        
    """ FINISHED EFFICIENT BUBBLE SORT """
    print("arrayext : ", ArrayExt)
 
    
        
    concat = ""   
    for row in range(len(AllOut)):
        for col in range(len(AllOut[row])-1):
            access = AllOut[row][col+1] 
            print(access)
            concat = concat + ArrayExt[access] + " "
    
    t = len(concat)
    concat = (concat[0]).upper() + concat[1:t-1]
    
    print( concat )
            
    
  
  
ArrangeWords("Keep calm and code on")       
# ArrangeWords("To be or not to be")  
ArrangeWords("Thirty days challengue") 
#ArrangeWords("Jtik hrzrvhbmk gbo cfhmiqwonj ojkew ufvledv bomoeqt ops jgi zdhvbpbb zczmepdfpm jry rjazc titttcu")        
             
        
        
    
   
            
    
    
    
        
    
            
            
        
    
    