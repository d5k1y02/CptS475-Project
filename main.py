from skmultiflow.data.file_stream import FileStream
from skmultiflow.meta import AdaptiveRandomForestClassifier
from datetime import datetime
from numpy import loadtxt
import random
import math
import csv
import pickle
import sys

# Read and load the dataset into memory
stream = FileStream("bodmas.csv")

test_months = []
i = 1
while i < len(sys.argv) - 1:
    test_months.append(sys.argv[i] + ' ' + sys.argv[i + 1])
    i += 2

month_counts = {}
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

print("month counts: ")
print(month_counts)

# Create and train the classifier
classifier = AdaptiveRandomForestClassifier(n_estimators = 100, max_features = 10)

classifier = pickle.load(open("classifier.sav", 'rb'))
for value in month_counts:
    if value in test_months:
        n_samples = 0
        correct_cnt = 0
        while n_samples < month_counts[value] and stream.has_more_samples():
            X, y = stream.next_sample()
            y_pred = classifier.predict(X)
            if y[0] == y_pred[0]:
                correct_cnt += 1
            classifier.partial_fit(X, y)
            n_samples += 1

        # Print results
        print('{} samples analyzed from month '.format(n_samples) + value + '.') #Display results
        print('Accuracy: {}'.format(correct_cnt / n_samples))
    
    else:
        n_samples = 0
        while n_samples < month_counts[value] and stream.has_more_samples():
            stream.next_sample()
            n_samples += 1

    pickle.dump(classifier, open("classifier.sav", 'wb'))
