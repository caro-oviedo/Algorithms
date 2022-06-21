def factorial(num):
  print(f"Current value: {num}")
  if num == 1 or num == 0:
    print("Process ended")
    return 1
  else:
    return num * factorial (num -1)


print(factorial(5))

# Tail call elimination. Without recursion

def factorialNoRecur(num):
  print(f"Factorial of {num}")
  result = 1

  while num > 1:
    result = result * num
    num = num -1
    print(f"Current value: {num}")

  print("Process ended")
  return result

print(factorialNoRecur(3))
