import sys
import json
from os.path import abspath, isfile

class App:
	def __init__(self,argv):
		self.json_path = abspath(argv)

	def start(self):
		try:
			with open(self.json_path) as json_data:
				data = json.load(json_data)
				print(data[0]['robot'])
		except Exception as e:
			print('unable to find file')
			print(e)
			sys.exit()

if __name__ == "__main__":
	app=App(sys.argv[1])
	app.start()