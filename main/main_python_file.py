import sys
import imports

chce = sys.argv
if '-py' in chce:
    print('choice equals pythagoras')
    imports.pythagoras.main(chce[2], chce[3])
else:
    print('usage: python main_python_file.py {choice} {args}')


__name__ == '__main__'
