#allowing google colab to access drive 
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

MY_PATH = '/content/drive/MyDrive/datavis/'  

#imports
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm
import numpy as np
import csv

#finding the file
datafile = MY_PATH + 'StudentGrades.csv'
csv_file = open(datafile, 'r')
csv_file.readline()

#lists created
name = []
score = []

for a, b in csv.reader(csv_file, delimiter=','):
    name.append(a)
    score.append(b)

#convert to numpy arrays
scorenp = np.array(score, dtype=float)

#plotting
plt.figure(dpi=1200)
fig = plt.figure(figsize = [6,4])
ax = fig.add_axes([0,0,1,1])
ax.bar(range(len(scorenp)),scorenp, color = 'goldenrod', hatch ='/', label = 'Score')
ax.set_xticks(range(len(name)))
ax.set_xticklabels(name, rotation = 'vertical')
plt.axhline(np.mean(scorenp), linestyle='-.', label = 'Mean')
plt.axhline(y=75, color = 'green', label = 'Passing')

#legend
ax.legend(fontsize = 8, shadow = True)

#axis labels, title
ax.set_xlabel('Name')
ax.set_ylabel('Score Recieved(%)')
ax.set_title('Student Scores')

#saving graph in Google Drive
MY_PATH = '/content/drive/MyDrive/datavis/'
filename = MY_PATH + "studentGrade_test.png"
fig.savefig(filename, dpi=400, bbox_inches="tight")
