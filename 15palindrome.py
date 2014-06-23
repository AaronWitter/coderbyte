def Palindrome(str): 
   a = str.replace(" ","")
   
   if a == a[::-1]:
      return 'true'
   else:
      return 'false'
   
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print Palindrome(raw_input())  
