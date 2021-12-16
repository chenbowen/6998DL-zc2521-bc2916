import numpy as np
import serial
import csv
import random
import time
import math
from datetime import datetime


port = input("[INPUT] Enter port num:(1440,etc) :")
port = "/dev/cu.usbserial-" + port 
baud = 115200

ser = serial.Serial(port, baud)

# 6 label
MINI_BATCH_2_TIMES = 6
BATCH_ALL = 50
THRES = 350000
BATCH_SIZE = 30

collected_data = []

def get_batch_data(posLabel):

    label = []
    start = False
    sequence = 0 
    ct = 0
    
    while True:
        line=str(ser.readline().decode('latin-1'))
        if line[0] != "-" and not start:  continue
        elif line[0] == "-" and len(label) == 0 and not start: 
            print("[INIT]")
            start = True
        elif line[0] == "-" and len(label) == 256: 
            sum_points = sum(label)
            if sum_points > THRES:

                print(sum(label))
                sequence = sequence + 1
                label.append(int(sequence))
                label.insert(0, int(posLabel))

                print("[COLLECTED] ",label)
                collected_data.append(label)
                label = []

                ct +=1
                print(ct)
                if ct > BATCH_SIZE: break

            elif sum_points <= THRES: 
                print("[DETECT NO HUMAN]")
                sequence = 0
                label = []
                
        else:
            thearr = line.split(",")
            if len(thearr) == 17:
                for i in thearr:
                    try:  label.append(int(i))
                    except: pass
            else: 
                print("[RESET]")
                label = []
                start = False

for i in range(0,MINI_BATCH_2_TIMES*4):
    # posRand = random.random() * 8
    # if posRand < 2: posLabel = 0
    # else: posLabel = int(posRand) - 1
    if i < MINI_BATCH_2_TIMES: posLabel = 0
    else: posLabel = int((i - MINI_BATCH_2_TIMES) / (MINI_BATCH_2_TIMES/2)) + 1
    print("collecting", posLabel,posLabel,posLabel,posLabel)
    prompt = "press enter to start collect label: " + str(posLabel) + ": "
    start = input(prompt)
    if start == "STOP": break
    get_batch_data(posLabel)


now = datetime.now()
current_time = now.strftime("%H_%M_%S")
now = datetime.today()
current_date = now.strftime("%m_%d_%y")

fileName = "data/COLLECTED__" +  current_date + "__" + current_time + ".csv"

new_repo = open(fileName, "w")
writer = csv.writer(new_repo)

for row in collected_data:
    if len(row) == 0: continue
    if row[0] == "label": continue
    row = row[0:258]
    writer.writerow(row)
new_repo.close()