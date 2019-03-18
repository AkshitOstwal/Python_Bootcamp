#two.py
print('hello')
import one

print("top level two.py")

one.func()

if __name__ == '__main__':
	print('two.py is being run directly')
else:
	print('two.py is imported')
