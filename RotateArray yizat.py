
RotateArray=[0]*7
NormalArray=[0]*7
def Rotate():
    
 


 print("enter the array elements for end write -00")
 for loop in range(7):
   imp=input("element: ")
  
    
   RotateArray[loop]=int(imp)
   
 
 k=int(input("k:"))#3
 count2=-1
 for index in range(7-k,7):
  Place=RotateArray[index]
  count2=count2+1
  NormalArray[count2]=Place
 
 for loop in range (0,7-k):
   count2=count2+1
   NormalArray[count2]=RotateArray[loop]
 print(NormalArray)
 
 
Rotate()

