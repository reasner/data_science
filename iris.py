'''
Download Fisher's Iris Data Set

The UCI Machine Learning Repository hosts a copy of the data set used by R.A.
Fisher in his seminal work on clustering:

Fisher, Ronald A. "The use of multiple measurements in taxonomic problems."
    Annals of eugenics 7, no. 2 (1936): 179-188.

https://en.wikipedia.org/wiki/Iris_flower_data_set
'''

import urllib.request
import random

iris_url = r'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
csv_name = r'iris.csv'

def download_text_data(url,name):
    response = urllib.request.urlopen(url)
    uncleaned_data = response.read()
    str_data = str(uncleaned_data)
    observations = str_data.split(r'\n')
    observations[0] = observations[0][2:]
    varnames = 'sepel length, sepal width, petal length, petal width, class'
    fw = open(name, 'w')
    fw.write(varnames + '\n')
    for obs in observations:
        fw.write(obs + '\n')
    fw.close()

download_text_data(iris_url, csv_name)
