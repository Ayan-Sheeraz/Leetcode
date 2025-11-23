# Leetcode 20.Valid Parantheses : level : easy 
""" I am gonna prove that raw problem solving beats all fancy techniques"""
def check(s):
    
    Power_One = 0
    Power_Two = 0
    Power_Three = 0
    
    for loop in range(len(s)):
        
        if s[loop] == "(" :
            Power_One = Power_One + 1
            
        if s[loop] == ")" :
            Power_One = Power_One - 1
            
        if s[loop] == "[" :
            Power_Two = Power_Two + 1
        
        if s[loop] == "]" :
            Power_Two = Power_Two - 1
            
        if s[loop] == "{" :
            Power_Three = Power_Three + 1
        
        if s[loop] == "}" :
            Power_Three = Power_Three - 1
            
    
    if Power_One == 0 and Power_Two == 0 and Power_Three == 0 :
        return True
    else:
        return False
            
            
    
def isValid(s):
    
    PowerOne = 0
    PowerTwo = 0
    PowerThree = 0
    
    newstring = s
    CountBracket = -1
    Array = []
    
    if check(newstring) == False :
        return False
        CountBracket = 0
    
    while CountBracket != 0 :
        
        for loop in range(len(newstring)) :
            
            if newstring[loop] == "(" :
                Head = loop
                PowerOne = PowerOne + 1
                for index in range(loop + 1,len(newstring)) :
                    
                    if newstring[index] == "(" :
                        PowerOne = PowerOne + 1
                        
                    if newstring[index] == ")" :
                        PowerOne = PowerOne - 1
                    
                    if PowerOne == 0 :
                        Tail = index
                        extract = newstring[Head + 1 : Tail]
                        Array.append(extract)
                        break
                    
            if newstring[loop] == "[" :
                Head = loop
                PowerTwo = PowerTwo + 1
                for index in range(loop + 1,len(newstring)) :
                    
                    if newstring[index] == "[" :
                        PowerTwo = PowerTwo + 1
                        
                    if newstring[index] == "]" :
                        PowerTwo = PowerTwo - 1
                    
                    if PowerTwo == 0 :
                        Tail = index
                        extract = newstring[Head + 1 : Tail]
                        Array.append(extract)
                        break
                    
            if newstring[loop] == "{" :
                Head = loop
                PowerThree = PowerThree + 1
                for index in range(loop + 1,len(newstring)) :
                    
                    if newstring[index] == "{" :
                        PowerThree = PowerThree + 1
                        
                    if newstring[index] == "}" :
                        PowerOne = PowerOne - 1
                    
                    if PowerThree == 0 :
                        Tail = index
                        extract = newstring[Head + 1 : Tail]
                        Array.append(extract)
                        break
                    
        CountBracket = 0
        Concatenate =  ""
        for runner in range(len(Array)):
            Concatenate = Concatenate + Array[runner]
            
            for seconder in range(len(Array[runner])):
                if (Array[runner])[seconder] == "(" or (Array[runner])[seconder] == ")" or (Array[runner])[seconder] == "[" or (Array[runner])[seconder] == "]" or (Array[runner])[seconder] == "{" or (Array[runner])[seconder] == "}" :
                    CountBracket = CountBracket + 1
                    
        newstring = Concatenate            
        if check(newstring) == False :
            return False
        
        
    return True
            
            
                        
                        
                        
# print(isValid("()"))
# print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
print(isValid("([)]"))

        
    
    
    
    
    
    
  
    
    
        