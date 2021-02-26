import csv
import os

dirname = os.path.dirname(__file__)
input_file_name = os.path.join(dirname, '11.csv')

score = input('input score: ') 

answer = list()
with open(input_file_name, 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile.readlines()[1:-2], quotechar='"')
    for row in reader:
        if row[9].split(',')[0] == score:
            answer.append(row)
    
answer.sort(key=lambda row: row[0]+row[1])

for row in answer:
    print(', '.join(row[:10]))
