Height=float(input("Enter your Height (cm): "))
Weight=float(input("Enter your Weight (kg): "))

Height = Height/100
BMI=Weight/(Height*Height)

print("Your Body Mass Index (BMI) value : ", BMI)

if (BMI>0):
    if (BMI<=16):
        print("Category - Severe Underweight")
    elif (BMI<=18.5):
        print("Category - Underweight")
    elif (BMI<=25):
        print("Category - Healthy")
    elif (BMI<=30):
        print("Category - Overweight")
    else: 
        print("Severe Overweight")
else:
    ("enter valid details")
