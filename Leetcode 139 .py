# LEETCODE  question 139.Word Break --Medium
def WordBreak(s,wordDict):
    
    Array = [""]* len(wordDict)
    
    for loop in range(len(wordDict)):
        a = 0
        while (a+len(wordDict[loop])) != (len(s)+1):
            if s[a:a+len(wordDict[loop])] == wordDict[loop] :
                Array[loop] = Array[loop] + s[a:a+len(wordDict[loop])]
                    
            a = a + 1
        
    count = 0
    length = 0
    
    for loop in range(len(Array)):
        length = length + len(Array[loop])
        
        if Array[loop] != "" :
            count = count + 1
            
    if count == len(wordDict) and length == len(s):
        print("true")
    else:
        print("false")
     
        
#WordBreak("leetcode",["leet","code"])
#WordBreak("applepenapple",["apple","pen"])
#WordBreak("catsandog",["cats","dog","sand","and","cat"])
WordBreak("applepenapplerows",["apple","pen"])
