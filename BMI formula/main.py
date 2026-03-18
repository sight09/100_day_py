#BMI formula

h = input ("enter  ur hight in meter")
w = input("enter ur wight in kg")


bmi = int (w)/float(h)**2
bmis = int (bmi)
print (bmis)





#BMI with comment

  h = float(input("enter ur hight in meter "))
  w = float(input("enter ur wight in kg "))


  bmi = w / h**2

  if bmi < 18.5:
      print ("ur underweghit")

  elif bmi > 18.5 :
          print ("ur normal wight")
          
  elif bmi > 25 :
          print("ur over wight")
          
  elif bmi > 30:
    print("ur obese")
  # else:
    print("clinically obes")                


