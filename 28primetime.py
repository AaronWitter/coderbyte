def PrimeTime(num): 
  if num <= 2:
    return 'true'
  if num == 3:
    return 'true'
  if num == 5:
    return 'true'
  if num == 7:
    return 'true'
  if num % 2 == 0:
    return 'false'
  if num % 3 == 0:
    return 'false'
  if num % 5 == 0:
    return 'false'
  if num % 7 == 0:
    return 'false'
  else:
    if num in range(8):
      return 'true'
    else:
      return 'true'
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print PrimeTime(raw_input())  
