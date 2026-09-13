# Dunder __builtins__, __init__
message = "PHYTHON: Everything is object!"
print(message)

result = type(message)
print("result:" result)

''' in Python, there are builtin tools:
(1) TYPES > int float str list dic
(2) FUNCTIONS > print() len() input() type() str() int()
(3) CONSTANTS > True False None
'''

print(dir(__builtins__))
