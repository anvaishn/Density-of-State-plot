from turtle import color, fillcolor
import numpy as np
import matplotlib.pyplot as plt
x1, y1 = [], []
x2, y2 = [], []
count = 0
with open("Yb-f-dos-data","rt") as file:
    for t in file:
        if t[0] == '#':
            count +=1
        if count == 4 and t[0] == ' ':
            k = t.split()
            x1.append(float(k[0]))
            y1.append(float(k[1]))
        if count == 8 and t[0] == ' ':
            k = t.split()
            x2.append(float(k[0]))
            y2.append(float(k[1]))
file.close()
X = np.array(x1)
X = X + 5
x3, y3 = [], []
x4, y4 = [], []
count = 0
with open("Ru-d-dos-data","rt") as file:
    for t in file:
        if t[0] == '#':
            count +=1
        if count == 4 and t[0] == ' ':
            k = t.split()
            x3.append(float(k[0]))
            y3.append(float(k[1]))
        if count == 8 and t[0] == ' ':
            k = t.split()
            x4.append(float(k[0]))
            y4.append(float(k[1]))
file.close()
plt.plot(x1,y1, color = "green")
plt.plot(X,y1, color = "blue")
# plt.fill_between(x1,y1, color = "green")
# plt.plot(x2,y2, color = "green")
# plt.fill_between(x2,y2, color = "green")
# plt.xlim(-15,5)

# plt.plot(x3,y3, color = "blue")
# plt.fill_between(x3,y3, color = "blue")
# plt.plot(x4,y4, color = "blue")
# plt.fill_between(x4,y4, color = "blue")

plt.show()