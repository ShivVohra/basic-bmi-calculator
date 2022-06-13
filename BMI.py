#BMI_CALCULATOR
Weight = input("Enter Your Weight in Kg - ")
Height = input("Enter Your Height in M - ")
# newWeight = int(Weight)
# newHeight = int(Height)
BMI = round(int(Weight) / float(Height)**2, 2)

#Start of BMI 2.0 Calculator
new_BMI = str(BMI)

if BMI < 18.5:
    print("You are underweight , Your BMI is: " + new_BMI)
elif BMI < 25:
    print("You have a normal weight , Your BMI is: " + new_BMI)
elif BMI < 30:
    print("You are slightly overweight , Your BMI is: " + new_BMI)
elif BMI < 35:
    print("You are obese")
else:
    print("You are extreamly obese bitch! , Your BMI is: " + new_BMI)



