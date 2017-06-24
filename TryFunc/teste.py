from func import *

def dobro(x):
	return x*2
def app(func, arg):
	return func(arg)
def main():
	resultado = app(dobro, 5)
	print(resultado)
	a=[1,2,3,5]
	print(first(a))
	print(first(rest(a)))
if __name__ == '__main__':
	main()