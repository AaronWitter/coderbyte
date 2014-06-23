def AlphabetSoup(str): 
  a = "abcdefghijklmnopqrstuvwxyz"
  b = []
  c = []
  for x in str: 
    if x in a:
      b.append(a.index(x))
      d = sorted(b)
  for x in d:
    c.append(a[x])
  return "".join(c)

    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print AlphabetSoup(raw_input())  
