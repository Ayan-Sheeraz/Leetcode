## --> 9 oct 2025 10:33 pm
# leetcode 1451. Reaarrange words in a Sentence , medium

def arrangeWords(text):
    
    #########
    
    def bubbleSort(Array): # returns 2D Array!!!!!!
        
        for single in range(len(Array)):
            for double in range(len(Array)-1):
                
                if Array[double][1] > Array[double + 1][1] :
                    
                    tempRow = Array[double][0]
                    tempCol = Array[double][1] 
                    
                    Array[double][0] = Array[double + 1][0]
                    Array[double][1] = Array[double + 1][1]
                    
                    Array[double + 1][0] = tempRow
                    Array[double + 1][1] = tempCol
                    
        return(Array)    
    
    #########
    
    
    
    Base = []
    
    HP = 0
    TP = -1
    
    text = text + " "
    for loop in range (len(text)):
        
        if text[HP:HP+1] == " " :
            # print(HP)
            # print(TP)
            
            store = text[TP+1:HP]
            TP = HP
            
            Base.append(store)
            
        HP = HP + 1
        
    #print("base: ",Base)
    Superbase = [[0]*2 for i in range(len(Base))]
    
    for index in range(len(Base)):
        
        num = str(len(Base[index])) + str(index)
        Superbase[index][0] =  Base[index]
        Superbase[index][1] =  int(num)
    
    #print("superbase: ", Superbase)
    final = bubbleSort(Superbase)    
    #print("final: ",final)
    
    concat = ""
    for X in range(len(final)):
        
        concat = concat + final[X][0] + " "
        
    concat = concat[0:len(concat)-1]
    
    
    print(concat)    
    
    
 
text = "Leetcode is cool" 
text = "Keep calm and code on"          
text = " To be or not to be"
arrangeWords(text)           
                    
                    
                    
        
        