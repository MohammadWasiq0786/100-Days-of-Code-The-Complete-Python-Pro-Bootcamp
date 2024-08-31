""""
BMI Calculator with Interpretations
Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

If the bmi is under 18.5 (not including), print out "underweight"

If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

If the bmi is 25 (including) or over, print out "overweight"
"""

weight = 85
height = 1.85

bmi = weight / (height ** 2)

# print(bmi)

if bmi < 18.5:
    print("underweight")
    
elif 18.5 <= bmi < 25:
    print("normal weight")
    
else:
    print("overweight")


# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi > 18.5 and bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi > 25 and bmi < 30:
#     print(f"Your BMI is {bmi}, you are slighthly overweight.")
# elif bmi > 30 and bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")