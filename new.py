# text = ("Today is my bday the cake was awesome")
    
# # text : today is my bday the cake was awesome
# #        0    5                               
# text = text + " " # for last words to be included
# c = 0
# HP = 0
# TP = -1
# ArrayExt = []
# ArrayLen = []
# while HP != len(text) :
    
#     TP = TP + 1
    
#     if text[TP:TP+1] == " " :
#         print("true")
        
#         extract = text[HP:TP] # extraction without spacee
#         HP = TP +1
#         ArrayExt.append(extract.lower())
        
#         nums = int(  str(len(extract)) + str(c)  )
#         print(" extract : ", len(extract), " c : ", c , "  = nums : ", str(nums))
#         ArrayLen.append(nums)
#         c = c+1
    
# print(ArrayExt)
# print(ArrayLen)

# Noswaps = False
# Boundary = len(ArrayLen) - 1
# while Noswaps == False :
    
#     Noswaps = True
#     for loop in range(Boundary):
        
#         if ArrayLen[loop] > ArrayLen[loop+1] :
            
#             temp = ArrayLen[loop]
#             ArrayLen[loop] = ArrayLen[loop + 1]      
#             ArrayLen[loop + 1] = temp
#             Noswaps = False
            
#     Boundary = Boundary - 1
    
# print(ArrayLen)

    
# EndArray = []

# for index in range(len(ArrayLen)):
    
#     start = str(ArrayLen[index])
#     pos = int( start[len(start)-1 : len(start)] )
#     # print(pos)
#     sorted = ArrayExt[pos]
#     # print("sorted ", sorted)
#     EndArray.append(sorted)
    
# print(EndArray)


# print("before ", EndArray[0])
# EndArray[0] =(( EndArray[0] )[0]).upper()  +   ( EndArray[0] )[1:len(EndArray)]
# print("after ", EndArray[0])

# concat = ""
# for runner in range(len(EndArray)) :
#     concat = concat + EndArray[runner] + " "
    
# concat = concat[0:len(concat)-1]
# print(concat)
ArrayLen = [4,4,3,4,2]
AllOut = []       
        
for one in range(len(ArrayLen)):
    
    first = ArrayLen[one]
    singleloop = [first]
    
    for two in range(one,len(ArrayLen)):
        
        second = ArrayLen[two]
        
        if first == second :
            
            singleloop.append(two)
            ArrayLen[two] = ""
    
    AllOut.append(singleloop)

    for corect in range(len(AllOut)):
        if AllOut[corect][0] == "" :
            AllOut.remove(AllOut[corect])        
    
    
    
        


    
""" TIME FOR EFFICIENT BUBBLE SORT """

Noswaps = False
Boundary = len(AllOut) - 1
while Noswaps == False :
    
    Noswaps = True
    for loop in range(Boundary):
        
        if AllOut[loop][0] > AllOut[loop+1][0] :
            
            temp = AllOut[loop]
            AllOut[loop] = AllOut[loop + 1]      
            AllOut[loop + 1] = temp
            Noswaps = False
            
    Boundary = Boundary - 1
        
print(AllOut)