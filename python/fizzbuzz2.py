# def fizzbuzz(n: int):
#   answer=[]
#   for i in range (1, n+1):
#     fizz = "Fizz" * (i%3 == 0)
#     buzz = "Buzz" * (i%5 == 0)
#     answer.append( (fizz + buzz) or str(i) )
#   return answer
# # print(fizzbuzz("hello")) #errors at for loop, so type hints (m:int) is just a suggestion, good to know

def fizzbuzz(n:int):
  # list comprehension
  # ditch loops and create list with a shorter syntax
  return [
    ("Fizz" * (i%3==0) + "Buzz" * (i%5==0) or str(i))
    for i in range (1, n+1)
  ]


print(fizzbuzz(15))
