from turtle import color, fillcolor
import numpy as np
import matplotlib.pyplot as plt
import os

def DOS1(filen, vacc, color, label) :
    x1, y1 = [], []
    x2, y2 = [], []
    count = 0
    with open(filen,"rt") as file:
        for t in file:
            if t[0] == '#':
                count +=1
            if count == 4 and t[0] == ' ' or count == 8 and t[0] == ' ':
                k = t.split()
                x1.append(float(k[0]))
                y1.append(float(k[1]))
            # if count == 8 and t[0] == ' ':
            #     k = t.split()
            #     x1.append(float(k[0]))
            #     y1.append(float(k[1]))
    file.close()
    X1 = np.array(x1)
    X1 = X1 - vacc

    # plt.plot(X1, y1, color = 'none', label = label)


    # plt.fill_between(X2, y2, color = 'teal')
    plt.fill_between(X1, y1, color = color, alpha = 0.5, label = label)
    plt.xlabel('E (eV)')
    plt.ylabel('DOS (eV^-1)' )
    plt.legend()
# filen = os.path.basename('/Pr-Ru-O-p')
DOS1('Pr-Ru-Pr-f', 3.294, 'olivedrab', 'Pr-Ru: Pr-f')
DOS1('Yb-Ru-Yb-f', 2.374, 'peru', "Yb-Ru: Yb-f")
plt.show()










# x3, y3 = [], []
# x4, y4 = [], []
# count = 0
# with open("Pr-f-dos-data","rt") as file:
#     for t in file:
#         if t[0] == '#':
#             count +=1
#         if count == 4 and t[0] == ' ':
#             k = t.split()
#             x3.append(float(k[0]))
#             y3.append(float(k[1]))
#         if count == 8 and t[0] == ' ':
#             k = t.split()
#             x4.append(float(k[0]))
#             y4.append(float(k[1]))
# file.close()
# X3 = np.array(x3)
# X3 = x3 +
# X4 = np.array(x4)
# #plt.plot(x1,y1, color = "green")
# plt.plot(X,y1, color = "blue")
# # plt.fill_between(x1,y1, color = "green")
# # plt.plot(x2,y2, color = "green")
# # plt.fill_between(x2,y2, color = "green")
# # plt.xlim(-15,5)

# # plt.plot(x3,y3, color = "blue")
# # plt.fill_between(x3,y3, color = "blue")
# # plt.plot(x4,y4, color = "blue")
# # plt.fill_between(x4,y4, color = "blue")

# plt.show()
