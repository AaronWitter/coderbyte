def ABCheck(str): 
  
  for x in str:
    if x == 'b':
      y = str.index('b')
      if str[y-4] == 'a':
        return 'true'
      else:
        return 'false'
        
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ABCheck(raw_input())   
