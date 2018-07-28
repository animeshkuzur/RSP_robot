import sys
import json
from os.path import abspath
from random import randint

class App():
	def __init__(self,argv):
		self.json_path = abspath(argv)
		self.data=[]

	def start(self):
		for i in range(0,1000):
			row={}
			if(i==0):
				row['robot'] = 0
				row['you'] = randint(0, 2)
			elif(i==1):
				row['robot'] = 1
				row['you'] = randint(0, 2)
			elif(i==2):
				row['robot'] = 2
				row['you'] = randint(0, 2)
			else:
				row['robot'] = randint(0, 2)
				row['you'] = randint(0, 2)
			self.data.append(row.copy())
		self.write()

	def write(self):
		with open(self.json_path, 'w') as outfile:
			json.dump(self.data, outfile)

if __name__ == "__main__":
	app = App(sys.argv[1])
	app.start()