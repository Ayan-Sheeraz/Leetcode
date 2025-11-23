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
        print("check gives false")
        return False
        CountBracket = 0
    
    while CountBracket != 0 :
        
        for loop in range(len(newstring)) :
            
            if newstring[loop] == "(" :
                Head = loop
                print(" *(* detected and head set to ",Head)
                PowerOne = PowerOne + 1
                for index in range(loop + 1,len(newstring)) :
                    
                    if newstring[index] == "(" :
                        PowerOne = PowerOne + 1
                        
                    if newstring[index] == ")" :
                        PowerOne = PowerOne - 1
                    
                    if PowerOne == 0 :
                        
                        Tail = index
                        print(" for () power one = 0 and now tail = ", Tail)
                        extract = newstring[Head + 1 : Tail]
                        print("extract ", extract)
                        Array.append(extract)
                        break
                            
                    """ heading towards speacial casse"""
                    
                if PowerOne > 0 :
                    Array.append(newstring[index])
                        
            if newstring[loop] == "[" :
                Head = loop
                print(" *[* detected and head set to ",Head)
                PowerTwo = PowerTwo + 1
                for index in range(loop + 1,len(newstring)) :
                    
                    if newstring[index] == "[" :
                        PowerTwo = PowerTwo + 1
                        
                    if newstring[index] == "]" :
                        PowerTwo = PowerTwo - 1
                    
                    if PowerTwo == 0 :
                        Tail = index
                        print(" for [] power two = 0 and now tail = ", Tail)
                        extract = newstring[Head + 1 : Tail]
                        Array.append(extract)
                        break
                    
                if PowerTwo > 0 :
                    Array.append(newstring[index])
                    
            if newstring[loop] == "{" :
                Head = loop
                print(" *{* detected and head set to ",Head)
                PowerThree = PowerThree + 1
                for index in range(loop + 1,len(newstring)) :
                    
                    if newstring[index] == "{" :
                        print("{ indexes", index)
                        PowerThree = PowerThree + 1
                                                                                                                                                                                                                                                                                                            
                    if newstring[index] == "}" :
                        PowerThree = PowerThree - 1
                    
                    if PowerThree == 0 :
                        Tail = index
                        print(" for {} power three = 0 and now tail = ", Tail)
                        extract = newstring[Head + 1 : Tail]
                        Array.append(extract)
                        break
                    
                if PowerThree > 0 :
                    Array.append(newstring[loop])
        print(Array)            
        CountBracket = 0
        Concatenate =  ""
        for runner in range(len(Array)):
            Concatenate = Concatenate + Array[runner]
            
            for seconder in range(len(Array[runner])):
                if (Array[runner])[seconder] == "(" or (Array[runner])[seconder] == ")" or (Array[runner])[seconder] == "[" or (Array[runner])[seconder] == "]" or (Array[runner])[seconder] == "{" or (Array[runner])[seconder] == "}" :
                    CountBracket = CountBracket + 1
        print("countbracket = ", CountBracket)            
        newstring = Concatenate 
        print("newstring = ",newstring)
        Array = []           
        if check(newstring) == False :
            return False
        
        
    return True
            
            
                        
                        
                        
#print(isValid("()"))
#print(isValid("()[]{}"))
#print(isValid("(]"))
#print(isValid("([])"))
#print(isValid("([)]"))
print(isValid("(){}}{"))

        
    
    
    
    
    
    
  
    
    
        