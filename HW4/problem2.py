
import sys


def main():
	n=input('Enter the number of nodes ')
	n=int(n)
	r=input('Enter R ')
	c=input('Enter C ')
	array=[]
	for i in range(0,n):
		inpu=input()
		array.append(inpu)
	value=[999999]*n

	for i in range(0,n):
		if i==0:
			value[i]=array[i]*r
		elif i<4:
			value[i]=value[i-1]+array[i]*r
		else:
			value[i]=min(value[i-1]+array[i]*r,value[i-4]+4*c)

	print value[n-1]


if __name__ == "__main__":
   main()
