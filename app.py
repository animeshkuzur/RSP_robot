import sys
import json
from os.path import abspath, isfile

class App:
	def __init__(self,argv):
		self.json_path = abspath(argv)
		self.history = {}

	def start(self):
		try:
			with open(self.json_path) as json_data:
				data = json.load(json_data)
				self.learn(data)
				l = self.length(data)
				self.predict(data[l-3]['robot'],data[l-2]['robot'],data[l-1]['robot'],data[l-1]['you'])
		except Exception as e:
			print('unable to read file')
			print(e)
			sys.exit()

	def predict(self,r1,r2,r3,y1):
		key = str(r1)+str(r2)+str(r3)+str(y1)
		val = 0
		if key in self.history:
			val = self.history[str(r1)+str(r2)+str(r3)+str(y1)]
			val = val + 1
			if(val>2):
				val = 0
			print(val)
		else:
			print('no data')

	def learn(self,data):
		l = self.length(data)
		for i in range(2,l-1):
			key = str(data[i-2]['robot'])+str(data[i-1]['robot'])+str(data[i]['robot'])+str(data[i]['you'])
			val = data[i+1]['you']
			self.history[key] = val
		return 0

	def length(self,data):
		c = 0
		try:
			while(data[c]):
				c = c+1
		except Exception as e:
			pass
		return c

if __name__ == "__main__":
	app = App(sys.argv[1])
	app.start()