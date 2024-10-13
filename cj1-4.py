class Animal:
	def __init__(self, armLength: float, legLength: float, numEyes: int, hasTail: bool, isFurry: bool):
		self.armLength = armLength
		self.legLength = legLength
		self.numEyes = numEyes
		self.hasTail = hasTail
		self.isFurry = isFurry

	def describe(self):
		print(f"Arm length: {self.armLength} meters")
		print(f"Leg length: {self.legLength} meters")
		print(f"Number of eyes: {self.numEyes}")
		print(f"Has a tail: {'Yes' if self.hasTail else 'No'}")
		print(f"Furry: {'Yes' if self.isFurry else 'No'}")

def main():
	cat = Animal(armLength=0.25, legLength=0.3, numEyes=2, hasTail=True, isFurry=True)
	cat.describe()

if __name__=="__main__":
	main()	