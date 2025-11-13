# leetcode 49. GROUP ANAGROMS difficult one

def groupAnagrams(strs):
    
 if len(strs) == 0 or len(strs)== 1 :
     return [[strs]]
 else:
  o = -1
  i = -1
  Arr = [""] * len(strs)
  
  for loop in range(len(strs)):
      
    tell = ""
    ext = strs[loop]
    if ext is None : 
      Arr[loop] = str(len(ext)) + ext
      lenex = len(ext)
      if loop != (len(strs)-1):
    
       for index in range (loop+1,len(strs)):
           
           new = strs[index]
           
           if len(new) == lenex:
               for outer in range (lenex):
                   o = o + 1
                   for inner in range (lenex):
                       i = i + 1
                       if ext[o:o+1] == new [i:i+1]:
                           tell = tell + "A"
                   i = -1
               o = -1
               
           if len(tell) == lenex:
               Arr[loop] = Arr[loop] + new
               strs[index] = None
               
 
 # end all loops time for phase 2 : hehehe
 
  array2D = []
  for loop in range (len(Arr)):
      if Arr[loop] != "":
      
         start = 1
         differ = int((Arr[loop])[0:1])
         end = start + differ
         runner = int((len(Arr[loop])-1) / differ)
         temparray = [""] * runner
         
         for index in range (runner):
             taker = (Arr[loop])[start:end]
             temparray[index] = taker
             start = end
             end = end + differ
             
         array2D.append(temparray)
               
  print(array2D )             


groupAnagrams(["eat", "tea", "tan","nat","bat"])