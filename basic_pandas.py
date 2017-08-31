import numpy
import pandas

myarray = numpy.array([
	[101, 'Anuj', 24, 'M'],
	[102, 'Supriti', 26, 'F'],
	[103, 'Piyush', 26, 'M']
])
#rownames = ['Employee 1', 'Employee 2', 'Employee 3']
colnames = ['ID', 'NAME', 'AGE', 'GENDER']
mydataframe = pandas.DataFrame(myarray, columns=colnames)

addData = numpy.array([
	[104, 'Shashank', 25, 'M'],
])
addDataframe = pandas.DataFrame(addData, columns=colnames)

mydataframe = mydataframe.append(addDataframe)
#mydataframe = mydataframe.drop(0)
#mydataframe.pop('GENDER')
mydataframe = mydataframe.reset_index(drop=True);

print(mydataframe)