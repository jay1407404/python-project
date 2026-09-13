''' Functions
(1) DEFINe vs CALL
(2) Parametr vs Argument
(3) Keword & default arguments
(4) scope
''''


print("======= DEFINE vs CALL =======")
#built in function > print() type()
# Function - reusable block of code!
# Instead of block {} in JAva, Python uses identationn!

#DEFINE - build
def greet(a):
    print(f"how do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"

    # Call - execute
    result1 = greet('Jay')
    print("result1:", result1)

    result2 = greeting("Justin")
    print("result2", result2 )