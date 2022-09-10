import sys
import imports

choice = sys.argv()
if 'py' in choice:
    print('choice equals pythagoras')
    print(str(sys.argv()))
    #imports.pythagoras()
else:
    print('usage: python main_python_file.py {choice} {args}')
print('this is the main python file!')

__name__ == '__main__'
