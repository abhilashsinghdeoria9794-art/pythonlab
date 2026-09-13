import numpy as np 
#Student  names
students=np.array(["S1","S2","S3","S4","S5"])
# Mid-Semester marks
mid_marks=np.array(
[
    [65,70,68,72],
    [78,75,80,77],
    [55,60,58,62],
    [82,85,80,88],
    [70,68,72,74]
])
end_marks =np.array([
    [72,78,75,80],
    [84,82,83,86],
    [65,68,66,70],
    [88,90,85,92],
    [78,75,80,82]
])

mid_total =np.sum(mid_marks,axis=1)
end_total = np.sum(end_marks,axis=1)

mid_average = mid_total/4
end_average = end_total/4
improvement= ((end_total-mid_total)/mid_total)*100

for i in range(5):
    print(students[i],mid_total[i],mid_average[i],end_average[i], round(improvement[i],2))