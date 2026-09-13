print('==========')
# in JAVA, variable is a name storage location!
# i PYTHOn, variable is named reference!

count = 100
count_type = type(count)
print(f"th count: {count} and type: {count_type}")

result1 = count.bit_count() #method
result2 = count.numerator #satte
print(result1, result2)

print("=======string=====")
#METHODS: uper() lower() title() find() replace()
course = "AI PYthon Fullstack"
result = type(course)
print(f"the result (1) : {result}")

result = course.title()
print(f"the result (2): {result}")

result = course.uper()
print(f"the result (3): {result}")

result = course.replace("FullStack", "MasterClass")
print(f"the result (4): {result}")
  

  print("=======boolean=====")
  # function > type() input() bool() int() str()
y = input("Give your value for y: ")
print("y:",y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")

#TRUTH vs FALSY value
#TRUTH: True 100 -100 "MIT"
#FALSY: False 0 "" None

test_falsy = "" or False or None or 0 or 100
print("The test_falsy:", bool(test_falsy))
