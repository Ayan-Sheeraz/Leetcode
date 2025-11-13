def SpiralOrder(matrix):  #This code leaves the user spiral
    
    

     TotalElements = len(matrix) * len(matrix[0])

     PlaceArray = [0] * TotalElements

     if len(matrix) == 1:

          for index in range(len(matrix[0])):

               PlaceArray[index] = matrix[0][index]

               #Next index

     else:

          Count = -1

          StartCol = 0
          EndCol = len(matrix[0]) - 1     # Max Col element
          StartRow = 0
          EndRow = len(matrix) - 1

          while (Count + 1) < TotalElements:

               if Count != (TotalElements-1):

                    for loop in range(StartCol, EndCol + 1):
                       if Count<TotalElements:
                         Count = Count + 1
                         PlaceArray[Count] = matrix[StartRow][loop]

               StartRow = StartRow + 1


               if Count!= (TotalElements-1):

                    for loop in range(StartRow, EndRow + 1):
                      if Count<TotalElements:
                         Count = Count + 1
                         PlaceArray[Count] = matrix[loop][EndCol]

               EndCol = EndCol - 1


               if Count!= (TotalElements-1):

                    for loop in range(EndCol, StartCol - 1, -1):
                       if Count<TotalElements:
                         Count = Count + 1
                         PlaceArray[Count] = matrix[EndRow][loop]

               EndRow = EndRow - 1


               if  Count!= (TotalElements-1):
                    for loop in range(EndRow, StartRow - 1, -1):
                      if Count<TotalElements:
                         Count = Count + 1
                         
                             
                         PlaceArray[Count] = matrix[loop][StartCol]

               StartCol = StartCol + 1
 

     print (PlaceArray)
     
     
    
#SpiralOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
#SpiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
SpiralOrder([[1,2,3],[4,5,6],[7,8,9]])
#SpiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
