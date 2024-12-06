Height = float(input("Enter Your Height in Centemiter: "))
Weight = float(input("Enter Your Weight in Kg: "))
Height = Height/100
BMI = Weight/(Height*Height)
 
print("Your Body Mass Index is: ", BMI)
if(BMI>0):
   if (BMI<=16):
     print('You Are Severly Underweighted')
   elif (BMI<=18.5):
     print('You Are Underweighted')
   elif (BMI<=25):
     print('You are healthy')
   elif (BMI<=30):
     print('You Are Overweighted')
   else:
     print('You Are Severly Overweighted')
else: ('Enter a valid details')
