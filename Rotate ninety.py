def RotateMatrix(Matrix):
    
    GroupLen = len(Matrix)     # Number of steps as matrix is n x n, it will work
    Concatenate = ""           # Empty String

    for row in range(GroupLen): 
        for Col in range(GroupLen):
            Concatenate = Concatenate + str(Matrix[row][Col])+" " # str: integer to String

            # NextCol
        # Next row

    StartPos = 0     # Index of string starts from 0
    count2=0
    for Col in range(GroupLen-1,-1,-1):
        for Row in range(GroupLen):
            while   Concatenate[StartPos:StartPos+1]!=" " :
                count2=count2+1
                StartPos=StartPos+1
                
            Place = Concatenate[StartPos-count2:StartPos] 
            Matrix[Row][Col] = int(Place)
            StartPos=StartPos+1
            count2=0
            # Next Row
        # NEXT Col

    for Present in range(len(Matrix)):

        print(Matrix[Present])
        
           