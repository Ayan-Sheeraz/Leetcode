#LEETCODE 3 :  Longest substring without repeating characters , medium

def lengthoflongestsubstring(s):
    
    Array = [""]*len(s)
    Starter  = 0
    Runner = Starter
    flag = True
    
    while Starter != len(s) :
        while flag != False :
            
            Runner = Runner + 1
            for loop in range((Runner-1),Starter-1,-1):
                
                if s[Runner:Runner+1] == s[loop:loop+1] :
                    flag = False
                    
            if Runner == len(s):
                flag =- False
                
        concat = s[Starter:Runner]
        Runner = Starter
        flag = True
        # print(concat)
        # print(Starter)
        Array[Starter] = concat
        Starter = Starter + 1 
    print(Array)
    
    # phase 2 : MAX technique
    max = 0
    for index in range(len(Array)):
        if len(Array[index]) > max :
            max = len(Array[index])
    
    print(max)
    
# lengthoflongestsubstring("pwwkew")
# lengthoflongestsubstring("abcabcbb")
# lengthoflongestsubstring("bbbb")
lengthoflongestsubstring("ayansheeraz")
lengthoflongestsubstring("")