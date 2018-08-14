hcm =int(input("What is your height?" ))
w =int(input("What is your weight?"))
h = hcm / 100
BMI= w/ (h+h)
print("Your Body Mass Index:", BMI)
if BMI <16:
    print ("Severely underweight")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print(" Obese")
