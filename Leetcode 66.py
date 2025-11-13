#Leetcode 66 Plus one, easy level

def Plus_one(digits):
    
    concat = ""
    
    for x in range(len(digits)):
        number = digits[x]
        number_str = str(number)
        
        concat = concat + number_str
    
    og = int(concat) + 1
    use = str(og)
    
    new = [0] * len(use)
    for i in range(len(use)):
        
        a = use[i:i+1]
        new[i] = int(a)        
    
    print(new)
    
    

m = [221]
Plus_one(m)