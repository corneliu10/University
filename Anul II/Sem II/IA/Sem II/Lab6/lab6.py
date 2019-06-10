import csv
import re
from sklearn import preprocessing
from sklearn.kernel_ridge import KernelRidge
from sklearn.metrics import mean_squared_error, mean_absolute_error

from Bag_of_Words import *


def read_data(file_path):
    data = []
    scores = []

    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(re.sub("[-.,;:!?\"\'\/()_*=`]", "", row["essay"].lower()).split())
            scores.append(int(row["score"]))
    return data, scores


train_data, train_scores = read_data("Data/train_data.csv")
test_data, test_scores = read_data("Data/test_data.csv")

print("Train data length: texts: %d, scores: %d" % (len(train_data), len(train_scores)))
print("Test data length: texts: %d, scores: %d" % (len(test_data), len(test_scores)))