from numpy import load
from skmultiflow.data.file_stream import FileStream
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

with open('bodmas_metadata.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    starting_index = 0
    for value in month_counts:
        print(type(month_counts[value]))
#        print(random.randint(value, size = math.ceil(month_counts[value] * 0.75)))
#        print(random.randint(month_counts[value], size = math.ceil(month_counts[value] * 0.75)))
        print(random.sample(range(0, month_counts[value]), math.ceil(month_counts[value] * 0.75)))

# 2. convert the dataset into a format suitable for learning


# 3. select month of data and split the data into 
# the train set and testing set


# 4. create the classifier

# 5. train the classifier

# 6. display results
