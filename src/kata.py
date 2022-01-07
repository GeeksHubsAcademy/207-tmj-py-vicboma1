import shlex
import sys


#
# Apply Method
# @param input
# @return
#    
def apply(input):
    #your code here
    return None

def main() -> int:
    phrase = shlex.join(sys.argv)
    print(apply([ 20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
    return 0

if __name__ == '__main__':
    sys.exit(main()) 