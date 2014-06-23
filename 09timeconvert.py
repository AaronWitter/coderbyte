def TimeConvert(num): 
  a = num / 60
  b = num % 60
  return str(a) + ":" + str(b)
  
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print TimeConvert(raw_input())   
