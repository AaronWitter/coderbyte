def ExOh(str): 
  n = 0
  for x in str:
    if x == 'x':
      n +=1
    else:
      n -=1
  if n == 0:
    return 'true'
  else: 
    return 'false'
    
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ExOh(raw_input()) 
