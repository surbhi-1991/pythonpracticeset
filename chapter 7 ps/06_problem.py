#  n=int(input("Enter the number: "))
#  product=1
#  for i in ramge(1, n+1):
#     product= product*i

#     print(f"the factorial of {n} is {product}")


def get_factorial_without_recursion(number :int) -> int:
    product: int = 1
    for i in range(1 , number + 1):
        product*= i
    return product


def get_factorial_with_recursion(number :int) -> int | None:
      if number < 0:
        return None
      elif number == 0 or number == 1:
        return 1
      else:
        return number * get_factorial_with_recursion(number - 1)
    

n = int(input("Enter the number : "))

print(f"Factorial of {n} without using recursion is : {get_factorial_without_recursion(n)}")
print(f"Factorial of {n} using recursion is : {get_factorial_with_recursion(n)}")
888888888888888888