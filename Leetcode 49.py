# leetcode 49. GROUP ANAGROMS difficult one
# ron araha hai: my program is correct!!!!!!!!!!!!!!!!!!!!!!!
def groupAnagrams(strs):
    
    empty = 0
    for finding in range (len(strs)):
        if strs[finding]=="":
            empty = empty + 1
            
    concat = ""     
    if len(strs) == 0 or len(strs)== 1 :
        print( [strs])
    else:
        o = -1
        i = -1
        Arr = [""] * len(strs)
        tell = ""
        for loop in range(len(strs)):
            
           
            ext = strs[loop]
            
            if ext != "-1": 
                Arr[loop] = str(len(ext)) + ext
                lenex = len(ext)
                if loop != (len(strs)-1):
                
                    for index in range (loop+1,len(strs)):
                        
                        new = strs[index]
                        
                        if len(new) == lenex:
                            for outer in range (lenex):
                                o = o + 1
                                for inner in range (lenex):
                                    i = i + 1
                                    if ext[o:o+1] == new [i:i+1]:
                                        tell = tell + "A"
                                        concat = concat + new[i:i+1]
                                i = -1
                            o = -1
                            
                            if len(tell) == lenex and concat == ext:
                                Arr[loop] = Arr[loop] + new
                                strs[index] = "-1" #null value
                        tell = ""
       # print(Arr)# phase 1 is perfect
    # end all loops time for phase 2 : hehehe
       
        array2D = []
        for phaseloop in range (len(Arr)):
            if Arr[phaseloop] != "" and Arr[phaseloop] != "0":
              
                  
                    start = 1
                    differ = int((Arr[phaseloop])[0:1])
                    end = start + differ
                    runner =int((len(Arr[phaseloop]) - 1) / differ )
                    # print(differ)
                    # print(runner)
                    temparray = [""] * runner # rebirth
                    # print(temparray)
                    for phaseindex in range (runner):
                        taker = (Arr[phaseloop])[start:end]
                        temparray[phaseindex] = taker
                        
                        start = end
                        end = end + differ
                        
                    array2D.append(temparray)
                    # print(temparray)  
        if empty != 0 :
            cpr = [""]*empty
            array2D.append(cpr)
        print(array2D )             


# groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# groupAnagrams([])
# groupAnagrams(["bat"])
# groupAnagrams(["aab","abb"])
# groupAnagrams(["abcd","bcda","cbda","ab"])
# only works correctlt if length of all element is strs is same
# groupAnagrams(["","",""])
# groupAnagrams(["b",""])
groupAnagrams(["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"])