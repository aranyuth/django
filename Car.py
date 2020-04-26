class Car:
	color = ""
	brand = ""
	number_of_week = ""
	number_of_seats = ""
	maxspeed = 0

	def __init__(self, color, brand, number_of_week, number_of_seats, maxspeed):
		self.color = color
		self.brand = brand
		self.number_of_week = number_of_week
		self.number_of_seats = number_of_seats
		self.maxspeed = maxspeed

	def setcolor(self, x):
		self.color = x

	def setbrand(self, x):
		self.brand = x

	def setspeed(self, x):
		self.speed = x

	def printdata(self):
		print("Color of this car is ", self.color)
		print("Brand of this car is ", self.brand)
		print("Max speed of this car is ", self.maxspeed)

	def __del__(self):
		print()



