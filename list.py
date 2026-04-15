"""
l1 = [3,8,2,3,6,7,3,7,5]
#print(l1[1:6:1])
#print(l1[2:8:3])
l2 =[3,5,6]
#print (l1+l2)
#print (l2*3)
fruits = ["apple", "banana", "cherry"]
#print (fruits)
(fruits.append("mango"))
#print (fruits)
fruits.insert(2 , "watermelon")
fruits.extend(["yoyo","brobro"])
fruits.remove("watermelon")
fruits.pop(3)
fruits.reverse()
nums = [4,5,7,8,2,4,6,2,7,3545,35346,6344,]
#print (nums)
nums.sort(reverse=True)
#print (nums.count(4))
print (min(nums))
"""
#Exercise 1
Patients = ["yash","om","deepak","taruni","mayank"]
print (len(Patients))
#Exercise 2
Medicines = ["paracetamol" , "ibuprofen","asprin"]
Medicines.append("amoxicillin")
Medicines.remove("asprin")
print (Medicines)
#Exercise 3
scores = [72, 85, 91, 60, 78, 95, 55, 88]
print (max (scores))
print (min (scores))
print (sum (scores)/len(scores))
print (sorted(scores))
#Exercise 4
vitals = [120, 80, 98.6, 72, 95, 110, 75]
print (vitals[0:3:1])
print (vitals[-2:])
print (vitals[0:8:2])
#Exercise 5
ages = [25, 65, 12, 70, 35, 8, 55, 67]
above_60 = 0
below_18 = 0

for age in ages:
    if age > 60:
        above_60 = above_60 + 1
    if age < 18:
        below_18 = below_18 + 1

print(f"Patients above 60: {above_60}")
print(f"Patients below 18: {below_18}")