"""
import os

path = '/Users/chaiwonpark/Desktop/excel/'
files = []
for _, _, files in os.walk(path):
    files.extend([f for f in files])

f = open(path + "fileNames.txt","a+")

for file in files:
    f.write(file + '\n')

f.close()
"""

import os

textFile = open("/Users/chaiwonpark/Desktop/excel/files.txt", "a+")
for root, dirs, files in os.walk("/Users/chaiwonpark/Desktop/excel"):
    for file in files:
        if file.endswith(".xlsx"):
             # print(os.path.join(root, file))
            print(file)
            textFile.write(file + '\n')
