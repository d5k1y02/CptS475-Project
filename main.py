
from skmultiflow.data.data_stream import DataStream
from datetime import datetime
from numpy import loadtxt
import random
import math
import csv
# 1. read and load the dataset into memory
stream = FileStream("bodmas.csv")
print(stream.next_sample())
print(type(stream))

month_counts = {}
month_count = 0 
with open('bodmas_metadata.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    current_month = ''
    month_count = 0
    for row in reader:
        datetime_str = row['timestamp'].split()[0]
        try:
            datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d')
        except:
            datetime_object = datetime.strptime(datetime_str, '%m/%d/%Y')
        if str(datetime_object.year) + ' ' + str(datetime_object.month) == current_month:
            month_count += 1
        else:
            if(current_month != ''):
                month_counts[current_month] = month_count
            current_month = str(datetime_object.year) + ' ' + str(datetime_object.month)
            month_count = 1

print(month_counts)


