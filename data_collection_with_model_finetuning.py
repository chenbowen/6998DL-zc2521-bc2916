import numpy as np
import serial
import csv
import random
import time
import math
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from xgboost.sklearn import XGBRegressor


fieldnames = ["x_val", "y1"]

data = {}
data["x_val"] = [i for i in range(100)]
data["y1"] = [0 for i in range(100)]


port = input("[INPUT] Enter port num:(1440,etc) :")
port = "/dev/cu.usbserial-" + port 
baud = 115200

ser = serial.Serial(port, baud)

# 6 label
MINI_BATCH_2_TIMES = 6
MAIN_REPO = "data/data_repo_zj.csv"
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


for i in range(0,MINI_BATCH_2_TIMES * 4):
    posRand = random.random() * 7
    if posRand < 2: posLabel = 0
    else: posLabel = int(posRand)
    print("collecting", posLabel,posLabel,posLabel,posLabel)
    # if i < MINI_BATCH_2_TIMES: posLabel = 0
    # else: posLabel = int((i - MINI_BATCH_2_TIMES) / (MINI_BATCH_2_TIMES/2)) + 1
    prompt = "press enter to start collect label: " + str(posLabel) + ": "
    start = input(prompt)
    if start == "STOP": break
    get_batch_data(posLabel)


if start != "STOP":
    now = datetime.now()
    current_time = now.strftime("%H_%M_%S")
    now = datetime.today()
    current_date = now.strftime("%m_%d_%y")

    # 存档
    fileName = "data/DATA_REPO__" +  current_date + "__" + current_time + ".csv"

    repo = open(fileName, "w")
    writer = csv.writer(repo)

    file = open(MAIN_REPO, "r")
    reader = csv.reader(file)

    for row in reader: writer.writerow(row)

    file.close()
    repo.close()
        
    # 更新main_repo
    new_repo = open(MAIN_REPO, "a")
    writer = csv.writer(new_repo)

    for row in collected_data:
        if len(row) == 0: continue
        if row[0] == "label": continue
        row = row[0:258]
        writer.writerow(row)
    new_repo.close()


# TRAIN NEW MODEL






train_data = pd.read_csv(MAIN_REPO)
train_data = train_data.iloc[:,0:258]
train_data.dropna(inplace=True)
train_data.drop_duplicates(inplace=True)
train_data.reset_index(drop=True,inplace=True)
print("TRAINING ON...\n", train_data.label.value_counts())

final_classfiers = []

for i in range(1,7):

  now_data = train_data[(train_data["label"] == 0) | (train_data["label"] == i)]
  data = now_data.values
  X = data[:,1:258]
  y = data[:,:1]
  xgb=XGBRegressor()
  print("TRAINING", i)
  xgb.fit(X, y)
  final_classfiers.append(xgb)

label = []
start = False
sequence = 0 

while True:
    line=str(ser.readline().decode('latin-1'))
    if line[0] != "-" and not start:  continue
    elif line[0] == "-" and len(label) == 0 and not start: 
        print("[INIT]")
        start = True
    elif line[0] == "-" and len(label) == 256: 
        sum_points =  sum(label)
        if sum_points > THRES:

            sequence = sequence + 1
            label.append(int(sequence))
            print(sum(label))

            all_score = []
            for i in range(0,6):
                all_score.append(final_classfiers[i].predict([label])/(i+1))
            
            print(sum(all_score))

            # update 图标
            # data['y1'].append(sum(all_score))
            # data['y1'] = data['y1'][1: 101]

            # with open('data.csv', 'w') as csv_file:
            #     csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            #     csv_writer.writeheader()
            #     for i in range(0,100):
            #         info = {
            #             "x_val": data['x_val'][i],
            #             "y1": data['y1'][i]
            #         }
            #         csv_writer.writerow(info)

            label = []

        elif sum_points < THRES: 
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
