#Exercise 1
t1 = ("om",18,"B+","Bhopal")
print(t1[0],t1[-1])
print (len(t1))
for i in t1:
    print(i)
#Exercise 2
medicine = ("dolo","montec-lc","azio")
medicine[0] = ("crosine")
print(medicine)
medicine_1 = list(medicine)
medicine_1[0]=("crosine")
medicine = tuple(medicine_1)
#Exercise 3
patients = [101, 102, 101, 103,
            102, 104, 103, 105]
patients = set(patients)
print(patients)
print (len(patients))
#Exercise 4
hospital_a = {'Om', 'Yash',
              'Deepak', 'Taruni'}
hospital_b = {'Deepak', 'Taruni',
              'Mayank', 'Priya'}
print (hospital_a | hospital_b)
print (hospital_a & hospital_b)
print(hospital_a - hospital_b)
print(hospital_a ^ hospital_b)
#Exercise 5
patient = {"name":"om","age":18,"blood_type":"B+","bp":120,"is_diabetic":True}
print (patient.keys())
print (patient.values())
patient["city"]= ("Bhopal")
patient["bp"]= 130
del patient["blood_type"]
print (patient)
#Exercise 6
dataset = [
    {'name': 'Om',    'age': 18, 'bp': 120},
    {'name': 'Yash',  'age': 45, 'bp': 155},
    {'name': 'Priya', 'age': 62, 'bp': 170},
    {'name': 'Deepak','age': 30, 'bp': 118},
]
for x in dataset:
    print(x)
    print(x["name"])
    print(x["bp"])

