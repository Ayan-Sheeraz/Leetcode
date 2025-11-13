## leetcode 59 - Spiral Matrix 2

def Spiralcreate(n):
    
    if n == 1 :
        matrix = [[1]]
        
    else:
    
        matrix = [ [0]*n for i in range(n)]
        
        max = n * n
        incrementor = 1
        
        FirstRowRow = 0
        FirstRowCol = n-1
        
        LastColRow = 1
        LastColCol = n-1
        
        LastRowRow = n-1
        LastRowCol = 0
        
        FirstColRow = n-2
        FirstColCol = 0
        
        
        while incrementor <= max :
            
            if incrementor <= max :
                for loop in range(FirstRowRow,FirstRowCol+1):
                    
                    matrix[FirstRowRow][loop] = incrementor
                    incrementor = incrementor + 1
            
            # incrementir at the end incrementred fir next word not yet used 
            if incrementor <= max :
                for index in range(LastColRow,LastColCol+1):
                    
                    matrix[index][LastColCol] = incrementor
                    incrementor = incrementor + 1
                    
            if incrementor <= max :
                for storm in range(LastRowRow-1,LastRowCol-1,-1):
                    
                    matrix[LastRowRow][storm] = incrementor
                    incrementor = incrementor + 1
                    
            if incrementor <= max :        
                for runner in range(FirstColRow,FirstColCol,-1):
                    
                    matrix[runner][FirstColCol] = incrementor
                    incrementor = incrementor + 1
                
            
            FirstRowRow = FirstRowRow + 1
            FirstRowCol = FirstRowCol - 1
            LastColRow = LastColRow + 1
            LastColCol = LastColCol - 1
            LastRowRow = LastRowRow - 1
            LastRowCol = LastRowCol + 1
            FirstColRow = FirstColRow - 1
            FirstColCol = FirstColCol + 1
            
                
        
        
    print(matrix)    
        
        
Spiralcreate(5)