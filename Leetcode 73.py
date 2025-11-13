# Leetcode question 73.Set Matrx Zeroes

def setZeroes(matrix):
    
    count = 0
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            
            if matrix[row][col] == 0 :
                count = count + 1

    Array = [[0]*2 for i in range(count)]
    Pos=0 
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            
            if matrix[row][col] == 0 :
                Array[Pos][0] = row 
                Array[Pos][1] = col 
                Pos = Pos + 1
    
    # last stage : Time for Zeroes
        
    for i in range(count): # there are more then one zeroes therefore more then one loop
        
        Refcol = Array[i][1] # i will auto increment so idonot need to do it manually
        Refrow = Array[i][0]
        
        for setR in range(len(matrix)):
            
            matrix[setR][Refcol] = 0
        
        for setC in range(len(matrix[0])):
            
            matrix[Refrow][setC] = 0
            
    print(matrix)
# BISMILLAH HIRAMA NIRAHEEM  
#setZeroes([[1,1,1],[1,0,1],[1,1,1]])
#setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
#setZeroes([[1,2]])
setZeroes([[1,2,3,0,4],[5,6,9,8,9],[0,11,12,13,14]])