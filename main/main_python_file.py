import sys
import imports

chce = sys.argv
if '-py' in chce:
    print('choice equals pythagoras')
    imports.pythagoras.main(chce[2], chce[3])
if '-abc' in chce:
    print('choice equals abc formule')
    imports.abc_dingie.main(chce[2], chce[3], chce[4])
else:
    print('usage: python main_python_file.py {choice} {args}')


__name__ == '__main__'
