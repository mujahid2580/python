Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(6):
    for j in range(6):
        if (j==0 or j ==5 ) and (i>0 and i<5) or (i==0 or i==5) and (j>1 and j<4):
            print("*",end="")
        else:
            print(end=" ") 
    print()

    
  **  
*    *
*    *
*    *
*    *
  **  
>>> 
