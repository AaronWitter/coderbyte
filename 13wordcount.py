def WordCount(str): 
  spaces = 0
  for x in str:
    if x == ' ':
      spaces +=1
  return spaces+1
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print WordCount(raw_input()) 
