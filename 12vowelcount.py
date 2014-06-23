def VowelCount(str): 
  vowels = 0
  for x in str:
    if x in "aeiouAEIOU":
      vowels += 1
  return vowels

    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print VowelCount(raw_input())  
