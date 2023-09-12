expression = input("Enter a mathematical expression: ")
try:
    result = eval(expression)
    print(f"The result of {expression} is {result}")
except Exception as e:
    print(f"An error occurred: {e}")
