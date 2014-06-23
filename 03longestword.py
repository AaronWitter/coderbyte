def LongestWord(sen): 
  a = sen.split()
  return max(a, key = len)
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LongestWord(raw_input())  
