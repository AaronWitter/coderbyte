def LetterChanges(str): 
  a = "abcdefghijklmnopqrstuvwxyz"
  b = []
  c = []
  for x in str:
    if x in a:
      b.append(a[a.index(x)+1])
    elif x not in a:
      b.append(x)
  for y in b:
    if y in "aeiou":
      c.append(y.upper())
    else:
      c.append(y)
      
  return "".join(c)
     
      
          

      
      
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterChanges(raw_input())   
