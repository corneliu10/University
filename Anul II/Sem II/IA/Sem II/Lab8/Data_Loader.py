
import os
import re
from sklearn.utils import shuffle

class Data_Loader:
  def __init__(self):
      dataset_path = "data/txt_sentoken/"
      self.positive_samples_path = dataset_path + "pos/"
      self.negative_samples_path = dataset_path + "neg/"

  # functie care primeste path-ul catre un folder si
  # citeste toate fisierele din el, salvand recenziile intr-o lista
  def read_folder(self, folder_path):
      reviews = []

      for file_name in os.listdir(folder_path):
          file_path = folder_path + file_name
          file = open(file_path, 'r')
          file_content = file.read()
          reviews.append(re.sub("[-.,;:!?\"\'\/()_*=`]", "", file_content).split())
      return reviews

  def build_dataset(self):
      positive_samples = self.read_folder(self.positive_samples_path)
      negative_samples = self.read_folder(self.negative_samples_path)

      # impartim setul de date in 50% pentru antrenare si 50% pentru test
      num_training_samples_per_class = int(0.5 * len(positive_samples))
      num_test_samples_per_class = len(positive_samples) - num_training_samples_per_class

      # in setul de antrenare salvam exemplele pozitive si negative cu indecsii 0:499
      train_data = positive_samples[0:num_training_samples_per_class] + \
                   negative_samples[0:num_training_samples_per_class]

      # exemplele pozitive vor avea eticheta 1, iar cele negative -1
      train_labels = [1] * num_training_samples_per_class + \
                     [-1] * num_training_samples_per_class

      # in setul de test salvam exemplele pozitive si negative cu indecsii 500:999
      test_data = positive_samples[num_training_samples_per_class:len(positive_samples)] + \
                  negative_samples[num_training_samples_per_class:len(negative_samples)]
      test_labels = [1] * num_test_samples_per_class + \
                    [-1] * num_test_samples_per_class

      # amestecam datele
      self.train_data, self.train_labels = shuffle(train_data, train_labels)
      self.test_data, self.test_labels = shuffle(test_data, test_labels)


