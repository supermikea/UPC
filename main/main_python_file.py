import sys
import imports

chce = sys.argv



if '-py' in chce:
	print('choice equals pythagoras')
	try:
		imports.pythagoras.main(chce[2], chce[3])
	except IndexError:
		raise SystemExit(f'Pythagoras requires 2 args')

elif '-abcD'  in chce:
	print('choice equals abc formule -> solve D')
	try:
		imports.abc_formula.main(chce[2], chce[3], chce[4])
	except IndexError:
		raise SystemExit(f'abc formula requires 3 args')

elif '-abcR' in chce:
	print('choice equals abc formule -> solve by factoring')
	try:
		import.solve_refactoring.main()

elif 'help' in chce:
	imports.help.main()
else:
	print('usage: python main_python_file.py {choice} {args}')
	print("For more information type \"help\"")


__name__ == '__main__'
