
# https://open.kattis.com/problems/magictrick
# return 1 if the given string has no repeated letters, 0 otherwise

def dupeCheck(s):
    if len(set(s)) == len(s):
        return(True)
    else:
        return(False)
    
#using python ternary
print(1) if dupeCheck(input()) else print(0)
