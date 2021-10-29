
# https://nus.kattis.com/problems/circuitmath

# Read in inputs
n = int(input())
myinput = input().split()
alpha_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
circuitInputs = {}
for i in range(n):
    circuitInputs[alpha_str[i]] = False if myinput[i] == 'F' else True

#print(circuitInputs)

# Read in and evaluate circuit
circuit = input().split()
stack = [] # working stack

'''
Algorithm: https://www.youtube.com/watch?v=n8s7OKSxRxU

Usage of 'first' and 'second':
- 'second' is the item earlier in the list
- since we evaluate from left to right, 'second' needs to be the first operand
'''
for char in circuit:
    if char == '*':
        first = stack.pop()
        second = stack.pop()
        stack.append(second and first)
    elif char == '+':
        first = stack.pop()
        second = stack.pop()
        stack.append(second or first)
    elif char == '-':
        stack.append(not stack.pop())
    else:
        stack.append(circuitInputs[char])

print(str(stack.pop())[0])
