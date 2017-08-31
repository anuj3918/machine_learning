# import csv
# with open('small_data.csv') as csvfile:
# 	reader = csv.DictReader(csvfile, delimiter=',')
# 	for line in reader:
# 		print(line["first_name"]),
# 		print(line["last_name"])

# import numpy as np
# reader = np.loadtxt("small_data.csv",
# 	dtype={
# 		'names': ('first_name', 'last_name', 'address', 'city', 'state', 'zip_code'),
# 		'formats': ('S15', 'S15', 'S15', 'S15', 'S15', 'S15')
# 	},
# 	delimiter=",",
# 	skiprows=1
# )
# for line in reader:
# 	print(list(line))

from pandas import read_csv

url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(url, names=names)
print(data)