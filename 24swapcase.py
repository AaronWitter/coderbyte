def SwapCase(str): 
  a = []
  for x in str:
    if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
      y = x.lower()
      a.append(y)
    elif x in "abcdefghijklmnopqrstuvwxyz":
      z= x.upper()
      a.append(z)
    else:
      a.append(x)
 
  return ''.join(a)

    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print SwapCase(raw_input())           
