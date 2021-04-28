# Python file for handling personal weather data

import requests

class PersonalData: 

	# Static variables
	wuAPIKey = ""
	baseURL = "https://api.weather.com/v2/pws/observations/current?"
	stationID = "IWHIST7"
	format = "json"
	units = "m"
	precision = "decimal"

	currentData = None 

	def LoadAPIKey(self):
		f = open("config.txt", "r")
		lines = f.readlines() 
		self.wuAPIKey = lines[1].replace("\n", "", 1) 
		
	def GetCurrentData(self):
		requestParams = "stationId={0}&format={1}&units={2}&apiKey={3}&numericPrecision={4}".format(self.stationID, self.format, self.units, self.wuAPIKey, self.precision) 
		requestText = self.baseURL + requestParams 

		response = requests.get(requestText)
		if response.status_code == 200:
			self.currentData = response.json()
			print(self.currentData)



