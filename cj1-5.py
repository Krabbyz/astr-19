import math

def table(x):
	print(f"{math.sin(x)}	{x}")

def main():
	x = 0
	for i in range(1000):
		x += math.pi*2/1000
		table(x)

if __name__=="__main__":
	main()