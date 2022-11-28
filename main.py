from numpy import load
from skmultiflow.data.file_stream import FileStream
# 1. read and load the dataset into memory
stream = FileStream("bodmas.csv")
print(stream.next_sample())
# 2. convert the dataset into a format suitable for learning


# 3. select month of data and split the data into 
# the train set and testing set


# 4. create the classifier

# 5. train the classifier

# 6. display results