'''
Download Galton's Height Data

This file downloads Galton's famous dataset on the height of children and parent
pair heights with which his idea of regression to the mean is made clear!

Galton, F. (1886) Regression towards mediocrity in hereditary stature.
    Journal of the Anthropological Institute of Great Britain and Ireland,15,
    246–263.
'''
import urllib.request
import random

height_url = r'http://www.randomservices.org/random/data/Galton.txt'
csv_name = r'height.csv'

def download_text_data(url,name):
    response = urllib.request.urlopen(url)
    uncleaned_data = response.read()
    str_data = str(uncleaned_data)
    observations = str_data.split(r'\r')
    len_obs = len(observations)
    for i in range(len_obs):
        observations[i] = observations[i].replace(r'\t',',')
    observations[0] = observations[0][2:]
    fw = open(name, 'w')
    for obs in observations:
        fw.write(obs + '\n')
    fw.close()

download_text_data(height_url, csv_name)
