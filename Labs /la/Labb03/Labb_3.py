import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')


x = []
y = []

# opening and reading the file
with open('/home/emicr/-python-programming-Altobelli-Matteo/-python-programming-Altobelli-Matteo/Labs /la/Labb03/unlabelled_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        x.append(float(row[0]))
        y.append(float(row[1]))

# calculating if a point is above or below the y_line
def classify_point(x, y, k, m):
    line_y = k * x + m
    if y < line_y:
        return 0
    else:
        return 1

# classifying the points
k = -0.75
m = -0.25
for i in range(len(x)):
    result = classify_point(x[i], y[i], k, m)

# creating a new csv file

with open('labelled_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y', 'class'])  
    for i in range(len(x)):
        class_label = classify_point(x[i], y[i], k, m)
        writer.writerow([x[i], y[i], class_label])


# creating a scatter plot with the new sorted points
class0_x = []; class0_y = []
class1_x = []; class1_y = []

for i in range(len(x)):
    class_label = classify_point(x[i], y[i], k, m)
    if class_label == 0:
        class0_x.append(x[i])
        class0_y.append(y[i])
    else:
        class1_x.append(x[i]) 
        class1_y.append(y[i])

plt.scatter(class0_x, class0_y, c ='g', label='Class 0')
plt.scatter(class1_x, class1_y, c ='r', label='Class 1')

# plotting the line
x_line = np.linspace(min(x), max(x), 100)
y_line = k * x_line + m
plt.plot(x_line, y_line, c='y', label='Decision boundary')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data Plot', fontsize=20)
plt.legend()
plt.savefig('classification_plot.png')