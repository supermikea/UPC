import sys
import imports

chce = sys.argv
mtrs = False

# Python implementation to check string
# for specific characters
 
# function to check 3 strings
def check(s1,s2,s3, checs):
    result = []
    for i in checs:
       
        # for every character in char array
        # if it is present in string return true else false
        if i in s1:
            result.append("True")
        else:
            result.append("False")
        if i in s2:
                result.append("True")
        else:
            result.append("False")
        if i in s3:
                result.append("True")
        else:
            result.append("False")

    mtrs = True
 
 
# Driver Code
checs = ["cm","mm","km","m"]
s1 = chce[2]  
s2 = chce[3]
s3 = chce[4]

if '-py' in chce: # TODO check how lonk chce is and limit number of chce[4] or 3 to eliminate error if chce[4] isn't there
    print('choice equals pythagoras')
    imports.pythagoras.main(chce[2], chce[3])
if '-abc' in chce:
    print('choice equals abc formule')
    imports.abc_dingie.main(chce[2], chce[3], chce[4])
else:
    print('usage: python main_python_file.py {choice} {args}')


__name__ == '__main__'
