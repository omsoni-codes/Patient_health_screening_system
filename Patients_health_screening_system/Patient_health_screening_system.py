# Patient health screening system
name = input("Enter patient's name: ")
age = int(input("Enter patient's age: "))
bp = int(input("Enter patient's BP: "))
sugar = int(input("Enter patient's sugar: "))
bmi = float(input("Enter patient's BMI: "))

print (f'--- Report for {name} ---')
# age group
age_group = 'Senior citizen ' if age >= 60 else ('Adult' if age >= 18 else 'Minor')
print (f'Age Group: {age_group},{age}')
# Bp status
if bp < 120:
    bp_status = 'Normal'
elif bp < 130:
    bp_status = 'Elevated'
elif bp < 160:
    bp_status = 'High Stage 1'
elif bp < 180:
    bp_status = 'High Stage 2'
elif bp > 110:
    bp_status = 'Slightly low'
elif bp < 110:
    bp_status = 'Low BP'
else :
    bp_status = 'HYPERTENSIVE CRISIS'
print (f'BP: {bp_status},{bp}')
#sugar classification
if sugar < 70: print('Sugar: Hypoglycemia - URGENT')
elif sugar < 100: print('Sugar: Normal')
elif sugar < 126: print('Sugar: Pre-diabetic')
else: print('Sugar: Diabetic')
#BMI classification
if bmi < 18.5: print('BMI: Underweight')
elif bmi < 25: print('BMI: Normal')
elif bmi < 30: print('BMI: Overweight')
else: print('BMI: Obese')
# Overall risk
if bp > 140 and sugar > 126:
    print('OVERALL: HIGH RISK - Immediate attention')
elif bp > 140 or sugar > 126:
    print('OVERALL: MEDIUM RISK - Immediate attention')
else :
    print('OVERALL: LOW RISK - Immediate attention')