low= int(input ("please,enter the lower range value: "))  
high = int(input ("please,enter the upper range Value: ")) 
for number in range (low,high):  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
          print (number)  
