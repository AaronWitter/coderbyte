def LetterCapitalize(str): 
  good = []
  a = str.lower()
  for x in a:
    good.append(x)
    b = ''.join(good)
  return b.title()
    

      
      

    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterCapitalize(raw_input()) 
