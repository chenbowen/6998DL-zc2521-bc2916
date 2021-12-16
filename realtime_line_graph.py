
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.image as mpimg
from matplotlib.pyplot import figure

plt.style.use('fivethirtyeight')
figure(figsize=(18, 10), dpi=80)
plt.style.use('fivethirtyeight')


THRES = 500
MAX = 2000

data = {}
data["x_val"] = [i for i in range(100)]
data["thres"] = [THRES for i in range(100)]
# data["y1"] = [0 for i in range(100)]

img_0 = mpimg.imread('0.png')
img_1 = mpimg.imread('1.png')

# i = 0
def animate(i):
    print(i)
    plt.gcf().clear()
    
    plt.subplot(1,2,1)

    plt.ylim(ymax = MAX, ymin = 0)
    x = data['x_val']
    y0 = data["thres"]

    data_csv = pd.read_csv('data.csv')
    y1 = data_csv['y1']

    plt.plot(x, y0, "r-.")
    plt.plot(x, y1, label="Bad Posture",color = "lightblue")


    plt.subplot(1,2,2); 
    print(sum(data_csv["y1"][95:100]))
    if sum(data_csv["y1"][95:100]) > THRES*1.2*5:
        plt.imshow(img_1)
        plt.grid(None)
        plt.axis('off')
    else:
        plt.imshow(img_0)
        plt.grid(None)
        plt.axis('off')

    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.draw()



ani = FuncAnimation(plt.gcf(), animate, interval=20)

plt.tight_layout()
plt.show()