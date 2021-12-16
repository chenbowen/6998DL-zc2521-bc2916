from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from random import random
import time
import numpy as np
import serial
import cv2
# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# train_csv = pd.read_csv("pink.csv")
# scaler = StandardScaler()
# data = train_csv.iloc[:,1:257]
# scaler = scaler.fit(data)

# VMAX = int(input("vmax:"))
# VMAX = 2000
# THRES = 30
port = input("PORT:")
# port = "0001"
arduino_port = "/dev/cu.usbserial-" + port
baud = 115200

ser = serial.Serial(arduino_port, baud)
label = [0]*256
    
window = Tk()
window.title('Plotting in Tkinter')
window.geometry("1000x1000")

# lb = []
fig = Figure(figsize = (50, 50), dpi = 100)
plot1 = fig.add_subplot(111)    
canvas = FigureCanvasTkAgg(fig, master = window)

def plot():
    global label
    start = False

    while True:
        line=str(ser.readline().decode('latin-1'))
        if line[0] != "-" and not start:  continue
        elif line[0] == "-" and len(label) == 0 and not start:  start = True
        elif line[0] == "-" and len(label) == 256: 
            # point_s = len([i for i in label if i > 107])
            # print("Active Points", point_s)
            # if point_s < THRES: label = [107] * 256
            break
        else:
            thearr = line.split(",")
            if len(thearr) == 17:
                for i in thearr:
                    try: label.append(int(i))
                    except: pass
            # 如果没有 清空
            else: 
                # print("[DETECT BUG, RE-STARTING]")
                label = []
                start = False
    # label = scaler.transform([label]) * 1000
    a = np.asarray([label])
    a = a.reshape(16,16)
    # a = np.flip(a)
    # resize_a = cv2.resize(a.astype('float'), (256,256), interpolation=cv2.INTER_LANCZOS4)


    # mx = []
    # ma = -99909999099990999909
    print(a)
    # sum = []
    # for i in range(0,14,3):
    #     for j in range(0,14,3):
    #         s_2 = []
    #         for k in range(0,3):
    #             for f in range(0,3):
    #                 s_1 = a[i+k,j+f]
    #                 s_2.append(s_1)
    #         sm = sum(s_2)
    #         print(sm)
    #         if sm > ma: 
    #             ma = sm
    #             mx = [i,j]
    # print(mx)
    # b = np.zeros(256).reshape(16,16)
    # b[mx[0],mx[1]] = 1000 
    # for k in range(0,3):
    #     for f in range(0,3):
    #         b[mx[0]+k,mx[1]+f] = 800
    # print(mx)
    # print(b)

    plot1.clear()
    plot1.imshow(a, cmap='RdPu', vmin=1500, vmax=3100, interpolation='none')
   
    # canvas.get_tk_widget().delete("all")
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
  
    canvas.get_tk_widget().pack()
    label = []
    window.after(10, plot)
        
plot()
# run the gui
window.mainloop()