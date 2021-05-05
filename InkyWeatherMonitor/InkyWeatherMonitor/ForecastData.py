# Python file for handling personal weather data

import requests

class ForecastData: 

	# Static variables
	wuAPIKey = ""
	baseURL = "https://api.weather.com/v3/wx/forecast/daily/5day?"
	lat = ""
	lon = ""
	format = "json"
	units = "m"
	lang = "en-US"

	currentData = None 

	# TODO: Build request string from a dictionary of parameters

	def LoadAPIKey(self):
		f = open("config.txt", "r")
		lines = f.readlines() 
		self.wuAPIKey = lines[1].replace("\n", "", 1) 

	def LoadGeoCode(self):
		f = open("config.txt", "r")
		lines = f.readlines() 
		self.lat = lines[5].replace("\n", "", 1)[5::] 
		self.lon = lines[6].replace("\n", "", 1)[5::] 
				
	def GetForecastData(self):
		requestParams = "geocode={0},{1}&format={2}&units={3}&language={4}&apiKey={5}".format(self.lat, self.lon, self.format, self.units, self.lang, self.wuAPIKey) 
		requestText = self.baseURL + requestParams 

		response = requests.get(requestText)
		if response.status_code == 200:
			self.currentData = response.json()
			#print(self.currentData)



