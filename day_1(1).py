with open('day_1.txt') as file :
    data = file.readlines()

max = 0
max1=0
max2=0
score = 0
for i in data:
    if  (i=="\n"):
        score = 0
        continue
    score += int(i)
    if score > max :
        max= score
    elif score > max1 :
        max1= score
    elif score > max2:
        max2= score
    
print(max) 
print(max + max1+ max2)


