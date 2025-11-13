#Leetcode 2125 - no. of laser beams in a bank -- medium


def numberofbeams(bank):
    
    if len(bank) == 1 :
        print(0)
       # print("first stage no row")
    else:
        Array = []
        
        for loop in range(len(bank)):
            
            flag = True
            Count = 0
            for index in range(len(bank[loop])):
                
                if (bank[loop])[index:index+1] == "1":
                    flag = False
                    Count = Count + 1
                    
            if flag == False :
                Array.append(Count)
                
        if len(Array) == 1:
            print(0)
            #print("printing next stage no rows")
        else:
            sum = 0
            #print(Array)
            for x in range(1,len(Array)):
                
                val = Array[x] * Array[x-1]
                sum = sum + val 
            #print("printing sum")
                      
                      
            print(sum)
            
            
            
    
#numberofbeams(["011001","000000","010100","001000"])
numberofbeams(["000","111","000"])