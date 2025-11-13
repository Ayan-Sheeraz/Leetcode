#LEETCODE 394 --> fri 3 oct 2:46 pm
# medium level - Decode Syring

def Decode_String(s):
    
    final = s
    count_bracket = 12345678
    while count_bracket != 0 :
        
        Array = []
        power = 0 
        for loop in range(len(final)):
            
            head = loop
            
            if final[head:head+1] == "[" :
                
                power = power + 1
                if power == 1:
                   tail =  head 
                   flag = True
                  
                   while flag == True :
                      tail = tail-1
                      if final[tail:tail+1].isdigit() == False:
                          flag = False
                   tail = tail + 1
            if final[head:head + 1] == "]" :
                
                power = power - 1
                
                if power == 0 :
                    
                    extract = final[tail: head + 1]
                    Array.append(extract)
                    
            if power == 0 and final[head:head+1].isdigit() == False and final[head:head+1] != "[" and final[head:head+1] != "]":
                
                extract = final[head : head + 1 ]
                Array.append(extract)
                    
       # print("array",Array)
        
        for index in range(len(Array)):
            a = 1
            
            mystery = Array[index]
            
            for storm in range(len(mystery)):
                if mystery[storm] == "[" :
                    a = storm
                    break
                
            number = mystery[0:a]
            
            if number.isdigit() == True :
                
                repeats = mystery[a+1:len(mystery)-1]
                concat = ""
                
                for fulfill in range(int(number)):
                    concat = concat + repeats
                    
               # print("concat",concat)
                Array[index] = concat
                
        final = ""
        for ocean in range(len(Array)):
            
            final = final +  Array[ocean]       
            #print("final ",final)       
        
        count_bracket = 0
        for lastcheck in range(len(final))  :
            
            if final[lastcheck : lastcheck + 1]  == "[" :
                
             count_bracket = count_bracket + 1
       # print(count_bracket)
    
    print(final)            
           
                     
Decode_String("3[a]2[bc]")    
Decode_String("3[a2[c]]")    
Decode_String("2[abc]3[cd]ef")    
Decode_String("100[eet]")
            
        
            
    
    