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
            nums = float(  str(len(extract)) + "." + str(c)  )
            ArrayLen.append(nums) 
        
            c = c + 1
            
    print("arraylen : ", ArrayLen)       
    """ TIME FOR EFFICIENT BUBBLE SORT """
    
    Noswaps = False
    Boundary = len(ArrayLen) - 1
    while Noswaps == False :
        
        Noswaps = True
        for loop in range(Boundary):
            
            if ArrayLen[loop] > ArrayLen[loop+1] :
                
                temp = ArrayLen[loop]
                ArrayLen[loop] = ArrayLen[loop + 1]      
                ArrayLen[loop + 1] = temp
                Noswaps = False
                
        Boundary = Boundary - 1
        
    """ FINISHED EFFICIENT BUBBLE SORT """
    print("arrayext : ", ArrayExt)
 
    EndArray = []
    
    for index in range(len(ArrayLen)):
        
        start = str(ArrayLen[index])
        
        ''' '''
        TP = 0
        
        while start[TP] != ".":
            TP = TP + 1
        
        
        ''' '''
        
        pos = int(   start[TP + 1 : len(start)]   )
        
        sorted = ArrayExt[pos]
       # print(sorted)
        EndArray.append(sorted)
    print("after arraylen : ", ArrayLen)
    print("before : ", EndArray)  
    EndArray[0] =(( EndArray[0] )[0]).upper()  +   ( EndArray[0] )[1:len(EndArray[0])]
    print("after : ", EndArray)  
    
    concat = ""
    for runner in range(len(EndArray)) :
        concat = concat + EndArray[runner] + " "
        
    concat = concat[0:len(concat)-1]
    print(concat)
        
    
  
  
# ArrangeWords("Keep calm and code on")       
# ArrangeWords("To be or not to be")  
#ArrangeWords("Thirty days challengue") 
ArrangeWords("Jtik hrzrvhbmk gbo cfhmiqwonj ojkew ufvledv bomoeqt ops jgi zdhvbpbb zczmepdfpm jry rjazc titttcu")        
             
        
        
    
   
            